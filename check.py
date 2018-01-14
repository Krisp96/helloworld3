#!/usr/bin/env python3
from check_ip_addresses import check_ip_addresses 
address_list=['8.8.8.8', '8.8.4.4', '192.168.1.1', '32.34.34.2']
alive_ip=[]
dead_ip=[]
flag=False
for i in address_list:
	print(i," cheking address...")
	line=check_ip_addresses(i)[check_ip_addresses(i).find("ping statistics ---"):].split("\n")
	line=line[1].split(",")
	sent,resv=line[0].strip(" ")[0],line[1].strip(" ")[0]		 
	if int(sent)==int(resv):
		flag=True
		print(i,"   ALIVE")
	else:
		flag=False
		print(i,"    DEAD")
		      
	if flag:      
             alive_ip.append(i)
	else:      
             dead_ip.append(i)                                        
print(alive_ip,dead_ip)

