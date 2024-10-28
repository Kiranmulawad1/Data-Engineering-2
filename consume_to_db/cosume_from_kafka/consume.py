from kafka import KafkaConsumer
import json 
from collections.abc import Iterator

def consume_from_topics(topic:str)->Iterator[dict|None]:
    consumer = KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False,
    bootstrap_servers='kafka:9092',consumer_timeout_ms=5000)
    consumer.subscribe(topic)

    for message in consumer:
        try :
            value =  json.loads(message[6].decode('utf-8'))
        except IndexError:
            value =None
        yield value 
    
if __name__=="__main__":
    print(consume_from_topics('rank'))

