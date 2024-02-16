# Install CircuitPython

## CircuitPython

The picocade is powered by a Raspberry Pi Pico running CircuitPython. CircuitPython is a version of Python for microcontrollers.

Download CircuitPython for the Raspberry Pi Pico or the Raspberry Pi Pico  W. I am using the second one:

https://circuitpython.org/board/raspberry_pi_pico_w/

[This guide from Adafruit](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython) explains how to install CircuitPython on the Raspberry Pi Pico.

## CircuitPython HID

The picocade also uses the [Adafruit CircuitPython HID library](https://github.com/adafruit/Adafruit_CircuitPython_HID) to make it behave as a keyboard.

Download the CircuitPython libraries bundle from here:

https://circuitpython.org/libraries

Then unzip the downloaded zip file and copy the `adafruit_hid` folder to the `lib` folder on your `CIRCUITPY` drive.
