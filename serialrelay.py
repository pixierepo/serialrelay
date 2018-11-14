#!/usr/bin/env python
# coding: utf-8

import serial
import time
import serial.tools.list_ports

class SerialRelay:
    "Simple class for controlling a USB/Serial relay."
    default_open_str = 'A00100A1'
    default_close_str = 'A00101A2'
    
    def __init__(self,port=None):
        ports = serial.tools.list_ports.comports()
        if port==None and len(ports) != 0:
            port = '/dev/'+ports[0].name #Will open the first port available
        try:
            self.port = serial.Serial(port)
        except:   
            print("Error: Can't open serial port!")
    
    def open_relay(self,open_str = default_open_str):
        b = bytes.fromhex(open_str)
        self.port.write(b)
        
    def close_relay(self,close_str = default_close_str):
        b = bytes.fromhex(close_str)
        self.port.write(b)
        
    def toggle(self,t=3,open_str = default_open_str, close_str = default_close_str):
        self.close_relay(close_str)
        time.sleep(t)
        self.open_relay(open_str)
        

