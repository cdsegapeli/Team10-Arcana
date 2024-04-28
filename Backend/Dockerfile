FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 7200

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "7200"]