
FROM python:3.14-rc-alpine

RUN apk update && apk add build-base python3-dev musl-dev libpq-dev

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python3", "app.py"]
