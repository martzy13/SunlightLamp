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

def setAllColor(ring, color):
        for i in range(ring.numPixels()):
		ring.setPixelColor(i, color)
	ring.show()
		

def killTheLights(ring):
	for i in range(ring.numPixels()):
                ring.setPixelColor(i,Color(0,0,0))
	ring.show()

def setAllBrightnewss(ring, level):
	for i in range(ring.numPixels):
		ring.setBrightness(i,level)
	ring.show()

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	ring = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	ring.begin()
	# register killTheLights method on exit of the program
        atexit.register(killTheLights, ring)
	print ('Press Ctrl-C to quit.')
	wakeup_hour = 21

	while True:
		local_time = datetime.now(pytz.timezone("America/New_York"))
              	# print(local_time.hour)
		if local_time.hour == wakeup_hour:
			#print ('TIME TO WAKE UP!')
			if local_time.minute <= 30:
		                setAllColor(ring, Color(0, 0, 255))  # Blue
				if local_time.minute <= 10:
					#set brightness low
					setAllBrightness(ring, 85)
					time.sleep(1)
				elif local_time.minute <= 20:
					#set brightness medium
					setAllBrightness(ring, 170)
					time.sleep(1)
				elif local_time.minute <= 25:
					#set brightness to high
					setAllBrightness(ring, 255)
					time.sleep(1)
				else :
					# play that funky music white boy. 
					# flash and strobe and stuff. 
					print("WOAHKSADFJADSK")

