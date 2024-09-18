from fastapi import FastAPI
from kafka import KafkaConsumer
import json
import threading

app = FastAPI()

# Kafka Consumer to listen for changes

consumer = KafkaConsumer(
    'banking.banking.accounts',
    bootstrap_servers=['kafka:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='test-group'
)

print(consumer)



# Notification handler
def notify(change_event):
    
    payload = change_event["payload"]["after"]
    account_number = payload["account_number"]
    balance = payload["balance"]
    print(f"Notification: Account {account_number} balance updated to {balance}")

# Background listener to consume Kafka messages
def kafka_listener():
    print("listener started")
    for message in consumer:
        change_event = message.value
        notify(change_event)

# Start Kafka listener in a background thread
listener_thread = threading.Thread(target=kafka_listener)
listener_thread.daemon = True
listener_thread.start()

@app.get("/")
async def read_root():
    return {"message": "Notification service running and listening to account changes"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
