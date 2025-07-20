
FROM python:3.14-rc-alpine

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
