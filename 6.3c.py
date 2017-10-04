with open("/home/python/tools/first_project/helloworld3/pyneng-examples-exercises/exercises/06_files/CAM_table.txt","r") as f:
	bad=["Mac","-",]
	n=[]
	for i in f:
		a=True
		for word in bad:
			if word in i:
				a=False
				break
		if a:
			n.append(i)
	for i in n:
		x=n.index(i)
		n[x]=n[x].strip("\n")
	n.remove("")
	for i in n:
		x=n.index(i)
		n[x]=n[x].strip(" ")
	y=True
	z=False
	while y:
		vlan=raw_input("Vvedite #vlan   ")
		if not vlan.isdigit():
			print("Vvedite num vlan again  ")
			continue
		word=vlan
		for i in n:
				if  word in i:
					z=True
					print(i)
				else:
					continue
		if not z:
			print("Takogo vlana net")
			continue
		y=False
