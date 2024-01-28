# picocade

Arcade controller for the pico-8 fantasy console.

## Bill Of Materials

| Item | Count | Cost | Vendor |
| ---- | ----- | ---- | ------ |
| Stick | 1 | $28.00 | Link |
| Arcade buttons | 4 | $22.00 | Link |
| Led | 1 | $0.20 | Link |
| Resistor | 1 | $0.20 | Link |
| Raspberry Pi Pico | 1 | $6 | Link |
| Enclosure | 1 | $25.00 | Link |

## Schematics

Notes:

- [Download the Raspberry Pi Pico KiCad symbol](https://forums.raspberrypi.com/viewtopic.php?t=336825)
- [Import KiCad symbols to the global library](https://forum.kicad.info/t/copying-new-symbols-from-one-project-to-another/36338/4)

![picocade schematics](https://github.com/isacben/picocade/blob/main/img/schematic.png)

## Firmware

Download CircuitPython for the Raspberry Pi Pico W here:

https://circuitpython.org/board/raspberry_pi_pico_w/

Download the CircuitPython libraries bundle from here:

https://circuitpython.org/libraries

Copy the [firmware/code.py](https://github.com/isacben/picocade/blob/main/firmware/code.py) file to the Rasberry Pi board.
