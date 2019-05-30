#!/usr/bin/python3
from pynput import keyboard
import time

COMBINATIONS = [
	{keyboard.Key.ctrl, keyboard.KeyCode(char='.')},
	{keyboard.Key.ctrl_r, keyboard.KeyCode(char='.')},
]

current = set()

def execute():
	dec = keyboard.KeyCode(65454)
	kc = keyboard.Controller()
	time.sleep(0.5)
	kc.press(dec)
	time.sleep(0.2)
	kc.release(dec)

def on_press(key):
	print("Pressed {}".format(key))
	if key == keyboard.Key.esc:
		return False
	if any([key in COMBO for COMBO in COMBINATIONS]):
		current.add(key)
		if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
			execute()

def on_release(key):
	if any([key in COMBO for COMBO in COMBINATIONS]):
		current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
