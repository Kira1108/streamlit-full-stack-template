FROM python:3.10.1-slim

WORKDIR /app

RUN apt-get update

# Only used in CV projects (opencv)
# RUN apt-get install \
#     'ffmpeg'\
#     'libsm6'\
#     'libxext6' -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]