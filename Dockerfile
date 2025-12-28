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
COPY site_twilight/requirements.txt ./site_twilight/
RUN python -m pip install --upgrade pip uv && \
    uv pip install --system -r site_twilight/requirements.txt

# Copy application
COPY site_twilight/ ./site_twilight/

# Collect static files
WORKDIR /app/site_twilight
RUN python manage.py collectstatic --noinput

EXPOSE $PORT
CMD gunicorn site_twilight.wsgi:application --bind 0.0.0.0:$PORT