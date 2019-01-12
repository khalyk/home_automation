FROM python:2-alpine

RUN apk add --update git build-base
RUN pip install pigpio
RUN pip install git+https://github.com/iancmcc/ouimeaux.git
COPY DHT22.py .
COPY DHT22.pyc .

COPY humidity_monitor.py .

ENTRYPOINT ["python", "humidity_monitor.py"]
