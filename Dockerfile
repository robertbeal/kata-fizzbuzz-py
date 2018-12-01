FROM python:alpine

WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /data
COPY . .

CMD ["nosetests", "tests"]

