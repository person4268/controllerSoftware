
import serial
import sys
import time
import keyboard

def debug_print(str):
   print(str) #comment out for no debug

controller = serial.Serial(sys.argv[1])
controller.baudrate = 9600

while True:
   input = controller.read(1)
   if input == b"U":
      keyboard.press("u")
      debug_print("[PRESS]: U")
   elif input == b"u":
      keyboard.release("u")
   elif input == b"D":
      keyboard.press("d")
      debug_print("[PRESS]: D")
   elif input == b"d":
      keyboard.release("d")
   elif input == b"Q":
      keyboard.press("q")
      debug_print("[PRESS]: Q")
   elif input == b"q":
      keyboard.release("q")
   elif input == b"W":
      keyboard.press("w")
      debug_print("[PRESS]: W")
   elif input == b"w":
      keyboard.release("w")
   elif input == b"E":
      keyboard.press("e")
      debug_print("[PRESS]: E")
   elif input == b"e":
      keyboard.release("e")
   elif input == b"R":
      keyboard.press("r")
      debug_print("[PRESS]: R")
   elif input == b"r":
      keyboard.release("r")
   elif input == b"T":
      keyboard.press("t")
      debug_print("[PRESS]: T")
   elif input == b"t":
      keyboard.release("t")
   elif input == b"K":
      keyboard.press("k")
      debug_print("[PRESS]: K")
   elif input == b"k":
      keyboard.release("k")
   elif input == b"L":
      keyboard.press("l")
      debug_print("[PRESS]: L")
   elif input == b"l":
      keyboard.release("l")
   time.sleep(0.010)
   
