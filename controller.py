# As much as I hate windows, this is windows only
# Mostly because I couldn't find a way to get games to pick up the inputs

import serial
import sys
import io
import time
import os
import ctypes
import win32api

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
   _fields_ = [("wVk", ctypes.c_ushort),
               ("wScan", ctypes.c_ushort),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
   _fields_ = [("uMsg", ctypes.c_ulong),
               ("wParamL", ctypes.c_short),
               ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
   _fields_ = [("dx", ctypes.c_long),
               ("dy", ctypes.c_long),
               ("mouseData", ctypes.c_ulong),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
   _fields_ = [("ki", KeyBdInput),
               ("mi", MouseInput),
               ("hi", HardwareInput)]


class Input(ctypes.Structure):
   _fields_ = [("type", ctypes.c_ulong),
("ii", Input_I)]

def press_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008 | 0x0002

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def debug_print(str):
   print(str) #comment out for no debug

controller = serial.Serial("COM3")
controller.baudrate = 9600

KEY_U = 0x16
KEY_D = 0x20

KEY_Q = 0x10
KEY_W = 0x11
KEY_E = 0x12
KEY_R = 0x13
KEY_T = 0x14

KEY_K = 0x25
KEY_L = 0x26

while True:
   input = controller.read(1)
   if input == b"U":
      press_key(KEY_U)
      debug_print("[PRESS]: U")
   elif input == b"u":
      release_key(KEY_U)
   elif input == b"D":
      press_key(KEY_D)
      debug_print("[PRESS]: D")
   elif input == b"d":
      release_key(KEY_D)
   elif input == b"Q":
      press_key(KEY_Q)
      debug_print("[PRESS]: Q")
   elif input == b"q":
      release_key(KEY_Q)
   elif input == b"W":
      press_key(KEY_W)
      debug_print("[PRESS]: W")
   elif input == b"w":
      release_key(KEY_W)
   elif input == b"E":
      press_key(KEY_E)
      debug_print("[PRESS]: E")
   elif input == b"e":
      release_key(KEY_E)
   elif input == b"R":
      press_key(KEY_R)
      debug_print("[PRESS]: R")
   elif input == b"r":
      release_key(KEY_R)
   elif input == b"T":
      press_key(KEY_T)
      debug_print("[PRESS]: T")
   elif input == b"t":
      release_key(KEY_T)
   elif input == b"K":
      press_key(KEY_K)
      debug_print("[PRESS]: K")
   elif input == b"k":
      release_key(KEY_K)
   elif input == b"L":
      press_key(KEY_L)
      debug_print("[PRESS]: L")
   elif input == b"l":
      release_key(KEY_L)
   time.sleep(0.010)
   
