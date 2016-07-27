import time
import RPi.GPIO as GPIO

class motor:
	pin_set = []
	StepCounter = 0
	WaitTime = 0.0015

	stepCount = 4
	Seq = []
	Seq = [3,2,1,0]
	Seq[0] = [0,0,1,1]
	Seq[1] = [1,0,0,1]
	Seq[2] = [1,1,0,0]
	Seq[3] = [0,1,1,0]

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
		try:
			for step in range(0, abs(num_steps)):
				for pin in range(0,4):
					cur_pin = self.pin_set[pin]
					setting = self.seq[self.StepCounter][pin]

					if setting==1:
						GPIO.output(cur_pin, True)
					else:
						GPIO.output(cur_pin, False)

				if(num_steps > 0):
					self.StepCounter += 1
				else:
					self.StepCounter -= 1

				if (self.StepCounter == self.stepCount):
					self.StepCounter = 0
				elif (self.StepCounter < 0):
					self.StepCounter = self.stepCount

				time.sleep(self.WaitTime)
		except:
			for pin in self.pin_set:
				GPIO.setup(pin,GPIO.OUT)
				GPIO.output(pin, False)
		finally:
			for pin in self.pin_set:
				GPIO.setup(pin,GPIO.OUT)
				GPIO.output(pin, False)




