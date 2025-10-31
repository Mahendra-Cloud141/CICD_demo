# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Disable Python cache and buffer
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Create a non-root user for security
RUN useradd -m appuser
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY app ./app

EXPOSE 8000
USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
