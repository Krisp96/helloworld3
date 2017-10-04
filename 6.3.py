with open("/home/python/tools/first_project/helloworld3/pyneng-examples-exercises/exercises/06_files/CAM_table.txt","r") as f:
	bad=["Mac","-",]
	for i in f:
		a=True
		for word in bad:
			if word in i:
				a=False
				break
		if a:
			print(i)

		
		 
	
			
