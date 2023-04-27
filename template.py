import os
from socket import socket, AF_INET, SOCK_DGRAM
import sys
from datetime import datetime
from utils import parseInt


class Template:

    # default server props
    PORT = 12000
    IP = 'localhost'

    # default buffer size
    BUFFER_SIZE = 1024

    def __init__(self):
        self.socket = socket(AF_INET,SOCK_DGRAM)
        self.serverIP= Template.IP
        self.serverPort = parseInt(os.environ.get('PORT', None)) or Template.PORT
        self.size = Template.BUFFER_SIZE

    def log(self, message):
        print(f'{datetime.now()}: {message}')

    def execute(self):
        raise NotImplementedError

    def closeConnection(self):
        self.socket.close()

    def shouldExit(self, topic):
        if topic == 'exit_':
            self.closeConnection()
            sys.exit(0)