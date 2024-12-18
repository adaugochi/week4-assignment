FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /src

# Copy the current directory contents into the container
COPY . /src

# Install any needed packages specified in requirements.txt
RUN pip install flask redis

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["python", "app.py"]
