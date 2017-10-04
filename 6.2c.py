from sys import argv
file_name,file1=argv[1:]
ignore = ['duplex', 'alias', 'Current configuration']
with open(file_name,"r") as f, open(file1,"w") as f1:
	for i in f:
		a=True
		for word in ignore:
			if word in i:
				a=False
				break
		if a:
			f1.write(i)
				
