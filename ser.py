import serial
from datetime import datetime
import time
#test
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("pass.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://auto-f76e1-default-rtdb.firebaseio.com'})

root = db.reference()
serial_port = 'COM3'
previous_value = None

try:
    # with serial.Serial(serial_port, baudrate=9600, timeout=1) as ser:
    #     print(f"Connected to {serial_port}")
    #     while True:
    #         value = ser.readline().strip()
    #         if len(value) == 0:
    #             value = '0'
            
    #         # Compare current value with previous value
    #         # if value != previous_value:
    #         root.update({'switch': value})
            
    #         previous_value = value
    #         print(value)
    time.sleep(5)
    for i in range(0, 24, 3):
        print(i%2)
        time.sleep(3)
        root.update({'switch': i%2})
except serial.SerialException as e:
    print(f"Error: {e}")
