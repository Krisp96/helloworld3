def cdp_neihbors(string):
	print(type(string))
	hostname=string[:string.find(">")]
	string=string[string.find("Device ID"):]
	string=string.split("\n")  
	string.pop(0)
	slov={} 
	not_pop=["Eth","FE","GE"]
	a=0
	for line in string:
		if line=="":
			a=a+1
			#print(string)
			continue
		else:
			continue
	#print(a)
	for i in range(a):
		string.remove("")
	print(string)
	for i in string:
		#print(string)
		i=i.split()
		for x in range(5):
                	if i[3] in not_pop:
                		break
                 	else:
                     		i.pop(3)    
		slov.setdefault((hostname,i[1]+i[2]),(i[0],(i[-2]+i[-1])))
	return slov

