network=raw_input("Vvedite chislo v formate 10.10.10.10    ")
a=True
n=network.count(".")
while a:
	if n<3:
		print('Incorrect IPv4 address 1')
		network=raw_input("Vvedite chislo v formate 10.10.10.10    ")
		continue
	else:	
		network=network.split(".")
		for i in network:
			if not i.isdigit():
				print('Incorrect IPv4 address 2')
				network=raw_input("Vvedite chislo v formate 10.10.10.10    ")
				break
			else:
				pass
		continue
		network[0],network[1],network[2],network[3]=int(network[0]),int(network[1]),int(network[2]),int(network[3])
		for i in network:
			if (i<0) or (i>255):
				print('Incorrect IPv4 address 3')
				network=raw_input("Vvedite chislo v formate 10.10.10.10    ")
				break
			else:
				a=False
	
if network[0]<=127:
	network[0],network[1],network[2],network[3]=str(network[0]),str(network[1]),str(network[2]),str(network[3])

	print("{}".format(".".join(network)) +"   " + "Class A" "Unicast")

elif (network[0]>127) and (network[0]<=191):
	network[0],network[1],network[2],network[3]=str(network[0]),str(network[1]),str(network[2]),str(network[3])

	print("{}".format(".".join(network)) +"   " + "Class B" "Unicast")

elif (network[0]>191) and (network[0]<=223):
	network[0],network[1],network[2],network[3]=str(network[0]),str(network[1]),str(network[2]),str(network[3])

	print("{}".format(".".join(network)) +"   " + "Class C" "Unicast")

elif (network[0]>223) and (network[0]<=239):
	network[0],network[1],network[2],network[3]=str(network[0]),str(network[1]),str(network[2]),str(network[3])
	print("{}".format(".".join(network)) +"   " + "Class D" "Multicast")
elif (network[0],network[1],network[2],network[3]==255):
	network[0],network[1],network[2],network[3]=str(network[0]),str(network[1]),str(network[2]),str(network[3])
	print("{}".format(".".join(network)) +"   " + "Broadcast")
elif (network[0],network[1],network[2],network[3]==0):
	nettwork[0],network[1],network[2],network[3]=str(network[0]),str(network[1]),str(network[2]),str(network[3])
	print("{}".format(".".join(network)) +"   " + "Unassinged")
else:
	print("{}".format(".".join(network)) +"   " + "unused")
