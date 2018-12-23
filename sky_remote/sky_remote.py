#!/bin/python3
import socket
import math

class SkyRemote:
    # Sky ports , Legacy is firmware earlier than 0.6
    PORT_SKY_Q = 49160
    SKY_Q_LEGACY = 5900
 
    # Button codes
    BUTTON_POWER = 0
    BUTTON_SELECT = 1
    BUTTON_BACKUP = 2
    BUTTON_DISMISS = 2
    BUTTON_CHANNELUP = 6
    BUTTON_CHANNELDOWN = 7
    BUTTON_INTERACTIVE = 8
    BUTTON_SIDEBAR = 8
    BUTTON_HELP = 9
    BUTTON_SERVICES = 10
    BUTTON_SEARCH = 10
    BUTTON_TVGUIDE = 11
    BUTTON_HOME = 11
    BUTTON_I = 14
    BUTTON_TEXT = 15 
    BUTTON_UP = 16
    BUTTON_DOWN = 17
    BUTTON_LEFT = 18
    BUTTON_RIGHT = 19
    BUTTON_RED = 32
    BUTTON_GREEN = 33
    BUTTON_YELLOW = 34
    BUTTON_BLUE = 35
    BUTTON_0 = 48
    BUTTON_1 = 49
    BUTTON_2 = 50
    BUTTON_3 = 51
    BUTTON_4 = 52
    BUTTON_5 = 53
    BUTTON_6 = 54
    BUTTON_7 = 55
    BUTTON_8 = 56
    BUTTON_9 = 57
    BUTTON_PLAY = 64
    BUTTON_PAUSE = 65
    BUTTON_STOP = 66
    BUTTON_RECORD = 67
    BUTTON_FASTFORWARD = 69
    BUTTON_REWIND = 71
    BUTTON_BOXOFFICE = 240
    BUTTON_SKY = 241
  
    def __init__(self, host, port=PORT_SKY_Q):
        # Set host and port
        self.host = host
        self.port = port

    def send_command(self, code):
        # Create a TCP/IP socket
        stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ((self.host, self.port))
 
        #Open connection
        stream_socket.settimeout(1000)
        stream_socket.connect(server_address)
        
        try:
            # Handshake first exchange string "SKY 000.001"
            data = stream_socket.recv(1024)
            stream_socket.sendall(data[:13])
            # Then exchange "0x01,0x01"
            data = stream_socket.recv(1024)
            stream_socket.sendall(data[:2])
           
            # Now send commands
            frame1 = bytes([0x04,0x01,0x00,0x00,0x00,0x00,math.floor(224 + (code/16)),code % 16])
            stream_socket.sendall(frame1)
            frame2 = bytes([0x04,0x00,0x00,0x00,0x00,0x00,math.floor(224 + (code/16)),code % 16])
            stream_socket.sendall(frame2)        

            # Close connection
            stream_socket.close()

        except socket.timeout:
            print('connection timed out')
            
def detect_devices():
    # Uses UDP to return a list of Sky boxes on the network.
    
    
    