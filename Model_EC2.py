# import threading
import threading
from threading import *
from multiprocessing import cpu_count, process, Process

import service
from threading import Thread

import boto3
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY
from datetime import datetime, timedelta
import time
import json


class StartThread(Thread):
    def __init__(self, ser):
        self.service = ser

    def run(self):
        #time.sleep(2)
        self.service.Json()
        #time.sleep(2)


class EC2_Model:

    def __init__(self, aws_accesskey, aws_secretkey, instanceid, region):
        self.cpuServiceThread = service.Service("CPUUtilization", "Percent", aws_accesskey, aws_secretkey, instanceid, region)
        self.IoServiceThread = service.Service("DiskReadOps", "Count", aws_accesskey, aws_secretkey, instanceid, region)
        self.netPacOutServiceThread = service.Service("NetPacketOut", "Count", aws_accesskey, aws_secretkey, instanceid, region)

        # self.cpuSer = service.Service("CPUUtilization", "Percent")
        # self.IoSer = service.Service("DiskReadOps", "Count")
        # self.netPacOutSer = service.Service("NetPacketOut", "Count")
        self.serviceArray = [self.cpuServiceThread, self.IoServiceThread]

    def StartAll(self):
        results = []
        thread_list = []
        for ser in self.serviceArray:
            t1 = threading.Thread(target=ser.Json(), args=(ser, results))
            thread_list.append(t1)
        for t1 in thread_list:
            t1.start()
        # for t1 in thread_list:
        #     t1.join()

        # processes = []
        # for ser in self.serviceArray:
        #     p1 = Process(target=ser.Json())
        #     processes.append(p1)
        # for p in processes:
        #     p.start()
        # for p in processes:
        #     p.join()

            # # x = StartThread(ser)
            # # x.run()
            # # time.sleep(2)
            # class StartTheard(Thread):
            #     def run(self):
            #         print("start")
            #         ser.Json()
            #
            # x = StartTheard()
            # x.start()
            # time.sleep(1)
            # x.join()

    def StartOne(self, serviceName):
        # t = Thread(target=self.task(), args=("1",))
        # t.start()
        if(serviceName == "CPUUtilization"):
            self.cpuServiceThread.start()
        if(serviceName == "DiskReadOps"):
            self.IoServiceThread.start()

        #     t = Thread(target=self.task, args=(0)) 
        #     t.start()
        # if(serviceName == "DiskReadOps"):
        #     t = Thread(target=self.task, args=(1)) 
        #     t.start()

        # for ser in self.serviceArray:
        #     if ser.parameter == serviceName:
        #         print(ser.parameter)
        #         x = StartThread(ser)
        #         x.run()
    def getCPUUtilization(self):
        return self.cpuServiceThread.Buffer;