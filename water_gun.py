
from motor import motor
import RPi.GPIO as GPIO

"Set this equal to the number of steps in a 360 degree rotation of yoru stepper motor"
MAX_STEPS = 360

class water_gun:
	shots_remaining = 100
	current_x = (MAX_STEPS / 2)
	current_y = (MAX_STEPS / 4)
	
	def move_x(self, steps):
		#Removing unecessary full rotations
		steps = steps % MAX_STEPS
		self.motor_x.shift(steps)

	def move_y(self, steps):
		#Removing unecessary full rotations
		degrees = steps % MAX_STEPS
		self.motor_y.shift(steps)

	def shoot(self):
		self.motor_shoot.shoot()
		self.shots_remaining -= 1

	def return_to_center(self):
		distance_to_x = (MAX_STEPS / 2) - self.current_x
		distance_to_y = (MAX_STEPS / 4) - self.current_y

		self.move_x(distance_to_x)
		self.move_y(distance_to_y)

	def __init__(self, motor_x_gpio, motor_y_gpio, motor_shoot_gpio):
		self.motor_x = motor(motor_x_gpio)
		self.motor_y = motor(motor_y_gpio)
		self.motor_shoot = motor(motor_shoot_gpio)

	def __del__(self):
		self.return_to_center()

if __name__ == "__main__":
	GPIO.setwarnings(False)
	pin_set_x = [14,15,18,17]
	pin_set_y = [27,22,23,24]
	pin_set_s = [10,9,25,8]

	pi_water_controller = water_gun(pin_set_x, pin_set_y, pin_set_s)

	pi_water_controller.move_x(100)
	pi_water_controller.move_x(280)
	pi_water_controller.move_x(360)
	pi_water_controller.move_x(180)
	pi_water_controller.move_x(75)

	pi_water_controller.move_y(90)
	pi_water_controller.move_y(180)
	pi_water_controller.move_y(45)
	pi_water_controller.move_y(32)


