import cv2
import pickle
import struct
import socket

# IP of the EC2 server
host = "52.39.126.12"
port = 60000

# size of a long type in bits
payload_size = struct.calcsize("Q")

# streaming socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    
    conn.connect((host, port))

    with conn:
        if conn:
        # recv function recieves data up to input size of bytes
            data = conn.recv(4096)

            while True:
                while len(data) < payload_size:
                    packet = conn.recv(4*1024)
                    if not packet: 
                        break
                    data += packet
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("Q", packed_msg_size)[0]
                while len(data) < msg_size:
                    data += conn.recv(4*1024)
                frame_data = data[:msg_size]
                data = data[msg_size:]
                frame = pickle.loads(frame_data)
                cv2.imshow("Receiving...", frame)
                key = cv2.waitKey(1)
        conn.close()
        cv2.destroyAllWindows()
