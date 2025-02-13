FROM python:3.11.4

RUN mkdir /movies

WORKDIR /movies

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

