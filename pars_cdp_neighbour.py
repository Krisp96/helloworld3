def cdp_neihbors(string):
	hostname="SW1"
	string=string[string.find("Device ID"):]
	string=string.split("\n")  
	string.pop(0) 
	slov={}
	for i in string:
		i=i.split()
		for x in range(5):
			i.pop(3)    
			slov.setdefault((hostname,i[1]+i[2]),(i[0],(i[-2]+i[-1])))
		return slov

	
