def clear_confg(result):       
          with open(result,"r") as f:
              trunk_ports={} 
              trunk={}                
              access_ports={}          
              access={}                           
              a=""                                
              b=""                                
              for line in f:                      
                  line=line.strip(" ")                         
                  line=line.strip("\n")                        
                  if "interface Ethernet" in line:             
                      a=line[-12:].strip("\n")                 
                      trunk_ports.setdefault(a)                
                      access_ports.setdefault(a)               
                  elif "switchport trunk allowed vlan" in line:
                      b=line[30:]                      
                      trunk_ports[a]=b.split(",")      
                  elif "swichport access vlan" in line:
                      b=line[22:]      
                      access_ports[a]=b
                  else:               
                      pass               
          print("Trunk porst")           
          for i in trunk_ports:          
              if trunk_ports[i]==None:   
                  pass                     
              else:                        
                  trunk[i]=trunk_ports[i]  
          print(trunk)                         
          print("access")                      
          for i in access_ports:
			if access_ports[i]==None:
                      		pass                 
          else:                    
                      access[i]=access_ports[i]
          print(access)  
	  return trunk, access 
