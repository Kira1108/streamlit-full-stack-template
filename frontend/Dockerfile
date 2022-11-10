FROM python:3.10.1-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# EXPOSE 8501

# CMD ["streamlit", "run", "main.py"]