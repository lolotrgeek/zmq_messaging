import zmq

defaults = {
    'address': 'tcp://127.0.0.1',
    'port': '3000',
}


class Server():
    def __init__(self, params):
        self.params = params
        self.addressport = params["address"] + ':' + params["port"]
        self.context = zmq.Context()


class Requester(Server):
    def __init__(self, params):
        Server.__init__(self, params)
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(self.addressport)
        print('REQ', self.addressport)

    def request(self, request):
        if isinstance(request, str):
            self.socket.send_string(request)
            print('sending string')
        elif isinstance(request, (dict, list)) :
            self.socket.send_json(request)
            print('sending object')
        elif isinstance(request, object) :
            self.socket.send_pyobj(request)
            print('sending object')
        else :
            self.socket.send(request)
            print('sending bytes')

        try :
            print('received string')
            msg = self.socket.recv_string()
        except :
            print('received bytes')
            msg = self.socket.recv()
            try :
                print('received object')
                msg = self.socket.recv_pyobj()
            except:
                pass 
        return msg


class Responder(Server):
    def __init__(self, params):
        Server.__init__(self, params)
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(self.addressport)
        print('RES' , self.addressport)

    def respond(self, response):
        try :
            msg = self.socket.recv_string()
            print('received string')
        except :
            msg = self.socket.recv()
            print('received bytes')
            try :
                msg = self.socket.recv_pyobj()
                print('received object')
            except:
                pass 
        
        if isinstance(response, str) : 
            self.socket.send_string(response)
            print('sending response - string')
        elif isinstance(response, (dict, list)) :
            self.socket.send_json(response)
            print('sending response - json')
        elif isinstance(response, object) :
            self.socket.send_pyobj(response)
            print('sending response - object')
        else :
            self.socket.send(response)
            print('sending response - bytes')

        return response


class Subscriber(Server):
    def __init__(self, params):
        Server.__init__(self, params)
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(self.addressport)
        print('SUB' , self.addressport)

    def subscribe (self, topic):
        self.socket.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))
        try :
            msg = self.socket.recv_string()
            print('received string')
        except:
            print('received bytes')
            msg = self.socket.recv()
            try :
                print('received object') 
                msg = self.socket.recv_pyobj()
            except :
                pass
        return msg

class Publisher(Server):
    def __init__(self, params):
        Server.__init__(self, params)
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(self.addressport)
        print('PUB:' , self.addressport)

    def publish(self, topic, msg):
        print('TOPIC:', topic)
        # encode the msg
        self.socket.send_string(topic, zmq.SNDMORE)
        
        if isinstance(msg, str) : 
            self.socket.send_string(msg)
            print('sending string')
        elif isinstance(msg, (dict, list)) :
            self.socket.send_json(msg)
            print('sending json')
        elif isinstance(msg, object) :
            self.socket.send_pyobj(msg)
            print('sending object')
        else :
            self.socket.send(msg)
            print('sending bytes')