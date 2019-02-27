import time
import messaging as message

from messaging import Responder

import sys

try:
    params = {
        'address': 'tcp://127.0.0.1',
        'port': '3000',
    }

    responder = Responder(params)
    responder.respond('response')
    
except KeyboardInterrupt:
    sys.stdout.flush()
    sys.exit(0) # or 1, or whatever
