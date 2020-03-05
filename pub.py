#!/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.publish as publish

print("MQTT Client is Running.")
while True:
    msg = input("Input Something")
    if msg == 'exit':
        break
    publish.single("/little/qiezi", msg, hostname="39.97.112.200")
