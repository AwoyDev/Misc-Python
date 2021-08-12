from time import sleep
import pynput

ke = pynput.keyboard.Controller()
sleep(1)

while True:
    ke.type("Hello world")
    ke.press(pynput.keyboard.Key.enter)
    sleep(0.5)