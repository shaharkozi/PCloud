from tokenize import Double
from InstancesFunction import InstancesFunctions
# from ruleHandler import ruleHandler

class Rule:
    

    def __init__(self,serverType,command,data,tresh,ruleHandler):
        self.Command = command
        self.Data = data
        self.TH = tresh
        self.serverType = serverType
        self.RuleHandler = ruleHandler


    
    def Execute(self):
        json = self.RuleHandler.model_EC2.getCPUUtilization()

        if(self.Data == "CPU"):
            if(self.Command == "Create"):
                if(json["Average"] > self.TH):
                    self.RuleHandler.createInstance(json["ID"])
                if(json["Average"] < self.TH):
                    self.RuleHandler.removeInstance(json["ID"])
            
            #add cpu and io getter