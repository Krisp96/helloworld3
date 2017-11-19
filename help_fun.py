config=raw_input("enter path to the file:    ")
def ignore_commrand(command, ignore):
	return any(word in command for word in ignore)
def help_fun(config):                                                 
        with open (config,"r") as f:                                        
          temp=""                                                           
          empty_list=[]                                                     
          first_time=True                                                   
          keys=[]                                                           
          values=[]                                                         
          probel=False                                                      
          double_space=False                                                
          ignore=["!",'duplex', 'alias', 'Current configuration']           
          for i in f:                                                       
            i=i.strip("\n")                                                 
            if ignore_command(i,ignore):                                    
                            continue                                        
            else:                                                           
                            pass                                            
            if first_time:               
              temp=i                     
              first_time=False           
              probel=False               
              continue                   
            if not i.startswith(" "):    
              if double_space:           
                values.append(True)      
                keys.append(temp)  
	        temp=i
                probel=False
                double_space=False
              elif probel:
                values.append(False)
                keys.append(temp)
                temp=i
                probel=False
                double_space=False
              else:
                values.append(empty_list)
                keys.append(temp)
                temp=i
                probel=False
                double_space=False
            else:
              i=i[1:]
              if i.startswith(" "):
                double_space=True
                probel=False
                print(i)
                continue
              else:
                double_space=False
                probel=True
                continue
          slovar=dict(zip(keys,values))
	print("tnx")      
	return slovar
      

