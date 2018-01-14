def get_int_vlan_map(result):                                                                            
               with open(result,"r") as f:                                                               
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
     

