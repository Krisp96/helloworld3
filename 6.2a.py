from sys import argv
file_name=argv[1]
ignore = ['duplex', 'alias', 'Current configuration']
with open(file_name,"r") as f:
	for i in f:
		a=True
		for word in ignore:
			if word in i:
				a=False
				break
		if a:
			print(i),
				
