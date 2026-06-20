import asyncio
import random
import websockets
import json
import sys, getopt
import time
from datetime import datetime

def get_connected_msg(client_no):
   msg_dict = {
         "deviceId": "client"+str(client_no),
         "messageId": "ABC",
         "timestamp": "12:00:00",
         "elementId": int(client_no),
         "payload":
         {
            "connected": True,
            "type": "Port",
            "hwVersion": "1.0",
            "swVersion": "1.0"
         }
      }
   return msg_dict


def get_acknowledge_msg(msg_dict):
   #if client_no > 0:
   #   msg_dict["deviceId"] = "client"+str(client_no)
   
   task = msg_dict["payload"]['task']
   msg_dict["payload"] = {
                              "confirmedTask": task,
                           }
   return msg_dict


def get_result_msg(msg_dict,sleep_time):
   msg_dict["payload"] = {
                              "solved": random.choice([True,False]),
                              "time": sleep_time,
                              "direction": random.choice(['TP_A_TO_B','TP_B_TO_A','TP_UNDEF']),
                              "speed": sleep_time*25
                           }
   return msg_dict


async def client_handler(uri,client_no):
    print(uri)
    async with websockets.connect(uri) as websocket:
        msg_dict = get_connected_msg(client_no)
        msg_json = json.dumps(msg_dict)
        await websocket.send(msg_json)
        while True:
            msg = await websocket.recv()
            # Process the received message and update highscore_data accordingly
            recv_time = datetime.now()
            sleep_time = random.random()*0.1 + (int(client_no)*0.5)
            await asyncio.sleep(sleep_time)
            print("Received: %s at: %s",msg,recv_time)
            json_dict = json.loads(msg) 
            if json_dict["payload"]['task'] == 'init':
               element_id = json_dict["payload"]['elementId']
               print("Assigned element_id:%d",element_id)
               json_dict["payload"]['elementId'] = element_id
               msg_dict = get_acknowledge_msg(json_dict)
               msg_json = json.dumps(msg_dict)
               await websocket.send(msg_json)
            elif json_dict["payload"]['task'] == 'set':
               await asyncio.sleep(0.1)
               msg_dict = get_result_msg(json_dict,sleep_time)
               msg_json = json.dumps(msg_dict)
               await websocket.send(msg_json)
               send_time = datetime.now()
               print("send: %s at: %s",msg_json,send_time)
               print('processing_time: %d', send_time - recv_time)


def main(argv):
   client_no =  argv[0] 
   asyncio.run(client_handler("ws://localhost:8080",client_no))

if __name__ == "__main__":
   main(sys.argv[1:])
