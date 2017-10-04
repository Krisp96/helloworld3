from sys import argv
file_name=argv[1]
file1="/home/python/tools/first_project/helloworld3/pyneng-examples-exercises/exercises/06_files/config_sw1_cleared.txt"
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
				
