# picocade

An arcade controller for the pico-8 fantasy console.

NOTE: this is Work In Progress! I am still designing the product; the following image is the idea of what I want to build:

![PICO-8 arcade controller concept](https://github.com/isacben/picocade/blob/main/img/concept.png | width=400)

## Bill Of Materials

| Item | Count | Cost | Vendor |
| ---- | ----- | ---- | ------ |
| Joystick | 1 | $28.00 | Link |
| Arcade buttons | 4 | $22.00 | Link |
| Led | 1 | $0.20 | Link |
| Resistor | 1 | $0.20 | Link |
| Raspberry Pi Pico | 1 | $6 | Link |
| Enclosure | 1 | $25.00 | Link |
| Solderable breadboard | 1 | $1.50 | Link |
| USB adapter | 1 | $8.00 | Link |
| Short USB cable | 1 | $6.99 | Link |
| Longer USB cable | 1 | $12.00 | Link | 

## Schematics

Notes:

- [Download the Raspberry Pi Pico KiCad symbol](https://forums.raspberrypi.com/viewtopic.php?t=336825)
- [Import KiCad symbols to the global library](https://forum.kicad.info/t/copying-new-symbols-from-one-project-to-another/36338/4)

![picocade schematics](https://github.com/isacben/picocade/blob/main/img/schematic.png | width=400)

## Firmware

Download CircuitPython for the Raspberry Pi Pico W here:

https://circuitpython.org/board/raspberry_pi_pico_w/

Download the CircuitPython libraries bundle from here:

https://circuitpython.org/libraries

Copy the [firmware/code.py](https://github.com/isacben/picocade/blob/main/firmware/code.py) file to the Rasberry Pi board.
