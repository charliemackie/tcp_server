import cv2
import pickle
import struct
import socket
import threading

client = socket.socket()

host = "52.39.126.12"
port = 5000

conn = client.connect((host, port))

payload_size = struct.calcsize("Q")

print("Connected @", conn)

def send():
    while(True):
        try:
            # OpenCV function, this will open the webcam on current machine
            vid = cv2.VideoCapture(0)
            while(vid.isOpened()):

                # metadata from the video frames (ex: pixel RGB values)
                img, frame = vid.read()
                a = pickle.dumps(frame)
                message = struct.pack("Q", len(a)) + a

                # send frames from local webcam
                conn.sendall(message)
                cv2.imshow('Sending ...', frame)
        except:
            break

t1 = threading.Thread(target = send)
t1.start()
t1.join()
