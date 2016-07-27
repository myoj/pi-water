#!/usr/bin/env python

import time
import sys
import RPi.GPIO as GPIO

class motor:
	pin_set = []
	StepCounter = 0
	WaitTime = 0.0015

	StepCount = 8
	Seq = []
	Seq = range(0, StepCount)
	Seq[0] = [1,0,0,0]
	Seq[1] = [1,1,0,0]
	Seq[2] = [0,1,0,0]
	Seq[3] = [0,1,1,0]
	Seq[4] = [0,0,1,0]
	Seq[5] = [0,0,1,1]
	Seq[6] = [0,0,0,1]
	Seq[7] = [1,0,0,1]

	def __init__(self, gpio_pins):
		# Set the GPIO pins for the motor
		self.pin_set = [gpio_pins[0], gpio_pins[1], gpio_pins[2], gpio_pins[3]]
		GPIO.setmode(GPIO.BCM)

		# Set all pins to output starting with low power
		for pin in self.pin_set:
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin, False)

		# Give the board a second to adjust
		time.sleep(0.5)

	def shoot(self):
		return

	def shift(self, num_steps):
		GPIO.setmode(GPIO.BCM)
		try:
			print "Starting"
			for x in range(0, abs(num_steps)):
				print "Step: " + str(x)
				for pin in range(0,4):
					cur_pin = self.pin_set[pin]
					print "Pin: " + str(cur_pin)
					print "Why?"
					setting = self.Seq[self.StepCounter][pin]
					print "What?"
					if setting==1:
						print "Set High"
						GPIO.output(cur_pin, True)
					else:
						print "Set Low"
						GPIO.output(cur_pin, False)		

				print "Counting Up"
				if(num_steps > 0):
					self.StepCounter += 1
				else:
					self.StepCounter -= 1

				print "Rotating"
				if (self.StepCounter == self.stepCount):
					self.StepCounter = 0
				elif (self.StepCounter < 0):
					self.StepCounter = self.stepCount

				print "Waiting"
				time.sleep(self.WaitTime)
		except:
			print "Failing"
			for pin in self.pin_set:
				GPIO.setup(pin,GPIO.OUT)
				GPIO.output(pin, False)
		finally:
			print "Finishing"
			for pin in self.pin_set:
				GPIO.setup(pin,GPIO.OUT)
				GPIO.output(pin, False)

if __name__ == "__main__":
	GPIO.setwarnings(False)
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	pins = [14,15,18,17]
	mtr = motor(pins)
	while 1==1:
		mtr.shift(100)




