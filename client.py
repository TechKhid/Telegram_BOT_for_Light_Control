from websocket import create_connection
import asyncio

# ws = create_connection("ws://192.168.43.183:81")
ws = create_connection("ws://192.168.100.178:81")

def send_payload(msg):
    ws.send(msg)

if __name__ == "__main__":
    send_payload(msg)