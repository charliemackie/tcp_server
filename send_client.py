import cv2
import pickle
import struct
import socket
import threading

host = "52.39.126.12"
port = 60000

payload_size = struct.calcsize("Q")

# make a streaming socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))

    # max amount of connections to listen for
    s.listen(5)
    print("Listening on port", port)

    # connect with client on another machine & network
    conn, addr = s.accept()
    print("Accepted connection:", conn, addr)
    
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
    

