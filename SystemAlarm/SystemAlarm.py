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

def main():
    #Assign IP & Port of Batch Controller
    ip_address = "192.168.10.131"
    port = 7734
    try:
        EA_array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        EE_array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        EA_array_named = ['RAM Corrput', 'Flash Error', 'RAM Bad', 'ROM Bad',
                          'Passcode Reset', 'System Program Error', 'Watchdog', 'Finish Backup Bad',
                          'User Alarm 3', 'User Alarm 2', 'User Alarm 1', 'Power Fail Alarm',
                          'Ticket Alarm', 'Communications', 'User Alarm 5', 'User Alarm 4',
                          'Pulse Security', 'Add Clean Line', 'Overrun Alarm', 'Zero Flow Alarm',
                          'Density Trans', 'Temp Probe', 'Back Pressure', 'Valve Fault',
                          'High Density', 'High Temp', 'High Flow', 'Pressure Trans',
                          'Low Density', 'Low Temp', 'Low Flow', 'High Pressure',
                          'Mass Meter Tube', 'Mass Meter Overdrive', 'Mass Meter Comm Fail', 'Low Pressure',
                          'Report Full Storage', 'Promass Alarm', 'Shared Printer', 'PTB Printer Failure',
                          'Not Used', 'DV: Divert Timeout Alarm', 'SW: BS&W Probe Alarm', 'NP:Network Printer Alarm']
        EE_array_named = ['Program Mode', 'Released', 'Flowing', 'Authorized',
                          'Transaction in Progress', 'Transaction Done', 'Batch Done', 'Keypad Data Pending',
                          'Printing in Progress', 'Permissive Delay', 'New Card Data Available', 'Alarm',
                          'Program Value Changed', 'Delayed Prompt in Effect', 'Display Message Time-Out', 'Power-Fail Occured',
                          'Checking Entries', 'Input #1', 'Input #1', 'Input #1',
                          'Pending Reports', 'Report Storage Full', 'Printer Standby', 'Preset in Progress',
                          'Reserved', 'Reserved', 'BS&W Limit Exceeded', 'Diverting',
                          'Reserved', 'Reserved', 'Reserved', 'Reserved']
        while True:
            # ENQUIRE ALARMS
            send_ascii_packet(ip_address, port, EA_packet)
            j = 0
            print(responseA)
            for i in responseA[3:16]:
                if i == '1':
                    EA_array[3 + (j*4)] = 1
                elif i == '2':
                    EA_array[2 + (j*4)] = 1
                elif i == '3':
                    EA_array[3 + (j*4)] = 1
                    EA_array[2 + (j*4)] = 1
                elif i == '4':
                    EA_array[1 + (j*4)] = 1
                elif i == '5':
                    EA_array[3 + (j*4)] = 1
                    EA_array[1 + (j*4)] = 1
                elif i == '6':
                    EA_array[2 + (j*4)] = 1
                    EA_array[1 + (j*4)] = 1
                elif i == '7':
                    EA_array[3 + (j*4)] = 1
                    EA_array[2 + (j*4)] = 1
                    EA_array[1 + (j*4)] = 1
                elif i == '8':
                    EA_array[0 + (j*4)] = 1
                elif i == '9':
                    EA_array[3 + (j*4)] = 1
                    EA_array[0 + (j*4)] = 1
                elif i == ':':
                    EA_array[2 + (j*4)] = 1
                    EA_array[0 + (j*4)] = 1
                elif i == ';':
                    EA_array[3 + (j*4)] = 1
                    EA_array[2 + (j*4)] = 1
                    EA_array[0 + (j*4)] = 1
                elif i == '<':
                    EA_array[1 + (j*4)] = 1
                    EA_array[0 + (j*4)] = 1
                elif i == '=':
                    EA_array[3 + (j*4)] = 1
                    EA_array[1 + (j*4)] = 1
                    EA_array[0 + (j*4)] = 1
                elif i == '>':
                    EA_array[2 + (j*4)] = 1
                    EA_array[1 + (j*4)] = 1
                    EA_array[0 + (j*4)] = 1
                elif i == '?':
                    EA_array[3 + (j*4)] = 1
                    EA_array[2 + (j*4)] = 1
                    EA_array[1 + (j*4)] = 1
                    EA_array[0 + (j*4)] = 1   
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
                if i == '1':
                    EE_array[3 + (j*4)] = 1
                elif i == '2':
                    EE_array[2 + (j*4)] = 1
                elif i == '3':
                    EE_array[3 + (j*4)] = 1
                    EE_array[2 + (j*4)] = 1
                elif i == '4':
                    EE_array[1 + (j*4)] = 1
                elif i == '5':
                    EE_array[3 + (j*4)] = 1
                    EE_array[1 + (j*4)] = 1
                elif i == '6':
                    EE_array[2 + (j*4)] = 1
                    EE_array[1 + (j*4)] = 1
                elif i == '7':
                    EE_array[3 + (j*4)] = 1
                    EE_array[2 + (j*4)] = 1
                    EE_array[1 + (j*4)] = 1
                elif i == '8':
                    EE_array[0 + (j*4)] = 1
                elif i == '9':
                    EE_array[3 + (j*4)] = 1
                    EE_array[0 + (j*4)] = 1
                elif i == ':':
                    EE_array[2 + (j*4)] = 1
                    EE_array[0 + (j*4)] = 1
                elif i == ';':
                    EE_array[3 + (j*4)] = 1
                    EE_array[2 + (j*4)] = 1
                    EE_array[0 + (j*4)] = 1
                elif i == '<':
                    EE_array[1 + (j*4)] = 1
                    EE_array[0 + (j*4)] = 1
                elif i == '=':
                    EE_array[3 + (j*4)] = 1
                    EE_array[1 + (j*4)] = 1
                    EE_array[0 + (j*4)] = 1
                elif i == '>':
                    EE_array[2 + (j*4)] = 1
                    EE_array[1 + (j*4)] = 1
                    EE_array[0 + (j*4)] = 1
                elif i == '?':
                    EE_array[3 + (j*4)] = 1
                    EE_array[2 + (j*4)] = 1
                    EE_array[1 + (j*4)] = 1
                    EE_array[0 + (j*4)] = 1   
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
