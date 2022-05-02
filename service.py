from threading import Thread
import boto3
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY
from datetime import datetime, timedelta
import time
import json


class Service(Thread):
    def __init__(self, parameter, units, aws_accesskey, aws_secretkey, instanceid, region):
        Thread.__init__(self)
        self.response = None
        self.parameter = parameter
        self.units = units
        self.Buffer = {"Date": [], "Average": []}
        self.INSTANCE_ID = instanceid
        self.region = region
        self.session = boto3.Session(
            aws_access_key_id=aws_accesskey,
            aws_secret_access_key=aws_secretkey,
            region_name=self.region
        )
        self.ec2 = self.session.resource("ec2")
        self.client = self.session.client("cloudwatch", region_name=self.region)
        for instance in self.ec2.instances.all():
            if instance.id == self.INSTANCE_ID:
                self.serverState = instance.state
        self.responceInitialiez()

    def responceInitialiez(self):
        self.response = self.client.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName=self.parameter,
            Dimensions=[{"Name": "InstanceId", "Value": self.INSTANCE_ID}],
            StartTime=datetime.utcnow() - timedelta(seconds=3600),
            EndTime=datetime.utcnow(),
            Period=300,
            Statistics=[
                "Average",
            ],
            Unit=self.units,
        )

    def printServerData(self):
        for instance in self.ec2.instances.all():
            if instance.id == self.INSTANCE_ID:
                print(
                    f"""ID: {instance.id}
                           \nType: {instance.instance_type}
                           \nPublic IPv4: {instance.public_ip_address}
                           \nAMI: {instance.image.id}
                           \nState: {instance.state}
                           \n
                           """
                )

    def Json(self):

       # while self.serverState.get("Name") == 'running':
        # for x in range(3):
        #     time.sleep(1)
        while True:
            datapoints_sorted = sorted(self.response["Datapoints"], key=lambda x: x["Timestamp"])
            for datapoint in datapoints_sorted:
                str = f"{datapoint['Timestamp']}, Average: {datapoint['Average']}"
                # newStr = str +"\n"
                tmp = str.split(",")
                self.Buffer["Date"].append(tmp[0])
                tmp2 = tmp[1].strip()
                tmp3 = tmp2.split(":")
                self.Buffer["Average"].append(tmp3[1])
                # print(self.Buffer)

            # print(self.parameter)
            time.sleep(5)
            print(self.parameter + json.dumps(self.Buffer))
            # self.responceInitialiez()


    def run(self):
        self.Json()