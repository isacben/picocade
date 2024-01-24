import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

up = digitalio.DigitalInOut(board.GP17)
up.direction = digitalio.Direction.INPUT
up.pull = digitalio.Pull.DOWN

down = digitalio.DigitalInOut(board.GP16)
down.direction = digitalio.Direction.INPUT
down.pull = digitalio.Pull.DOWN

while True:
    if up.value:
        kbd.send(Keycode.UP_ARROW)
    elif down.value:
        kbd.send(Keycode.DOWN_ARROW)

    time.sleep(0.1)
