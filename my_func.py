def ignore_command(command, ignore):
	return any(word in command for word in ignore)

def generate_acces(access):
	access_template = ['interface {}','switchport mode access',
 	'switchport access vlan {}',
  'switchport nonegotiate',
  'spanning-tree portfast',
 'spanning-tree bpduguard enable']
	result=[]
	for i in access:
          for y in access_template:
              if y.startswith("interface"):
                 result.append(y.format(i))
              elif y.endswith("vlan {}"):
                  result.append(y.format(access[i]))
              else:
                  result.append(y)
	print(result)
	return result
def trunk_gen(trunk):
	result=[]
	trunk_template = ['interfase {}','switchport trunk encapsulation dot1q',
     'switchport mode trunk',
     'switchport trunk native vlan 999',
     'switchport trunk allowed vlan   {}']
  
	for i in trunk:
             for y in trunk_template:
                 if y.startswith("interfase"):
                     result.append(y.format(i).strip("\n"))
                 elif y.startswith("switchport trunk allowed"):
                     result.append(y.format(",".join([str(a) for a in trunk[i]])))
                 else:
                     result.append(y.strip("\n"))
	return result
def get_int_vlan_map(config):                                                                            
               with open(config,"r") as f:                                                               
                   trunk_ports={}                                                                        
                   trunk={}                                                                              
                   access_ports={}                                                                       
                   access={}                                                                             
                   a=""                                                                                  
                   b=""                                                                                  
                   ignore=['service','version','duplex', 'alias', 'Current configuration','!']           
	           for line in f:                                                                        
                   	line=line.strip(" ")                             
                   	line=line.strip("\n")                            
                   	if ignore_command(line,ignore):                  
                       		continue                                     
                  	else:                                            
                   		pass                                                                           
                  	if "interface FastEthernet" in line:             
                       	 	a=line[-15:].strip("\n")                 
                        	trunk_ports.setdefault(a)                    
                        	access_ports.setdefault(a)               
                  	elif "switchport trunk allowed vlan" in line:
                   		b=line[30:]                              
                       	 	trunk_ports[a]=b.split(",")              
                  	elif "switchport access vlan" in line:                       
                       	 	b=line[22:]                       
                        	access_ports[a]=b
                   	else:               
                        	pass               
                          
               for i in trunk_ports:          
                   if trunk_ports[i]==None:   
                       pass                     
                   else:                        
                       trunk[i]=trunk_ports[i]  
               for i in access_ports:
                   if access_ports[i]==None:
                           pass                 
                   else:                    
                           access[i]=access_ports[i]
               return trunk, access
