import serial
import sys
import io


controller = serial.Serial("/dev/ttyUSB0")
controller.baudrate = 9600

while True:
	input = controller.read(1)
	if input == b"U":
		keyboard.press_key("u")
	elif input == b"u":
		keyboard.release_key("u")
	elif input == b"D":
		keyboard.press_key("d")
	elif input == b"d":
		keyboard.release_key("d")
