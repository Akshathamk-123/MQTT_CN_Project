from socket import *
import json
from utils import handleForceExit
from client import Client

class Subscriber(Client):

    def __init__(self):
        super(Subscriber, self).__init__()

    def getTopic(self):
        self.topic = input('Enter topic to subscribe or exit_ to terminate : ')

    def pack(self):
        message = json.dumps({'type':'subscribe','topic':self.topic})
        return message.encode('utf-8')

    def receiveData(self):
        reply = self.socket.recv(self.size * 2)
        print(reply.decode('utf-8'))

    def subscribe(self):
        self.socket.send(self.pack())
        self.receiveData()

    def execute(self):
        self.run(self.subscribe)

if __name__ == "__main__":
    handleForceExit(Subscriber)

