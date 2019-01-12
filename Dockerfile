FROM python:alpine-2

RUN pip install pigpio
RUN pip install git+https://github.com/syphoxy/ouimeaux.git
COPY DHT22.py .
COPY DHT22.pyc .

COPY humidity_monitor.py .

ENTRYPOINT ["python", "humidity_monitor.py"]
