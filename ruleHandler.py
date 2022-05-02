import imp
from queue import Queue
from InstancesFunction import InstancesFunctions
import Model_EC2
from rule import Rule
import service
from threading import Thread


class RuleHandler(Thread):

    def __init__(self, model_ec2, queue:Queue):
        Thread.__init__(self)
        self.model_EC2 = model_ec2
        self.insCre = InstancesFunctions()
        self.rulesString = queue

    def addRule(self, rule):
        parts = rule.split("/")

        rule = Rule()
        rule.serverType = parts[0]
        rule.Data = parts[1]
        rule.Command = parts[2]
        rule.TH = parts[3]
        self.rules.append(rule)
        return '{ "value":"true" }'

    def removeRule(self, rule):
        parts = rule.split("/")
        for r in self.rules:
            if(r.serverType == parts[0] and r.Data == parts[1] and r.Command == parts[2] and r.TH == parts[3]):
                self.rules.remove(rule)
                
        return '{ "value":"true" }'

    def handleRules(self):
        while True:
            if(not self.rulesString.empty()):
                data = self.rulesString.get()


    def createInstance(self,str):
        self.insCre.InstanceCreator(str) 

    def removeInstance(self, str):
        self.insCre.InstanceRemover(str) 

    def stopInstance(self,str):
        self.insCre.InstanceStoper(str) 

    def run(self):
        self.handleRules()