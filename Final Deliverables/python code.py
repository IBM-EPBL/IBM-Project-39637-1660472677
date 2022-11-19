import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "jj64y3",
        "typeId": "Nodered",
        "deviceId":"12345"
    },
    "auth": {
        "token": "123456789"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform:%s"% cmd.data['command'])
    m=cmd.data['command']
    if(m=='motoron'):
        print("Motor is turned ON")
    elif(m=='motoroff'):
        print("Motor is turned OFF")


client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    ph=random.randint(0,14)
    turb=random.randint(0,10)
    myData={'ph':ph, 'turbidity':turb}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully:", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
