import time
import messaging as message

from messaging import Requester

import sys

try:
    params = {
        'address': 'tcp://127.0.0.1',
        'port': '3000',
    }

    requester = Requester(params)
    response = requester.request('request')
    print(response)
    
except KeyboardInterrupt:
    sys.stdout.flush()
    sys.exit(0) # or 1, or whatever
