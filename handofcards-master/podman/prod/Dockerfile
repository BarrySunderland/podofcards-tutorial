# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and change to working dir
RUN mkdir /code
WORKDIR /code

# Copy code
COPY /release/ /code/

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifies the command to execute to start the server running.
CMD python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000