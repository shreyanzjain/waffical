# Use the official Python 3.13.3 slim image as a base
FROM python:3.13.3-slim

# Copy the requirements file into the container
COPY . /app

# Set the working directory inside the container
WORKDIR /app
# Install the Python dependencies
# --no-cache-dir reduces the image size
# --upgrade pip ensures we have the latest version
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# Expose port 8000 to allow communication with the application
EXPOSE 8000

# Command to run the application using uvicorn
# --host 0.0.0.0 makes the server accessible from outside the container
# CMD ["uvicorn", "/app/main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["fastapi", "run"]
