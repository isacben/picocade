import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

pins = (
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP16,
    board.GP17)
keys = [
    Keycode.UP_ARROW,
    Keycode.DOWN_ARROW,
    Keycode.LEFT_ARROW,
    Keycode.RIGHT_ARROW,
    Keycode.X,
    Keycode.Z
]

buttons = [digitalio.DigitalInOut(pin) for pin in pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

while True:
    for i, button in enumerate(buttons):
        if button.value:
            kbd.release(keys[i])
        else:
            kbd.press(keys[i])
    time.sleep(0.1)
