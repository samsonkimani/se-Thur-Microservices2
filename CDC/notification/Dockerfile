# Use official Python image as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python dependencies
RUN pip install --no-cache-dir fastapi uvicorn mysql-connector-python kafka-python

# Expose the FastAPI service port (you can use different ports for each service)
EXPOSE 8001

# Command to run the FastAPI application
CMD ["uvicorn", "notification_service:app", "--host", "0.0.0.0", "--port", "8001"]
