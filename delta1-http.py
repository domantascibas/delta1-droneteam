import serial
import json
import time

port_name = '/dev/ttyAMA0'
port_baudrate = 115200
domain_name = "http://vilniustransport.com"
latitude = 55.057380
longitude = 24.371699

RESPONSE_LEN = 128

SERVER_ADDR = '"http://ptsv2.com"'
SERVER_PORT = "80"
START_STR = 'AT+CIPSTART="TCP"'
SEND_CMD_STR = 'AT+CIPSEND='

server_string = START_STR +","+ SERVER_ADDR +',"'+ SERVER_PORT +'"'

def connectGsm(cmd, res):
  while(True):
    g.write(cmd)
    print cmd
    time.sleep(0.5)
    rcv = g.readline()
    print rcv
    rcv = g.readline()
    print rcv
    #while(1):
    #  if(res in rcv):
    #    time.sleep(1)
    #    return
    #  rcv = g.readline()
    #time.sleep(1)
    return

def initGsm():
  connectGsm("AT","OK")
  print "AT OK"
  connectGsm("ATE1","OK")
  print "ATE1 OK"
  connectGsm("AT+CPIN=4387","OK")
  print "AT+CPIN OK"
  connectGsm("AT+CPIN?","READY")
  print "AT+CPIN READY"

def initGprs():
  connectGsm("AT+CIPSHUT","OK")
  connectGsm("AT+CGATT=1","OK")
  print "AT+CGATT=1 OK"
  connectGsm('AT+CSTT="omnitel","omni","omni"',"OK")
  print "AT+CSTT OK"
  connectGsm("AT+CIICR","OK")
  print "AT+CIICR OK"
  time.sleep(1)
  g.write("AT+CIFSR")
  time.sleep(1)

g = serial.Serial(port_name, port_baudrate, timeout=2)
#initGsm()
#print "GSM init"
initGprs()
print "GPRS init"
connectGsm(server_string,"CONNECT")
#print "SERVER CONNECT"
time.sleep(1)

url="POST /t/delta1/post HTTP/1.1\r\n"
url+="Host: **.**.***.***\r\n"
url+="Content-Type: application/json\r\n"
url+="Content-Length:23\r\n\r\n"
url+="{'postkey':'postvalue'}"

url_len=len(url)
g.write(SEND_CMD_STR+str(url_len))
print "send to server cmd"
time.sleep(1)
g.write(url)
print "message sent"
time.sleep(1)
g.write(0x1A)
print "execute send"
time.sleep(1)

g.close()
exit()

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
