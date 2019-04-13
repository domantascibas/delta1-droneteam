import serial

ser = serial.Serial('/dev/ttyAMA0', 115200)
ser.close()

ser.open()
ser.write("AT")

serial_line = ser.readline()
print serial_line
while(serial_line != ''):
  serial_line = ser.readline()
  print serial_line

ser.close()