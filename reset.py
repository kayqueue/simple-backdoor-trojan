import subprocess

subprocess.call(["rm", "-r", "build", "dist", "client.spec"])
subprocess.call(["pyinstaller", "--onefile", "client.py"])
