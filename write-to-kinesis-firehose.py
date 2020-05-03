import boto3
from faker import Faker
import random
import time
import json

DeliveryStreamName = 'clickstream-delivery'

client = boto3.client('firehose')

fake = Faker()

fake = Faker()
actions = ['clickbtn'+ str(x) for x in range(40)]
names = ["Davi", "Sarah", "Joao P", "Danilo", "Mamai", "Isabela", "Karina"]

record = {}
while True:
    #record['user'] = fake.name()
    record['action'] = random.choice(actions)
    record['name'] = random.choice(names)
    record['timestamp'] = time.time()
    response = client.put_record
        DeliveryStreamName=DeliveryStreamName,
        Record={
            'Data': json.dumps(record)
        }
    )
    print('PUTTING RECORD TO KINESIS FIREHOSE: \n' + str(record))