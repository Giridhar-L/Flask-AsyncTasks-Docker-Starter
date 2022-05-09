FROM python:3.8
COPY . /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# RUN apt update && apt install gcc nano -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT gunicorn --config ./app/gunicorn.conf.py app.server:app
