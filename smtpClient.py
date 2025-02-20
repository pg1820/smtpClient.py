from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\nMy message"
    endmsg = "\r\n.\r\n"

    # Step 1: Create a socket and establish a TCP connection
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # Receive server response
    recv = clientSocket.recv(1024).decode()
    if recv[:3] != '220':
        return  # Exit if no proper response

    # Step 2: Send HELO command
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] != '250':
        return  # Exit if no proper response

    # Step 3: Send MAIL FROM command
    mailFromCommand = 'MAIL FROM:<alice@example.com>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    if recv2[:3] != '250':
        return

    # Step 4: Send RCPT TO command
    rcptToCommand = 'RCPT TO:<bob@example.com>\r\n'
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    if recv3[:3] != '250':
        return

    # Step 5: Send DATA command
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    if recv4[:3] != '354':
        return

    # Step 6: Send the email message
    clientSocket.send(msg.encode())

    # Step 7: End the message with a period on a line by itself
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    if recv5[:3] != '250':
        return

    # Step 8: Send QUIT command
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    if recv6[:3] != '221':
        return

    # Close the socket connection
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
