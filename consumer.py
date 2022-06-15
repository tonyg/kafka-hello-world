#!/usr/bin/env python3

import time
from kafka import KafkaConsumer

# import logging
# import sys
# logger = logging.getLogger('kafka')
# logger.addHandler(logging.StreamHandler(sys.stdout))
# logger.setLevel(logging.DEBUG)

consumer = KafkaConsumer('hello-world')

# for m in consumer:
#     print(m)

# while True:
#     print('Polling')
#     print(consumer.poll(timeout_ms=5000))

# while True:
#     print('Polling')
#     print(consumer.poll(timeout_ms=0))
#     print('Sleeping')
#     time.sleep(5)

# while True:
#     print('Polling')
#     print(consumer.poll(timeout_ms=1))
#     print('Sleeping')
#     time.sleep(5)

while True:
    print('Polling')
    ms=0  # 1 and 5 both seem to work just fine, 0 I'm not 100% on
    print(consumer.poll(timeout_ms=ms))
    print(consumer.poll(timeout_ms=ms))
    print('Sleeping')
    time.sleep(5 - (2 * ms / 1000.0))
