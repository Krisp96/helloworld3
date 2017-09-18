network=raw_input("Vvedite network        ")
print('\n' + '-' * 30)
print("\n"*2 + network)
network=network.split(".")
mask=network[-1].split("/")
network[-1]=mask[0]
mask.remove(mask[0])
for i in range (4):
	network[i]=int(network[i])
mask[0]=int(mask[0])
i=0
j=0
for i in range (5):
         if i==0:
             print("NETWORK:")
         if i==4:
             print("\n")
             for j in range (4):
                print("%-15s" % bin(network[j])[2:].zfill(8) ),
         else:
                print("%-15d" % network[i]  ),
  

