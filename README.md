# Raspberry Pi Pico W 2 Rubber Ducky (Wi-Fi Payload Server)

Turn your Raspberry Pi Pico W 2 into a standalone Rubber Ducky USB HID device with a built-in Wi-Fi-controlled payload manager.

## Overview
This project allows you to use the Raspberry Pi Pico W 2 as a Rubber Ducky device, which can execute pre-defined payloads on a target machine. The device creates a Wi-Fi access point and a web interface, allowing you to upload and execute payloads remotely. The Pico W 2 acts as a USB HID device, simulating keyboard input to execute commands on the target machine.
## Disclaimer
This project is for educational and authorized security testing only. Using this on unauthorized systems is illegal and unethical.
## Requirements
- Raspberry Pi Pico 2W
- Micro USB cable
- Basic knowledge of Python and CircuitPython
## Setup Instructions
### Installation of CircuitPython
Download the UF2 from: [circuitpython.org/board/raspberry_pi_pico_w](https://circuitpython.org/board/raspberry_pi_pico2_w/).

1. Hold the BOOTSEL button on the Pico and connect it to your computer.
2. Release the button after connecting.
3. Copy the downloaded UF2 file to the Pico drive that appears.
4. The Pico will reboot and show up as CIRCUITPY.
### Installing Libraries
You can just use libraries of the repo. These are compatible with the current latest version of CircuitPython (eg 9.2.7). If you use an other version, you may need to update the libraries. You can download the libraries from the CircuitPython bundle: [circuitpython.org/libraries](https://circuitpython.org/libraries).

The project is configured to use a french macos keyboard layout. If you are using a different layout, you may need to change the keycode and the keyboard layout in the code. You can find all the libraries here: [github.com/Neradoc/Circuitpython_Keyboard_Layouts](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts).

And then, change these lines in the duck.py file:
```python
from adafruit_hid.keyboard_layout_mac_fr import KeyboardLayout
from adafruit_hid.keycode_mac_fr import Keycode
```
```python
layout = KeyboardLayout(kbd)
```

### Uploading the Code
1. Download the code from this repository.
2. Copy the `lib` folder, the `code.py`, the `duck.py`, the `index.html`, and the `payloads` folder to the CIRCUITPY drive.
3. The file `code.py` will be automatically executed when the Pico is connected to a computer.

## Features
- **Wi-Fi Access Point**: The Pico creates a Wi-Fi access point with the SSID `Pico WIFI DUCK` and the password `pico123456`. You can connect to this network with your computer or smartphone.
- **Web Interface**: You can access the web interface by connecting to the Pico's Wi-Fi network and navigating to `http://192.168.4.1` in your browser.
- **Payload Management**: The web interface allows you to upload, delete, and execute payloads. You can create payloads in the `payloads` folder on the Pico.
- **Keyboard Emulation**: The Pico emulates a USB HID device, allowing it to send keystrokes to the target machine.



