from guizero import App, PushButton, Text, TextBox
import serial
import time
from picamera import PiCamera
from os import system
import shutil
from datetime import datetime

camera = PiCamera()
camera.resolution = (720, 720)

ser=serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)

def recordObject():


    camera.start_preview()
    time.sleep(3)

    for i in range(0, 15):
        camera.capture('/home/pi/Documents/spinTemp/image%s.jpg' % i)
        print('image')
        time.sleep(1)
        ser.write(str('L').encode())
        time.sleep(1)
    camera.capture('/home/pi/Documents/spinTemp/image15.jpg')
    camera.stop_preview()
    print('begin conversion')
    strCount = str(fileNameNum)
    system('convert -delay 20 -loop 0 /home/pi/Documents/spinTemp/image*.jpg /home/pi/Desktop/SpinGifs/spin.gif')
    print('conversion complete')

    newFileName = '/home/pi/Desktop/SpinGifs/' + TextBox.get(fileNameText) + TextBox.get(fileNameNum) +'.gif'
    tempName = '/home/pi/Desktop/SpinGifs/spin.gif'
    shutil.move(tempName, newFileName)
    print('File Renamed')




def testCamera():
    camera.start_preview()
    time.sleep(10)
    camera.stop_preview()



app = App(title="Spin Control")
message = Text(app, text="Welcome to Spin Control")
recordButton = PushButton(app, command=recordObject, text="Record")
testButton = PushButton(app, command=testCamera, text="Test Camera")
fileNameText = TextBox(app, text="spin")
fileNameNum = TextBox(app, width = "3", text="0")
app.display()
