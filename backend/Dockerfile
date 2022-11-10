FROM python:3.10.1-slim

# If no usr/src/app directory exists, create it
# RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# prevent python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# prevent python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# update apt-get to latest
# RUN apt-get update

# Only used in CV projects (opencv)
# RUN apt-get install \
#     'ffmpeg'\
#     'libsm6'\
#     'libxext6' -y

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# EXPOSE 8000

# CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]