from water_gun import water_gun
from flask import Flask

app = Flask(__name__)

pin_set_y = [14,15,18,17]
pin_set_x = [27,22,23,24]
pin_set_s = [10,9,25,8]

pi_water_controller = water_gun(pin_set_x, pin_set_y, pin_set_s)

@app.route("/")
def index():
	return "This is Dean's Water Gun"

@app.route("/right/<int:degrees>")
def right(degrees):
	pi_water_controller.move_x(degrees)
	return "Done"

@app.route("/left/<int:degrees>")
def left(degrees):
	pi_water_controller.move_x((degrees * -1))
	return "Done"

@app.route("/up/<int:degrees>")
def up(degrees):
	pi_water_controller.move_y(degrees)
	return "Done"

@app.route("/down/<int:degrees>")
def down(degrees):
	pi_water_controller.move_y((degrees * -1))
	return "Done"

@app.route("/shoot")
def shoot():
	pi_water_controller.shoot()
	return "Done"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)