from socket import *
from socket import error as SocketError
from template import Template
from threading import Thread, Lock, active_count
import traceback
import json
from utils import handleForceExit

class Broker(Template):

    publishedData = dict()
    subscriberData = dict()

    def __init__(self):
        super(Broker,self).__init__()
        self.lock = Lock()
        self.socket.bind((self.serverIP,self.serverPort))
        self.log(f'Broker started at {self.serverIP}:{self.serverPort}')

    def addPublishData(self, data):
        topic = data['topic']
        self.lock.acquire()
        current_data = Broker.publishedData.get(topic,[])
        current_data.append(data['data'])
        Broker.publishedData[topic] = current_data
        self.lock.release()


    def respond(self, data, addr):
        message = str(data).encode('utf-8')
        self.lock.acquire()
        self.socket.sendto(message,addr)
        self.lock.release()

    def pushData(self,topic):
        subscribers = Broker.subscriberData.get(topic,[])
        data = '\n'.join(Broker.publishedData.get(topic, []))
        toRemove = []
        for subscriber in subscribers:
            self.respond(data, subscriber)
            toRemove.append(subscriber)
        for item in toRemove: Broker.subscriberData[topic].remove(item)

    def addSubscriber(self, topic, addr):
        self.lock.acquire()
        subscribers = Broker.subscriberData.get(topic, [])
        subscribers.append(addr)
        Broker.subscriberData[topic] = subscribers
        self.lock.release()

    def handleSubscriber(self,data, addr):
        topic =  data['topic']
        dataItems = Broker.publishedData.get(topic, None)
        if dataItems:
            self.respond('\n'.join(dataItems),addr)
        else:
            self.addSubscriber(topic, addr)

    def handlePublisher(self, data, addr):
        if 'data' not in data or len(str(data['data']).strip()) == 0:
            self.log('Publisher sent message with incorrect format')
            self.respond('Invalid data provided', addr)
            return
        self.addPublishData(data)
        self.respond('Broker has recieved message', addr)
        self.pushData(data['topic'])

    def handleSender(self,data,addr):
        if data['type'] == 'publish':
            self.log(f'Publisher has published from {addr[0]}:{addr[1]}')
            self.handlePublisher(data,addr)
        elif data['type'] == 'subscribe':
            self.log(f'Subscriber has subscribed from {addr[0]}:{addr[1]}')
            self.handleSubscriber(data, addr)

    def startHandlerThread(self, data, addr):
        try:
            Thread(target=self.handleSender, args=(data, addr), daemon=True).start()
        except:
            self.log('Cannot start new thread')
            traceback.print_exc()
            self.respond('Broker has got an error', addr)


    def getCleanedMessage(self, message, addr):
        if not message:
            return
        data = json.loads(message.decode('utf-8'))
        if (not data) or ('type' not in data) or ('topic' not in data):
            self.respond('Invalid request provided', addr)
            return
        if len(str(data['topic']).strip()) == 0:
            self.respond('Invalid topic provided', addr)
            return
        data['topic'] = str(data['topic']).strip()
        return data

    def execute(self):
        while True:
            msgIn, addr = self.socket.recvfrom(self.size)
            data = self.getCleanedMessage(msgIn, addr)
            if not data:
                continue
            self.startHandlerThread(data, addr)

if __name__ == "__main__":
    handleForceExit(Broker)