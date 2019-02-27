import time
import messaging as message

from messaging import Publisher

import sys

try:
    params = {
        "address": 'tcp://127.0.0.1',
        "port": '3000',
    }

    # addressport = params["address"] + ':' + params["port"]
    # print (addressport)

    publisher = Publisher(params)

    while True:
        publisher.publish('messages' ,{'message' : 'msg'})
        time.sleep(1)
        publisher.publish('messages' ,'message')
        time.sleep(1)
        publisher.publish('messages' ,['message1', 'message2'])
        publisher.publish('else' ,['message1', 'message2'])

        time.sleep(1)


except KeyboardInterrupt:
    sys.exit(0) # or 1, or whatever
