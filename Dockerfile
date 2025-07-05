# Use the official slim Python image for smaller footprint
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first (to leverage Docker cache)
COPY requirements.txt .

# Upgrade pip and install dependencies without cache to reduce image size
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port used by the app
EXPOSE 8000

# Start FastAPI with Gunicorn using Uvicorn worker class
CMD ["gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:3000", "--workers", "2"]
