# SpinControl
A simple python program to let your Raspberry Pi run Tiffany Tseng's Spin Device [spin.media.mit.edu](http://spin.media.mit.edu)
Once running, there is an Aim button and a Spin button. Aim turns the camera on for 10 seconds so that you can set up your rig, the Spin button will take 16 images, spinning your object 22.5 degrees between each image, and stitch them together into an animated GIF which will be placed in a folder named SpinGifs on your Pi Desktop.

My goal was to make this simple to setup and use, taking a cue from its creator and her elegant tablet/phone apps. Please leave any problems / suggestion in [Issues](https://github.com/PCswanson/spincontrol/issues)

![alt text](https://github.com/PCswanson/spincontrol/blob/master/IMG_3986.jpg)


## Hardware Requirements
* Raspberry Pi
* Raspberry Pi camera
* SPIN [spin.media.mit.edu](http://spin.media.mit.edu)


## Setup
* Set up your Pi with the standard Raspian image. I hooked up a touchscreen I had handy, but this will work just the same with a mouse and keyboard.
* Use the Setup program to enable the Pi Camera.
* You will need to install the following packages (thanks to bsteinbach112 for pointing this out!):
  * guizero (and potentially libjpeg-dev) - https://lawsie.github.io/guizero/
  * pyserial -  https://pyserial.readthedocs.io/en/latest/pyserial.html
  * imagemagick - sudo apt-get update
                  sudo apt-get install imagemagick
* Use whatever setup you need to attach/rig/aim the camera. If you are in need of something, you can buy Pi Camera holders from Pimoroni or Adafruit or find files to 3D Print or Lasercut on multiple sites including thingiverse.com
* Place spincontrol.py in your documents folder.
* Create a spinTemp folder in your documents folder
* Create a SpinGifs folder on your desktop (this is where your final objects will go).
* Either start SpinControl.py from IDLE3 or from the command line: python3 SpinControl.py
* It should just work!
