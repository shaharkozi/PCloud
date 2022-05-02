
from threading import Thread
import Model_EC2
import serverThreadHandler
from ruleHandler import RuleHandler
from queue import Queue
from view import View
from Controller import Controller
from httpController import HttpController

def main():
    ec2Model = Model_EC2.EC2_Model()
    qRules = Queue()
    ruleHandler = RuleHandler(ec2Model,qRules)
    # s1 = serverThreadHandler.threadHandler(7000,ec2Model,ruleHandler,qRules)
    # controller = HttpController()
    # s = Thread(target = controller.run)
    # s.start()
    
    ruleHandler.start()
    ec2Model.StartOne("CPUUtilization")
    ec2Model.StartOne("DiskReadOps")
    # s1.start()

    # obj.StartAll()


if __name__ == "__main__":
    controller = Controller()
    view = View(controller)
    view.start()
