#used the strand test as my example layout. 
import time
import datetime
import atexit
import pytz

from neopixel import *
from datetime import datetime

# LED strip configuration:
LED_COUNT      = 12      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# wakeup hour - 24 hour format. Will kick off at this time. 
# use regular integer
wakeup_hour = 6

def setCountColor(ring, color, count)
	for i in range(count):
		ring.setPixelColor(i, color)
	ring.show()

def setAllColor(ring, color):
        for i in range(ring.numPixels()):
		ring.setPixelColor(i, color)
	ring.show()
		

def killTheLights(ring):
	for i in range(ring.numPixels()):
                ring.setPixelColor(i,Color(0,0,0))
	ring.show()


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	ring = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	ring.begin()
	# register killTheLights method on exit of the program
        atexit.register(killTheLights, ring)
	#message of how to quit
	print ('Press Ctrl-C to quit.')
	# Initial blink to indicate script running
	ring.setBrightness(85)
	ring.setPixelColor(1, Color(155,155,155)) 
	ring.show()
	time.sleep(1)
	ring.setPixelColor(1,Color(0,0,0))
	ring.show()

	print("initialized")
	print("Wakeup time is " +  str(wakeup_hour))
	time.sleep(3)

	while True:
		local_time = datetime.now(pytz.timezone("America/New_York"))
              	print(local_time)
		# wait 60 seconds in between checking the time.	
		# will cause a 2 minute delay because of the delay within loop
		time.sleep(60)
		if local_time.hour == wakeup_hour:
			#print ('TIME TO WAKE UP!')
			#if local_time.minute <= 30:
		                setAllColor(ring, Color(255, 255, 255))  #white
				if local_time.minute <= 10:
					#set brightness low
					print("setting brightness to low")
					setCountColor(ring, Color(15, 15, 15),6) #set half the pixels to Grey
					ring.setBrightness(10) #set brightness very low
					ring.show()
					time.sleep(60) #wait a minute (601)
					ring.setBrightness(15) #set brightness to just sort of low
					time.sleep(240) #Wait a few minute(604)
					setAllColor(ring, color(50,50,50)) #slightly lighter grey
				elif local_time.minute <= 20:
					#set brightness medium
					print("setting brightness to medium")
					ring.setBrightness(100)
					ring.show()
					time.sleep(60)
				elif local_time.minute <= 25:
					#set brightness to high
					print("setting brightness to high")
					ring.setBrightness(255)
					ring.show()
					time.sleep(60)
				else :
					# play that funky music white boy. 
					# flash and strobe and stuff. 
					print("Time to wake up")
					time.sleep(10)
