import serial
import time

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("pass.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://auto-f76e1-default-rtdb.firebaseio.com'})

root = db.reference()

print(root.child('switch').get())