from sys import argv
file_name=argv[1]
with open(file_name,"r") as f:
	bad_words=["!"]
	for i in f:
		a=True
		for word in i:
			if word=="!":
				a=False
				break
		if a:
			print(i),
				
