network1=raw_input("Vvedite chislo v formate 10.10.10.10    ")
a=True
network=network1.split(".")
x=network[0].isdigit()
for i in range(3):
	x=x and (network[i].isdigit() and network[i+1].isdigit())
y=True
network[0],network[1],network[2],network[3]=int(network[0]),int(network[1]),int(network[2]),int(network[3])
for i in range(3):
	if y==True:
		if  not (network[i]>=0 and network[i]<=255):
			y=False
			break
	else:
			y=True 
while a:
	if  network1.count(".")<3:
		print("mistake 1 ")
	elif x==False:
		print("mistake 2")
	elif y==False:
		print("mistake 3")
	else:
		a=False
		continue
	
network[0],network[1],network[2],network[3]=int(network[0]),int(network[1]),int(network[2]),int(network[3])
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
