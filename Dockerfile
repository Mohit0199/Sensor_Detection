FROM python:3.8-slim-buster

# Install build essentials
RUN apt-get update && apt-get install -y build-essential

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Install Cython first (if required)
RUN pip install Cython

# Install PyYAML separately
RUN pip install PyYAML==5.4.1

# Install other dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
