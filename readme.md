# Goal:
Create a Backdoor Trojan to be delivered to a victim Ubuntu user

- upon backdoor execution, victim's machine will connect to your machine that runs on a Kali Linux
- once connection is established, attacker will be able to run commands with options, which will be sent to the victim's machine and executed there (reverse shell)
- some assumptions:
    - your Kali machine will run netcat to wait for incoming traffic --> nc -v -l -p 5555
    - backdoor trojan is a client Python program that will connect to your Kali machine waiting for connection
    - program will be based on Python socket package

Setup
-----
- Open up a Kali VM(Server-Attacker) and a Ubuntu VM(Client-Victim)
- Note the IPv4 address of your Kali. If it is not 10.0.2.5, please open up client.py in the Ubuntu machine and change the kali_ip accordingly.
- If any changes are made to client.py, please run the following command in your ubuntu terminal to compile the client.py file to make it into an executable: $ python3 reset.py
- NOTE: I am using pyinstaller to make "client.py" into an executable, so if you need to recompile "client.py", please ensure that the pyinstaller in your system is up to date(I am using pyinstaller v5.3).

Step 1
------
set up a listener in Kali terminal (refer to step1.png)
- $ nc -lvp 5555

Step 2
------
run the program in Ubuntu
- move to the dist/ directory (refer to step2a.png), and double click on the "client" executable (refer to step2b.png)
- after double clicking on the "client" executable, move over to Kali VM to check whether a connection has been established (refer to step2c.png)

Step 3
------
can proceed to run any commands(interactive/non-interactive)
- please refer to step3.png for examples of the commands 

Step 4
------
to exit from the reverse shell, type the following in the terminal
- $ exit
