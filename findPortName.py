import serial 
import time
import serial.tools.list_ports

GSM_port_name = 'CP2102'
port_range = 20
rply = ''

def find_port(cnt_p,name):
  port = ''
  print('Finding port for GSM)
  while(cnt_p):
    cnt_p -= 1
    p = serial.tools.list_ports.comparts()
    n = len(p)
    for i in range(0, n):
      des = p[i][1]
      if name in des:
        port = p[i][0]
        cnt_p = 0
        print('Found Port for GSM: ' +str(port))
        break
      else:
          print('.\n')
    time.sleep(0.5)
return port

p = find_port(port_range, GSM_port_name)
ser = serial.Serial(p, 9600, timeout = 1)
