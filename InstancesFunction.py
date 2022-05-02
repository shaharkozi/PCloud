import boto3
import credentials #add another python file for the keys

#Should get the Instance ID for those functions except the creation.
class InstancesFunctions:

    def __init__(self, user_details):
        self.region = user_details["region"]
        self.accesskey = user_details["access_key"]
        self.secretkey = user_details["secret_key"]
        self.ami = user_details["ami"]

    def instanceRemover(self, ids):
        # connect to the client using the keys
        # insert your own keys below
        ec2 = boto3.client('ec2',
                           self.region,
                           aws_access_key_id=self.accesskey,
                           aws_secret_access_key=self.secretkey)


        # Terminate ec2 instance
        ec2.terminate_instances(InstanceIds=ids)
        print("Removed the Instance")


    def instanceStoper(self, ids):
            # connect to the client using the keys
        # insert your own keys below
        ec2 = boto3.client('ec2',
                            self.region,
                            aws_access_key_id = self.accesskey,
                            aws_secret_access_key = self.secretkey)


        # Terminate ec2 instance
        ec2.stop_instances(InstanceIds=ids)
        print("Stopped the Instance")


    def instaceStarter(self, ids):
            # connect to the client using the keys
        # insert your own keys below
        ec2 = boto3.client('ec2',
                            self.region,
                           aws_access_key_id=self.accesskey,
                           aws_secret_access_key=self.secretkey)


        # Terminate ec2 instance
        ec2.start_instances(InstanceIds=ids)
        print("Started the Instance")


    def instanceCreator(self):
            # connect to the client using the keys
        # insert your own keys below
        ec2 = boto3.client('ec2',
                           self.region,
                           aws_access_key_id=self.accesskey,
                           aws_secret_access_key=self.secretkey)

        conn = ec2.run_instances(InstanceType="t2.micro",
                            MaxCount = 1,
                            MinCount = 1,
                            ImageId = self.ami)

        print("Instance created")

    def getInstanceState(self):
        client = boto3.client('ec2',
                           self.region,
                           aws_access_key_id=self.accesskey,
                           aws_secret_access_key=self.secretkey)
        ec2 = client.describe_instances()
        for pythonins in ec2['Reservations']:
            for instance in pythonins['Instances']:
                retdict = {instance["InstanceId"]:{"InstanceType": instance["InstanceType"],
                            "State": instance["Monitoring"]["State"]}}

        print(retdict)
        return retdict




    # InstanceCreator()
    # InstanceStoper()
    # InstaceStarter()
    # InstanceRemover()