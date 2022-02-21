from socket import *
import base64


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "My message"
    endmsg = "Done"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    
    # Fill in start
    # Fill in end
    mailserver = 'smtp.gmail.com'
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,587))


    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    # Fill in end
    mailFrom = "mr6439@nyu.edu"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    print("After MAIL FROM command: "+recv2)

    # Send RCPT TO command and handle server response.
    # Fill in start
    # Fill in end
    rcptTo = "praveenrajendran2109@gmail.com"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    print("After RCPT TO command: "+recv3)

    # Send DATA command and handle server response.
    # Fill in start
    # Fill in end
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    print("After DATA command: "+recv4)

    # Send message data.
    # Fill in start
    # Fill in end
    subject = "Subject: SMTP mail client testing" 
    clientSocket.send(subject.encode())
    message = raw_input("Enter your message:")
    clientSocket.send(message.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    print("Response after sending message body:"+recv_msg.decode())

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    # Fill in end
    clientSocket.send("QUIT\r\n".encode())
    message=clientSocket.recv(1024)
    print (message)
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
