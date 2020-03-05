#!/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json


def on_message(mqttc, obj, msg):
    print('-' * 30)
    print("Topic: ", msg.topic)
    print("Qos: ", msg.qos)
    _payload = str(msg.payload, 'utf-8')
    print("Payload: ", _payload)
    data = json.loads(_payload)
    print("Temperature: ", data["temp"])
    print("Humidity: ", data["humi"])


mqttc = mqtt.Client()
mqttc.on_message = on_message

mqttc.connect("39.97.112.200", 1883, 60)
mqttc.subscribe("/little/qiezi", 0)

print('MQTT Client is Running.')

mqttc.loop_forever()
