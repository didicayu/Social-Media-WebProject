FROM python:3.12-slim

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory
WORKDIR /app

# Install poetry and then use it to install dependencies
RUN pip install poetry && poetry install

# Expose port 8000 for the application
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
