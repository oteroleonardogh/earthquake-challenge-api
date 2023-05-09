# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /code
WORKDIR /code

# Install required packages
RUN pip install --upgrade pip
# Copy the current directory contents into the container at /code
COPY . /code/
RUN pip install -r requirements.txt

# # Run migrations and start the development server
# ENTRYPOINT ["python", "manage.py", "migrate"]
# CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:${API_PORT}"]
