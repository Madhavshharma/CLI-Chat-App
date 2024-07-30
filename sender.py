import socket  # socket is like the end point of system (door)


# socket.AF_INET --> transfer the message through internet
# socket.SO CK_DGRAM --> using the UDP Protocol(user datagram protocol)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

target_ip="127.0.0.1"
target_port=2525

target_address=(target_ip,target_port)

condition = True
while condition:
    message =input("Plz enter your message:-")
    message_encrypted=message.encode('ascii')
    s.sendto(message_encrypted,target_address)
    print("Your message is sent succesfully-")
    permission = input("Please enter ")
    if permission=="Y" or permission=="y":
        condition==False
