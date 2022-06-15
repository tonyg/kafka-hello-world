#!/usr/bin/env python3

import time
from kafka import KafkaProducer

# import logging
# import sys
# logger = logging.getLogger('kafka')
# logger.addHandler(logging.StreamHandler(sys.stdout))
# logger.setLevel(logging.DEBUG)

producer = KafkaProducer()

count = 0
while True:
    print('Sending', count)
    producer.send('hello-world', str(count).encode('utf-8'))
    producer.flush()
    count = count + 1
    time.sleep(1)
