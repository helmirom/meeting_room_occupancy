#Pull official base image
FROM python:3.8.10-slim-buster

#Set workdir
WORKDIR /usr/src/frontend

#Prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0
ENV STREAMLIT_SERVER_PORT 8080

#Update container
RUN apt-get update \
  && apt-get clean


# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .


RUN pip install -r requirements.txt

# add app
COPY . .