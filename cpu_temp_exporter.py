#!/usr/bin/python3

from prometheus_client import start_http_server, Gauge
import os
import time

g = Gauge('cpu_temp', 'CPU Temperature')


def process_request(t):
    time.sleep(t)


if __name__ == '__main__':
    start_http_server(9111)
    while True:
        sensors = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()
        temp = (sensors.replace("temp=", "").replace("'C\n", ""))
        g.set(float(temp))
        process_request(5)
