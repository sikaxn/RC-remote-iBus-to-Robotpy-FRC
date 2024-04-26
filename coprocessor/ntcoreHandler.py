#!/usr/bin/env python3

import ntcore
import time
import serial
import re
ser = serial.Serial('COM5', 9600) #change this to the serial port pico connected to coprocessor.


def parse_data(line):
    """
    Parse the serial data line to extract channel readings.
    Returns a list of floats representing the channel values.
    """
    # Use regular expressions to find channel data
    matches = re.findall(r'Ch \d+ ([+-]?\d+\.\d+)', line)
    # Convert the extracted data to float and return as a list
    return [float(match) for match in matches]

if __name__ == "__main__":
    inst = ntcore.NetworkTableInstance.getDefault()
    table = inst.getTable("flyskyiBus")
    ch1 = table.getDoubleTopic("ch1").publish()
    ch2 = table.getDoubleTopic("ch2").publish()
    ch3 = table.getDoubleTopic("ch3").publish()
    ch4 = table.getDoubleTopic("ch4").publish()
    ch5 = table.getDoubleTopic("ch5").publish()
    ch6 = table.getDoubleTopic("ch6").publish()
    inst.startClient4("example client")
    inst.setServerTeam(9999) # where TEAM=190, 294, etc, or use inst.setServer("hostname") or similar
    inst.startDSClient() # recommended if running on DS computer; this gets the robot IP from the DS
    print("started")
    while True:
        
        data = ser.readline().decode('utf-8').strip()
        try:
            if data:
                #print("received",data)
                channel_data = parse_data(data)
                #print("Channel Data:", channel_data)
        except Exception as e:
            print("Error:", e)
        ch1.set(channel_data[0])
        ch2.set(channel_data[1])
        ch3.set(channel_data[2])
        ch4.set(channel_data[3])
        ch5.set(channel_data[4])
        ch6.set(channel_data[5])
        #time.sleep(1)
        ##ch1.set()
        #x = xSub.get()
        #y = ySub.get()
        #print(f"X: {x} Y: {y}")