from http.server import HTTPServer
from threading import Thread
from httpController import HttpController
##Volatile
class threadHandler(Thread):
    def __init__(self, port, model_ec2,ruleHandler,qRules):
        Thread.__init__(self)
        self.PORT = port
        self.model_EC2 = model_ec2
        self.ruleHandler = ruleHandler
        self.qRules = qRules

    def run(self):
        HOST = "127.0.0.1"
        # ourServer = 
        # ourServer.setUp(self.model_EC2,self.ruleHandler,self.qRules)
        s = HTTPServer((HOST, self.PORT), HttpController)
        s.serve_forever()
        s.server_close()
