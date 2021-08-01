import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "cp3p3y",
        "typeId": "firstdevice",
        "deviceId":"kris123"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    fooditems={"i1":{"item":"chicken biriyani","price":100},"i2":{"item":"chicken noodles","price":120},"i3":{"item":"chicken friedrice","price":130},
                 "i4":{"item":"veg biriyani","price":100},"i5":{"item":"veg noodles","price":110},"i6":{"item":"egg biriyani","price":125}}
    myData={'fooditems':fooditems}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
    break
client.disconnect()

def myCommandCallback(cmd):
 print("Food order received from IBM IoT Platform: %s" % cmd.data['order_qty']) 
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
    
 client.commandCallback = myCommandCallback
 time.sleep(2)
client.disconnect()
