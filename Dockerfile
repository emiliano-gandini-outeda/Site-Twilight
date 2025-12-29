FROM node:20-slim AS frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

FROM python:3.12-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy frontend build
COPY --from=frontend /app/frontend/dist /app/frontend/dist

# Install Python dependencies
COPY site_twilight/pyproject.toml site_twilight/uv.lock ./site_twilight/

RUN python -m pip install --upgrade pip uv \
 && cd site_twilight \
 && uv sync --frozen

# Copy application
COPY site_twilight/ ./site_twilight/

WORKDIR /app/site_twilight

# Create emergency admin
RUN .venv/bin/python manage.py ensure_admin


# Collect static files
RUN .venv/bin/python manage.py collectstatic --noinput

EXPOSE $PORT
CMD .venv/bin/python manage.py migrate --noinput && \
    .venv/bin/gunicorn site_twilight.wsgi:application --bind 0.0.0.0:$PORT