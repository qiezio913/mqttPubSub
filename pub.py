#!/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.publish as publish
import json

print("MQTT Client is Running.")
while True:
    temp = input("Input Temperature: ")
    humi = input("Input Humidity: ")
    if temp == 'exit':
        break
    data = {"temp": int(temp), "humi": int(humi)}
    send_data = json.dumps(data)
    publish.single("/little/qiezi", send_data, hostname="39.97.112.200")
