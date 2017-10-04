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
	i=0
	maxim=""
	temp=""
	for i in range (x):
		maxim=n[0][0:3]
		for i in range (x):
			if int(n[i][0:3])>int(n[i+1][0:3]):
				temp=n[i+1]
				maxim=n[i]
				n[i+1]=maxim
				n[i]=temp
			else:
				continue
	for i in n:
		print(i)	
