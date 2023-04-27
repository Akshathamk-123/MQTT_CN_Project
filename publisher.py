from socket import *
import json
from utils import handleForceExit
from client import Client

class Publisher(Client):

    time_out = 5
    def __init__(self):
        super(Publisher,self).__init__()
        self.data = ""

    def getTopic(self):
        self.topic = input('Enter topic to publish or exit_ to terminate : ')

    def getData(self):
        self.data = input('Enter data to publish : ')

    def getPackedData(self):
        message = json.dumps({'type':'publish','topic':self.topic,'data':self.data})
        return message.encode('utf-8')

    def receiveAck(self):
        try:
            reply = self.socket.recv(self.size)
            print(reply.decode('utf-8'))
        except TimeoutError:
            print('Broker is taking too much time for reply')

    def publish(self):
        self.getData()
        self.socket.send(self.getPackedData())
        self.socket.settimeout(Publisher.time_out)
        self.receiveAck()

    def execute(self):
        self.run(self.publish)

if __name__ == "__main__":
    handleForceExit(Publisher)

