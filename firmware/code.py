import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

x = digitalio.DigitalInOut(board.GP16)
x.direction = digitalio.Direction.INPUT
x.pull = digitalio.Pull.DOWN

z = digitalio.DigitalInOut(board.GP17)
z.direction = digitalio.Direction.INPUT
z.pull = digitalio.Pull.DOWN

up = digitalio.DigitalInOut(board.GP1)
up.direction = digitalio.Direction.INPUT
up.pull = digitalio.Pull.DOWN

down = digitalio.DigitalInOut(board.GP2)
down.direction = digitalio.Direction.INPUT
down.pull = digitalio.Pull.DOWN

left = digitalio.DigitalInOut(board.GP3)
left.direction = digitalio.Direction.INPUT
left.pull = digitalio.Pull.DOWN

right = digitalio.DigitalInOut(board.GP4)
right.direction = digitalio.Direction.INPUT
right.pull = digitalio.Pull.DOWN

while True:
    if up.value:
        kbd.send(Keycode.UP_ARROW)
    elif down.value:
        kbd.send(Keycode.DOWN_ARROW)
    elif left.value:
        kbd.send(Keycode.LEFT_ARROW)
    elif right.value:
        kbd.send(Keycode.RIGHT_ARROW)
    elif x.value:
        kbd.send(Keycode.X)
    elif z.value:
        kbd.send(Keycode.Z)

    time.sleep(0.1)
