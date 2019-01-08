# Serial Communication
#### Serial communication from Arduino to computer (Python script)
The Arduino file `serail-temperature.ino` reads temperature data via pin 7 on arduino uno (received from DHT11) and sends it through port 9600.
The python script `serialRead.py` reads this data from port 9600 and prints this data.

#### Serial communication from computer (Python script) to arduino
The python script `serailWrite.py` sends 1 or 0 (depending on user input) to serial port 9600. The Arduino file `serial-led.ino` reads this data and turns on the led
if it receives 1 and turns it off if it receives 0.
