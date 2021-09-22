import cv2
import pickle
import struct
import socket
import threading

client = socket.socket()

host = "52.39.126.12"
port = 60000

conn = client.connect((host, port))

payload_size = struct.calcsize("Q")

def rec():
    while(True):
        print("Connected @", conn)
        try:
            while len(data) < payload_size:
                packet = conn.recv(4096)
                if not packet: 
                    break
                data += packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]
            while len(data) < msg_size:
                data += conn.recv(4096)
            frame_data = data[:msg_size]
            data  = data[msg_size:]
            frame = pickle.loads(frame_data)
            cv2.imshow("Receiving ...",frame)
        except:
            break

t1 = threading.Thread(target = rec)
t1.start()
t1.join()
