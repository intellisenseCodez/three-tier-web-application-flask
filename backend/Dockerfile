# Use an official Python runtime as a parent image
FROM python:3.11-alpine

ENV ENV_MODE=test

# Set working directory
WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose application port
EXPOSE 5000

# Run application
ENTRYPOINT ["python3", "app.py"]