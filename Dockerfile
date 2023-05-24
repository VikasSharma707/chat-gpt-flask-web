# Base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask code to the container
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the Flask app port
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["flask", "run"]
