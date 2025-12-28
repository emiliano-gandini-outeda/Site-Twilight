#!/usr/bin/env bash
set -e

echo "=== Building frontend ==="
cd frontend
npm install
npm run build --base /static/
cd ..

echo "=== Installing Python dependencies ==="
cd site_twilight
python -m pip install --upgrade pip uv
uv pip install -r requirements.txt

echo "=== Collecting static files ==="
python manage.py collectstatic --noinput

echo "=== Starting Django ==="
gunicorn site_twilight.wsgi:application --bind 0.0.0.0:$PORT
