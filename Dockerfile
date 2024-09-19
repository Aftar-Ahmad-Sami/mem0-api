# This Dockerfile sets up a container for a Python 3.11 application using a slim base image.
# 
# Environment variables:
# - PYTHONDONTWRITEBYTECODE: Prevents Python from writing .pyc files to disk.
# - PYTHONUNBUFFERED: Ensures that the Python output is sent straight to the terminal without being buffered.
#
# The working directory is set to /app.
#
# System dependencies installed:
# - gcc: GNU Compiler Collection.
# - libpq-dev: PostgreSQL development libraries.
#
# Python dependencies are installed from requirements.txt.
#
# The current directory contents are copied into the container at /app.
#
# A non-root user named 'appuser' is created and the container switches to this user.
#
# Port 8000 is exposed for external access.
#
# The application is run using Gunicorn with Uvicorn workers, listening on all network interfaces at port 8000.
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]

