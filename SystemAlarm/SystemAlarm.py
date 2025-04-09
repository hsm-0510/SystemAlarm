import time
from time import sleep
from datetime import datetime
import socket

EE_packet = "*01EE\r\\n" #Get Extended Status
EA_packet = "*01EA SY\r\\n" #Get Enquire System Alarms

def send_ascii_packet(ip, port, packet):
    global responseA
    responseA = "000000"
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the specified IP and port
        sock.connect((ip, port))
        #print(f"Connected to {ip} on port {port}")
        
        # Send the ASCII packet
        sock.sendall(packet.encode('ascii'))  # Encode the string to ASCII bytes
        #print(f"Sent packet: {packet}")
        
        # Receiving a Response
        response = sock.recv(1024)
        responseA = response.decode('ascii')
        #print(f"{response.decode('ascii')},, end=" ")
        #print(f"Bit Caught: {responseA[5]}")
    
    except Exception as e:
        print(" ")
    
    finally:
        # Close the connection
        sock.close()
        #print("Connection closed")

def decoder(dict, array, i, j):
    if i == '1':
        array = list(dict.keys())
        key_change = array[3 + (j*4)]
        dict[key_change] = 1
    elif i == '2':
        array = list(dict.keys())
        key_change = array[2 + (j*4)]
        dict[key_change] = 1
    elif i == '3':
        array = list(dict.keys())
        key_change = array[3 + (j*4)]
        dict[key_change] = 1
        key_change = array[2 + (j*4)]
        dict[key_change] = 1
    elif i == '4':
        array = list(dict.keys())
        key_change = array[1 + (j*4)]
        dict[key_change] = 1
    elif i == '5':
        array = list(dict.keys())
        key_change = array[3 + (j*4)]
        dict[key_change] = 1
        key_change = array[1 + (j*4)]
        dict[key_change] = 1
    elif i == '6':
        array = list(dict.keys())
        key_change = array[2 + (j*4)]
        dict[key_change] = 1
        key_change = array[1 + (j*4)]
        dict[key_change] = 1
    elif i == '7':
        array = list(dict.keys())
        key_change = array[3 + (j*4)]
        dict[key_change] = 1
        key_change = array[2 + (j*4)]
        dict[key_change] = 1
        key_change = array[1 + (j*4)]
        dict[key_change] = 1
    elif i == '8':
        array = list(dict.keys())
        key_change = array[0 + (j*4)]
        dict[key_change] = 1
    elif i == '9':
        array = list(dict.keys())
        key_change = array[3 + (j*4)]
        dict[key_change] = 1
        key_change = array[0 + (j*4)]
        dict[key_change] = 1
    elif i == ':':
        array = list(dict.keys())
        key_change = array[2 + (j*4)]
        dict[key_change] = 1
        key_change = array[0 + (j*4)]
        dict[key_change] = 1
    elif i == ';':
        array = list(dict.keys())
        key_change = array[3 + (j*4)]
        dict[key_change] = 1
        key_change = array[2 + (j*4)]
        dict[key_change] = 1
        key_change = array[0 + (j*4)]
        dict[key_change] = 1
    elif i == '<':
        array = list(dict.keys())
        key_change = array[1 + (j*4)]
        dict[key_change] = 1
        key_change = array[0 + (j*4)]
        dict[key_change] = 1
    elif i == '=':
        array = list(dict.keys())
        key_change = array[3 + (j*4)]
        dict[key_change] = 1
        key_change = array[1 + (j*4)]
        dict[key_change] = 1
        key_change = array[0 + (j*4)]
        dict[key_change] = 1
    elif i == '>':
        array = list(dict.keys())
        key_change = array[2 + (j*4)]
        dict[key_change] = 1
        key_change = array[1 + (j*4)]
        dict[key_change] = 1
        key_change = array[0 + (j*4)]
        dict[key_change] = 1
    elif i == '?':
        array = list(dict.keys())
        key_change = array[3 + (j*4)]
        dict[key_change] = 1
        key_change = array[2 + (j*4)]
        dict[key_change] = 1
        key_change = array[1 + (j*4)]
        dict[key_change] = 1
        key_change = array[0 + (j*4)]
        dict[key_change] = 1

def main():
    #Assign IP & Port of Batch Controller
    ip_address = "192.168.10.131"
    port = 7734
    try:
        EA_dict = {'RAM Corrput':0, 'Flash Error':0, 'RAM Bad':0, 'ROM Bad':0,
                   'Passcode Reset':0, 'System Program Error':0, 'Watchdog':0, 'Finish Backup Bad':0,
                   'User Alarm 3':0, 'User Alarm 2':0, 'User Alarm 1':0, 'Power Fail Alarm':0,
                   'Ticket Alarm':0, 'Communications':0, 'User Alarm 5':0, 'User Alarm 4':0,
                   'Pulse Security':0, 'Add Clean Line':0, 'Overrun Alarm':0, 'Zero Flow Alarm':0,
                   'Density Trans':0, 'Temp Probe':0, 'Back Pressure':0, 'Valve Fault':0,
                   'High Density':0, 'High Temp':0, 'High Flow':0, 'Pressure Trans':0,
                   'Low Density':0, 'Low Temp':0, 'Low Flow':0, 'High Pressure':0,
                   'Mass Meter Tube':0, 'Mass Meter Overdrive':0, 'Mass Meter Comm Fail':0, 'Low Pressure':0,
                   'Report Full Storage':0, 'Promass Alarm':0, 'Shared Printer':0, 'PTB Printer Failure':0,
                   'Not Used':0, 'Divert Timeout Alarm':0, 'BS&W Probe Alarm':0, 'Network Printer Alarm':0}
        EE_dict = {'Program Mode':0, 'Released':0, 'Flowing':0, 'Authorized':0,
                   'Transaction in Progress':0, 'Transaction Done':0, 'Batch Done':0, 'Keypad Data Pending':0,
                   'Printing in Progress':0, 'Permissive Delay':0, 'New Card Data Available':0, 'Alarm':0,
                   'Program Value Changed':0, 'Delayed Prompt in Effect':0, 'Display Message Time-Out':0, 'Power-Fail Occured':0,
                   'Checking Entries':0, 'Input #1':0, 'Input #1':0, 'Input #1':0,
                   'Pending Reports':0, 'Report Storage Full':0, 'Printer Standby':0, 'Preset in Progress':0,
                   'Reserved':0, 'Reserved':0, 'BS&W Limit Exceeded':0, 'Diverting':0,
                   'Reserved':0, 'Reserved':0, 'Reserved':0, 'Reserved':0}
        while True:
            # ENQUIRE ALARMS
            send_ascii_packet(ip_address, port, EA_packet)
            j = 0
            print(responseA)
            for i in responseA[3:16]:
                decoder(EA_dict, EA_array, i, j)
                j += 1
            time.sleep(1)
            j = 0
            for i in EA_array:
                print(f"{EA_array_named[j]} : {i}")
                j += 1
            
            # EXTENDED STATUS
            send_ascii_packet(ip_address, port, EE_packet)
            j = 0
            print(responseA)
            for i in responseA[3:11]:
                decoder(EE_dict, EE_array, i, j)   
                j += 1
            time.sleep(1)
            j = 0
            for i in EE_array:
                print(f"{EE_array_named[j]} : {i}")
                j += 1
    except KeyboardInterrupt:
        print("Stopped")

if __name__ == "__main__":
    main()
