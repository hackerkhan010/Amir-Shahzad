import subprocess
cmd = "apt update"
p1 = subprocess.Popen(cmd, shell=True)
p1.wait()

if p1.returncode == 0:
  print('command : success')
else
   print('command : failed')
