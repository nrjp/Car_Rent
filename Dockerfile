# FROM python:3.9-slim-buster

# WORKDIR /app

# COPY requirements.txt requirements.txt

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY . .

# CMD [ "python3", "manage.py", "runserver","0.0.0.0:8000" ]

# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set environment variables for PostgreSQL
ENV POSTGRES_DB=test
ENV POSTGRES_USER=test
ENV POSTGRES_PASSWORD=test

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install PostgreSQL and set up a database with user and password
RUN apt-get update && apt-get install -y postgresql && \
    service postgresql start && \
    su - postgres -c "psql -c 'CREATE DATABASE $POSTGRES_DB;'" && \
    su - postgres -c "psql -c 'CREATE USER $POSTGRES_USER WITH PASSWORD '\''$POSTGRES_PASSWORD'\'';'" && \
    su - postgres -c "psql -c 'ALTER ROLE $POSTGRES_USER SET client_encoding TO '\''utf8'\'';'" && \
    su - postgres -c "psql -c 'ALTER ROLE $POSTGRES_USER SET default_transaction_isolation TO '\''read committed'\'';'" && \
    su - postgres -c "psql -c 'ALTER ROLE $POSTGRES_USER SET timezone TO '\''UTC'\'';'" && \
    su - postgres -c "psql -c 'GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER';"

# Expose the port the app runs on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
