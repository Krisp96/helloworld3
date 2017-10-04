with open("/home/python/tools/first_project/helloworld3/pyneng-examples-exercises/exercises/06_files/ospf.txt","r") as f:
	for i in f:
		i=i[1:]
		i=i.strip(" ")
		i=i.split(" ")
		for n in range(5):
			i[n]=i[n].strip(",")
		
		
		print("Protocol: OSPF \n Prefix: {} \n  AD/Metric: {} \n  Next-Hop:{} \n  Last update: {} \n   Outbound Interface: {}".format(i[0],i[1],i[3],i[4],i[5]))
12
	
