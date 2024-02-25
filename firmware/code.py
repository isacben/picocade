import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

SPLORE = "splore\n"

pins = (
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21
    )

keys = [
    Keycode.UP_ARROW,
    Keycode.DOWN_ARROW,
    Keycode.RIGHT_ARROW,
    Keycode.LEFT_ARROW,
    Keycode.X,
    Keycode.Z,
    SPLORE,
    Keycode.ESCAPE
]

led = digitalio.DigitalInOut(board.GP17)
led.direction = digitalio.Direction.OUTPUT

buttons = [digitalio.DigitalInOut(pin) for pin in pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

while True:
    led.value = True

    for i, button in enumerate(buttons):
        if button.value:
            if keys[i] != SPLORE:
                kbd.release(keys[i])
        else:
            if keys[i] == SPLORE:
                layout.write(SPLORE)
                kbd.release_all()
            else:
                kbd.press(keys[i])
    time.sleep(0.1)
