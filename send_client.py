import cv2
import pickle
import struct
import socket

host = "52.39.126.12"
port = 60000

payload_size = struct.calcsize("Q")

# make a streaming socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    
    conn.connect((host, port))
    
    with conn:
        if conn:
            # OpenCV function, this will open the webcam on current machine
            vid = cv2.VideoCapture(0)
            while(vid.isOpened()):

                # metadata from the video frames (ex: pixel RGB values)
                img, frame = vid.read()
                a = pickle.dumps(frame)
                message = struct.pack("Q", len(a)) + a

                # send frames from local webcam
                conn.sendall(message)
                cv2.imshow('Sending...', frame)
                key = cv2.waitKey(10) 
                if key == 13:
                    conn.close()
    

