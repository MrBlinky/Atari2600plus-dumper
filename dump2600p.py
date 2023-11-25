################################################################################
#  Atari 2600+ Dumper v1.00                            by Mr. Blinky Nov 2023  #
################################################################################

# requires Python 3 & pyserial to be installed

import sys
import platform
import serial
import os.path
import time
import hashlib

romdir = os.path.split(sys.argv[0])[0] + os.sep + 'romdumps' + os.sep

print('Atari 2600+ Dumper v1.00 by Mr. Blinky Nov 2023\n')
print('Using python version {}\n'.format(platform.python_version()))
if  (len(sys.argv) < 2):
    print('USAGE: {} comport'.format(os.path.basename(sys.argv[0])))
    sys.exit()

try:
    port = sys.argv[1]
    com = serial.Serial()
    com.port = port
    com.baudrate = 115200
    com.timeout = 1
    com.setDTR(False)
    com.open()
except serial.SerialException:
    print('Error! Can\'t open serial port ' + port)
    sys.exit()

def read(n):
  bytes = bytearray()
  while len (bytes) != n:
    bytes += com.read(1)
  return bytes

print('Waiting for dumper to respond...(Remove and/or insert cart)')  
while True:
  cmd = read(1)
  if cmd[0] == 0xEA:
    print('No cart detected')
  #expect rom dump command
  elif cmd[0] == 0xAA:
    cmd += read(4)
    if len(cmd) == 5 and cmd[1] == 0x55 and cmd [2] == 0x26:
      romsize = ((cmd[4] >> 4) * 10 + (cmd[4] & 0x0f)) * 1024
      print('Reading {} bytes from cart'.format(romsize))
      romdump = read(romsize)
      romhash = hashlib.md5(romdump).hexdigest()
      #expect cart type command
      cmd = read(5)
      if cmd[0] == 0x55 and cmd[1] == 0xAA:
        romtype = cmd[3] * 256 + cmd[4]
        print('Detected cart type 0x{:04X}'.format(romtype))
        #save romdump
        filename = romdir + "romdump-{}-md5-{}-type-{:04x}.bin".format(time.strftime("%Y%m%d-%H%M%S", time.localtime()), romhash, romtype)
        
        print('Saving romdump to ' + filename)
        if not os.path.exists(romdir):
          os.makedirs(romdir)
        with open(filename, "wb") as binfile:
          binfile.write(romdump)
          binfile.close()
        print('Remove cart and insert next cart to dump\n')
