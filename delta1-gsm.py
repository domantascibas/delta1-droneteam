import serial

port_name = '/dev/ttyAMA0'
port_baudrate = 115200

class GsmModule():

  def __init__(self, port, baud):
    self.port = port
    self.baud = baud
    self.serial = serial.Serial(self.port, self.baud)
    self.serial.close()
    print "GSM object created", port_name, port_baudrate

  def openSerial(self):
    self.serial.open()
    print "Serial open"

  def closeSerial(self):
    self.serial.close()
    print "Serial closed"

  def sendCommand(self, cmd):
    self.openSerial()
    self.serial.write(cmd + '\r')
    print "Cmd sent", cmd

    rcv = self.serial.read()
    while(rcv != ''):
      rcv = self.serial.read()

    self.closeSerial()
    print rcv

Gsm = GsmModule(port_name, port_baudrate)
Gsm.sendCommand("AT")

# ser = serial.Serial('/dev/ttyAMA0', 115200)
# ser.close()

# ser.open()
# ser.write("AT")

# serial_line = ser.readline()
# print serial_line
# while(serial_line != ''):
#   serial_line = ser.readline()
#   print serial_line

# ser.close()

# def send_AT_cmd(cmd):
#   port = serial.Serial(port_name, port_baudrate)
#   port.write(cmd + '\r')
  
#   rcv = ''

#   while(port.read() != ''):
#     rcv += port.read()

#   port.close()
#   print rcv