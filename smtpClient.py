Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from socket import *
... 
... def smtp_client(port=1025, mailserver='127.0.0.1'):
...     msg = "\r\nMy message"
...     endmsg = "\r\n.\r\n"
... 
...     # Step 1: Create a socket and establish a TCP connection
...     clientSocket = socket(AF_INET, SOCK_STREAM)
...     clientSocket.connect((mailserver, port))
... 
...     # Receive and check server response
...     recv = clientSocket.recv(1024).decode()
...     if recv[:3] != '220':
...         print('220 reply not received from server.')
... 
...     # Step 2: Send HELO command and print server response.
...     heloCommand = 'HELO Alice\r\n'
...     clientSocket.send(heloCommand.encode())
...     recv1 = clientSocket.recv(1024).decode()
...     if recv1[:3] != '250':
...         print('250 reply not received from server.')
... 
...     # Step 3: Send MAIL FROM command and handle server response.
...     mailFromCommand = 'MAIL FROM:<alice@example.com>\r\n'
...     clientSocket.send(mailFromCommand.encode())
...     recv2 = clientSocket.recv(1024).decode()
...     if recv2[:3] != '250':
...         print('250 reply not received from server.')
... 
...     # Step 4: Send RCPT TO command and handle server response.
...     rcptToCommand = 'RCPT TO:<bob@example.com>\r\n'
...     clientSocket.send(rcptToCommand.encode())
...     recv3 = clientSocket.recv(1024).decode()
...     if recv3[:3] != '250':
...         print('250 reply not received from server.')
... 
...     # Step 5: Send DATA command and handle server response.
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    if recv4[:3] != '354':
        print('354 reply not received from server.')

    # Step 6: Send message data.
    clientSocket.send(msg.encode())

    # Step 7: End message with single period and handle server response.
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    if recv5[:3] != '250':
        print('250 reply not received from server.')

    # Step 8: Send QUIT command and handle server response.
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    if recv6[:3] != '221':
        print('221 reply not received from server.')

    # Close the socket
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
