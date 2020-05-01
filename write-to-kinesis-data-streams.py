import boto3
from faker import Faker
import random
import time
import json

DeliveryStreamName = 'kinesis-1'

client = boto3.client('kinesis',region_name='us-east-1')

fake = Faker()
actions = ['clickbtn'+ str(x) for x in range(40)]
names = ["Davi", "Sarah", "Joao P", "Danilo", "Mamai", "Isabela", "Karina"]

record = {}
while True:
    #record['user'] = fake.name()
    record['action'] = random.choice(actions)
    record['name'] = random.choice(names)
    record['timestamp'] = time.time()
    response = client.put_record(
        StreamName=DeliveryStreamName,
        Data=json.dumps(record),
        PartitionKey=random.choice(names)
    )
    print('PUTTING RECORD TO KINESIS: \n' + str(record))