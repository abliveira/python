"""
# https://pyserial.readthedocs.io/en/latest/shortintro.html
# https://www.engineersgarage.com/articles-raspberry-pi-serial-communication-uart-protocol-ttl-port-usb-serial-boards/

Instalação
Deve-se instalar o pyserial antes de rodar o script usando o seguinte comando:

pip install pyserial

"""


import time
import serial
ser = serial.Serial('COM5', 115200, timeout=0,parity=serial.PARITY_NONE)
counter=0
while 1:
    ser.write(b'Write counter: %d \n'%(counter))
    print("Printed")
    time.sleep(1)
    counter += 1


while 1:
    rx_data = ser.read()
    print(rx_data)
	
import serial
ser = serial.Serial('COM5', 115200, timeout=0,parity=serial.PARITY_NONE)
x=0
while x < 500:
	x=x+1
	rx_data = ser.read()
	print(rx_data)
	
while x < 500:
	rx_data = ser.read()
	print(rx_data)
	
	
data = ser.readline()
print(data)


counter = 500
ser.write(b'Write counter: %d \n'%(counter))
ser.write(b'Write counter: %d \n'%(counter))



# o que funcionou ---------------------------------

import serial
import time
ser = serial.Serial('COM5', 9600, timeout=0,parity=serial.PARITY_NONE)

counter = 0
while counter < 400:
 counter = counter + 1
 print(counter)
 #ser.write(b'Write counter: %d \n'%(counter))
 ser.write(b'%d'%(counter))
 #ser.write(b'%d \n'%(counter))
 time.sleep(0.2)