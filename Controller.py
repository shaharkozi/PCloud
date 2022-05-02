import view
from Model_EC2 import EC2_Model
from ruleHandler import RuleHandler
from InstanceCreaton import InstanceCreator
from InstancesFunction import InstancesFunctions

class Controller():
    def __init__(self):
        self.dict = {}

    def addRuleTodict(self,serverType, rule):
        self.dict[serverType] = rule

    def applyRule(self, rule, user_details):
        # if rule['Type'] == 'EC2':
        # EC2 = EC2_Model(aws_accesskey, aws_secretkey, instanceid, region)
        # EC2.StartOne("CPUUtilization")
        instance = InstancesFunctions(user_details)
        # create_instance.create_key_pair()
        # instance.InstanceStoper(user_details["instance_id"])
        instance.getInstanceState()