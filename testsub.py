import time
import messaging as message

from messaging import Subscriber
import sys

try:
    params = {
        "address": 'tcp://127.0.0.1',
        "port": '3000',
    }

    subscriber = Subscriber(params)

    while True:
        msg = subscriber.subscribe('messages')
        print (type(msg))
        print(msg)

except KeyboardInterrupt:
    sys.exit(0) # or 1, or whatever
