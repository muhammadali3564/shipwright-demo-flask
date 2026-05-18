# Shipwright Demo Flask App

A small Flask + Bootstrap web application used as a demo deployment for the Shipwright platform.

## Features

- Home page with a hero section
- About page with tech stack info
- Contact page with a working POST form
- Health check at /health
- Production-ready Dockerfile

## Local development

```bash
pip install -r requirements.txt
python app.py
```

Visit http://localhost:8000

## Deployment

Built to deploy via Shipwright. The Dockerfile builds a Python 3.11-slim image and runs Gunicorn with 2 workers on port 8000.
