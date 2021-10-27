key = input()

while True:
    if key == 'a':
        print("up")

# rec side 
message = input()
conn.sendall(message)

# send side
data = conn.recv(4096)
print(message)