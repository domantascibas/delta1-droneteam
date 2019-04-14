import serial
import json
import time

port_name = '/dev/ttyAMA0'
port_baudrate = 115200
domain_name = "http://vilniustransport.com"
latitude = 55.057380
longitude = 24.371699

RESPONSE_LEN = 128

def connectGsm(cmd, res):
  while(True):
    g.write(cmd)
    time.sleep(0.5)
    rcv = g.readline()
    while(rcv != ''):
      if(res in rcv):
        time.sleep(1)
        return
    time.sleep(1)

def initGsm():
  connectGsm("AT","OK")
  connectGsm("ATE1","OK")
  connectGsm("AT+CPIN=4387","OK")
  connectGsm("AT+CPIN?","READY")

def initGprs():
  connectGsm("AT+CIPSHUT","OK")
  connectGsm("AT+CGATT=1","OK")
  connectGsm('AT+CSTT="omnitel","omni","omni"',"OK")
  connectGsm("AT+CIICR","OK")
  time.sleep(1)
  g.write("AT+CIFSR")
  time.sleep(1)

g = serial.Serial(port_name, port_baudrate, timeout=2)
initGsm()
initGprs()

g.close()

# g.write('AT+CGATT=1')
# print g.read(RESPONSE_LEN)
# print g.read(RESPONSE_LEN)

# g.write('AT+CIPMUX=0')
# print g.read(RESPONSE_LEN)
# print g.read(RESPONSE_LEN)

# g.write('AT+CSTT="omnitel","omni","omni"')
# print g.read(RESPONSE_LEN)
# print g.read(RESPONSE_LEN)

# g.write('AT+CIICR')
# print g.read(RESPONSE_LEN)
# print g.read(RESPONSE_LEN)

# g.write('AT+CIFSR')
# print g.read(RESPONSE_LEN)
# print g.read(RESPONSE_LEN)

# g.write('AT+CIPSHUT')
# print g.read(RESPONSE_LEN)
# print g.read(RESPONSE_LEN)

# g.write('AT+HTTPINIT')
# print g.read(RESPONSE_LEN)
# print g.read(RESPONSE_LEN)

# g.write('AT+HTTPPARA="CID",1')
# print g.read(RESPONSE_LEN)
# print g.read(RESPONSE_LEN)

# g.write('AT+HTTPPARA="URL","http://ptsv2.com/t/delta1/post"')
# # g.write('AT+HTTPPARA="URL","78.61.220.12"')
# print g.read(RESPONSE_LEN)

# g.write('AT+HTTPPARA="CONTENT","multipart/form-data; boundary=----WebKitFormBoundaryvZ0ZHShNAcBABWFy"')
# print g.read(RESPONSE_LEN)

# g.write('AT+HTTPDATA=192,10000')
# print g.read(RESPONSE_LEN)

# g.write('AT+HTTPDATA=150,5000'+'\r\n')
# print g.read(RESPONSE_LEN)

# data = {"beacon_id": 1, "latitude": latitude, "longitude": longitude}

# g.write(json.dumps(data))
# print g.read(RESPONSE_LEN)

# g.write('AT+HTTPACTION=1' + '\r\n')  
# print g.read(RESPONSE_LEN)
