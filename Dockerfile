# Pull official base Python Docker image
FROM python:3.12.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
# RUN chmod u+x wait-for-it.sh

# Copy the Django project
COPY . .