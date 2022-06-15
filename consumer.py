#!/usr/bin/env python3

from kafka import KafkaConsumer

# import logging
# import sys
# logger = logging.getLogger('kafka')
# logger.addHandler(logging.StreamHandler(sys.stdout))
# logger.setLevel(logging.DEBUG)

consumer = KafkaConsumer('hello-world')

# for m in consumer:
#     print(m)

while True:
    print('Polling')
    print(consumer.poll(timeout_ms=5000))
