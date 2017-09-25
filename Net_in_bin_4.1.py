network=raw_input("Vvedite network        ")
network=network.strip(" ")
print('\n' + '-' * 30)
print("\n"*2 + network)
network=network.split(".")
mask=network[-1].split("/")
network[-1]=mask[0]
mask.remove(mask[0])
print("NETWORK")
print("\n")
print("{:15} {:15} {:15} {:15}".format(network[0] , network[1], network[2], network[3]))
print("{:15} {:15} {:15} {:15}".format(bin(int((network[0])))[2:].zfill(8) , bin(int(network[1]))[2:].zfill(8), bin(int(network[2]))[2:].zfill(8), bin(int(network[3]))[2:].zfill(8)))
mask=int(mask[0])
x=32-mask
a="1"*mask + "0"*x
b=["","","",""]
c=[0,0,0,0]
b[0],b[1],b[2],b[3]=a[0:8],a[8:16],a[16:24],a[24:32]
c=[0,0,0,0]
c[0],c[1],c[2],c[3]=int(b[0],2),int(b[1],2),int(b[2],2),int(b[3],2)
print("MASK")
print("\n")
print("%-15d %-15d %-15d %-15d" % (c[0],c[1],c[2],c[3])+"\n"+"%-15s %-15s %-15s %-15s"% (b[0],b[1],b[2],b[3])) 

