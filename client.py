from template import Template
class Client(Template):

    def __init__(self):
        super(Client, self).__init__()
        self.serverAddress = (self.serverIP,self.serverPort)
        self.topic = ""

    def run(self, callable):
        self.socket.connect(self.serverAddress)
        addr = self.socket.getsockname()
        self.log(f'Connected from {addr[0]}:{addr[1]}')
        while True:
            self.getTopic()
            self.shouldExit(self.topic)
            callable()

