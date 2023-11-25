# Atari 2600+ dumper

You can add a cart dumping feature to the Atari 2600+ by connecting a FTDI cable (USB to serial cable) to the Ataro2600+ I/O board serial header (see images).
To hook up this cable, connect GND and Tx of the I/O boards serial header to the FTDI cable GND and Rx pins respectively (see images).

The The serial header on the Atari 2600+ I/O board has no pin header soldered to the board so you will have t solder your some jumper wires or a pin header to the board.
You can solder male to male jumper wires directly to the pads or cut off one of the ends and solder the wire to the pad. Whichever is easier to do.

![I/O board Serial header](https://github.com/MrBlinky/Atari2600plus-dumper/blob/main/images/atari-2600-plus-serial-header.jpg)
## Running the dumper tool

The dumper tool is a python script to run it, open a commandline window and when no Python installed on your computer (or you don't know) enter:

```
dump2600p comport
```

or when Python is installed with pySerial on your computer you can run the script directly by entering:

```
dump2600p.py comport
```

comport is the name of the serial port of the FTDI cable. To find out which serial port is used by the FTDI cable go to device manager and check under ports which com port is added when you insert the cable into the computer.

After entering one of the above commands the dumper will run continiously and wait for the 2600+ to detect a cart.
When a cart is succesfully detected it is dumped and saved to the romdump directory located in the same folder as the script.
Once a cart is dumped you can pull the cart and insert another cart to dump (hot swap) or power off before inserting another cart and switching power back on.
To exit the dumper press CTRL+C or close the window.

Notes:
- The script should also work on Linux and OSX. Python3 with PySerial must be installed and the script should be run from the terminal.
- Only carts that are supported by the Atari2600+ can be dumped .

## FTDI cable

The FTDI cable is a USB to Serial converter which allows for a simple way to connect serial (UART) devices to USB.
It is called a FTDI cable because it uses an FTDI chip. There are many similar (clone) cables and also modules available
that convert serial to USB.

Whichever cable or module you have or will use make sure the drivers are installed and the device is visible in device manager.
Also double check the pinout of your cable or module as clone cables and modules do not always use the same pinout.

Note:
If you want to use a FTDI cable with a stereo audio jack so you can connect it to an audio jack connector built into the 2600+ shell, I recommend to get a 2.5mm one and not a 3.5mm one because you don't want someone accidentally insert an original Atari power supply. Feeding 9V into the I/O board will most likely damage your 2600+.

![FTDI cable](https://github.com/MrBlinky/Atari2600plus-dumper/blob/main/images/atari-2600-plus-ftdi-cable.jpg)
