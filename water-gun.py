
import motor

"Set this equal to the number of steps in a 360 degree rotation of yoru stepper motor"
MAX_STEPS = 508

class water_gun:
	shots_remaining = 0
	current_x = (MAX_STEPS / 2)
	current_y = (MAX_STEPS / 4)

	motor_x
	motor_y
	motor_shoot
	
	def move_x(self, steps):
		print "Removing unecessary full rotations"
		steps = steps % MAX_STEPS

		if(sum(self.current_x, steps) > MAX_STEPS):
			print "Moving in counterclockwise direction to prevent tangled wires"
			steps = steps - MAX_STEPS
			print "spinning {0} steps".format(steps)
			self.motor_x.shift(steps)
			self.current_x += steps
		if(sum(self.current_x, steps) < 0):
			print "Moving in clockwise direction to prevent tangled wires"
			degrees = MAX_STEPS - steps
			print "spinning {0} degrees".format(steps)
			self.motor_x.shift(steps)
			self.current_x += steps
		else:
			print "spinning {0} steps".format(steps)
			self.motor_x.shift(steps)
			self.current_x += steps

	def move_y(self, steps):
		print "Removing unecessary full rotations"
		degrees = steps % MAX_STEPS

		"Make sure the water-gun is not flipped"
		if (sum(self.current_y, steps) > (MAX_STEPS / 2)):
			self.move_x((MAX_STEPS / 2))
			total_steps = ((MAX_STEPS / 2) - self.current_y) * 2
			self.move_y(total_steps - steps)
		if (sum(self.current_y, steps) < 0):
			self.move_x((MAX_STEPS / 2))
			total_steps = (self.current_y) * 2
			self.move_y(total_steps - steps)
		else:
			self.motor_y.shift(steps)
			self.current_y += steps

	def shoot(self):
		self.motor_shoot.shoot()
		self.shots_remaining -= 1

	def return_to_center(self):
		distance_to_x = (MAX_STEPS / 2) - self.current_x
		distance_to_y = (MAX_STEPS / 4) - self.current_y

		self.move_x(distance_to_x)
		self.move_y(distance_to_y)

	def __init__(self, motor_x_gpio, motor_y_gpio, motor_shoot_gpio):
		self.motor_x = direction_motor(motor_x_gpio)
		self.motor_y = direction_motor(motor_y_gpio)
		self.motor_shoot = trigger_motor(motor_shoot_gpio)
