import socket
# socket.AF_INET --> transfer the message through internet
# socket.SO CK_DGRAM --> using the UDP Protocol(user datagram protocol)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# to coneect the system we need Ip_address
# ip_address=("192.168.1.4")
ip_address="127.0.0.1" #local host



# we also need the port no to transfer the message at correct location
port_no=2525  # range of port no is 0 - 65353
# and 0 to 1023 are reserved
complete_addres=(ip_address,port_no)

#  Now we have to register the reciever address using bindfunction()
# until the address will not register the reciever is not capable to recieve the message
s.bind(complete_addres)
print("hey i am listening:")
while True: 
    Data=s.recvfrom(100)
    # print(message)
    message=Data[0]
    message=message.decode('ascii')
    # message = message.decode('ascii')
    

    sender_address=Data[1]
    # print(Message)
    print(sender_address)
    file=open("reciever_ipaddres.txt","a")
    file.write(message)
    file.close()
    
    
    
    
    



