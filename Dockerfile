FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# make a directory in our Docker image in which we can use to store our source code
# Copy the project folder from our local machine to the docker image
RUN mkdir /project
WORKDIR /project

COPY . .
