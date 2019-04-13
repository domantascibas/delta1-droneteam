import serial
import json

port_name = '/dev/ttyAMA0'
port_baudrate = 115200
domain_name = "http://vilniustransport.com"
latitude = 55.057380
longitude = 24.371699

RESPONSE_LEN = 128

g = serial.Serial(port_name, port_baudrate, timeout=2)
g.write('AT+CGATT=1')

g.write('AT+HTTPINIT')
print g.read(RESPONSE_LEN)

g.write('AT+HTTPPARA="CID",1')
print g.read(RESPONSE_LEN)

g.write('AT+HTTPPARA="URL","http://vilniustransport.com"')
print g.read(RESPONSE_LEN)

g.write('AT+HTTPPARA="CONTENT","application/json"')
print g.read(RESPONSE_LEN)

g.write('AT+HTTPDATA=150,5000'+'\r\n')
print g.read(RESPONSE_LEN)

data = {"beacon_id": 1, "latitude": latitude, "longitude": longitude}

g.write(json.dumps(data))
print g.read(RESPONSE_LEN)

g.write('AT+HTTPACTION=1' + '\r\n')  
print g.read(RESPONSE_LEN)
