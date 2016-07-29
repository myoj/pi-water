#!/usr/bin/env python

import math
import time
import sys
import RPi.GPIO as GPIO

class motor:
	pin_set = []
	StepCounter = 0
	WaitTime = 0.0015
	StepsPerDegree = 11.378

	stepCount = 8
	Seq = []
	Seq = range(0, stepCount)
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

	def shift(self, degrees):
		num_steps = int(math.ceil(degrees * self.StepsPerDegree))
		GPIO.setmode(GPIO.BCM)
		try:
			print "Starting" + str(num_steps)
			step_for = num_steps
			if(step_for < 0):
				step_for *= -1

			for x in range(0, step_for):
				print "whatup1"
				for pin in range(0,4):
					print "whatup1.5"
					cur_pin = self.pin_set[pin]
					print "whatup1.6"
					print self.StepCounter
					print pin
					setting = self.Seq[self.StepCounter][pin]
					print "whatup1.7"
					if setting==1:
						print "whatup1.8"
						GPIO.output(cur_pin, True)
					else:
						print "whatup1.9"
						GPIO.output(cur_pin, False)		

				print "whatup2"

				if(num_steps > 0):
					self.StepCounter += 1
				else:
					self.StepCounter -= 1

				print "whatup3"

				if (self.StepCounter == self.stepCount):
					self.StepCounter = 0
				elif (self.StepCounter < 0):
					self.StepCounter = (self.stepCount - 1)

				print "whatup4"
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
	mtr.shift(int(sys.argv[1]))




