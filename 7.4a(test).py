config=raw_input("enter path to the file:    ")
def ignore_command(command, ignore):
###This function returns only words that are not present in ignore list###
	return any(word in command for word in ignore)
def help_fun(config):
###This function returns dict , in wich keys- configuration strings without space###
###Values:Sub-commands of global config strings have 1 space- False###
###Sub-commands of global config strings have 2 space- True###
 ###Sub-commands of global config strings without subcomands- []###                                                
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
                continue
              else:
                double_space=False
                probel=True
                continue
          slovar=dict(zip(keys,values)) 
          slovar.setdefault("end",[])     
	return slovar
def slov_fun(config):
	with open(config,"r") as f:                                                                              
              ignore=["!",'duplex', 'alias', 'Current configuration']   
              temp_key=""                                               
              temp_val=[]                                               
              result_slov={}                                            
              help_slov=help_fun(config)                                
              empty_list=[]                                             
              b={}                                                      
              temp_b_key=""                                             
              temp_b_val=[]                                             
              probel=False                                              
              double_probel=False                                       
              n=0  	
	      first_time=True                                           
              for i in f:                                               
                  if ignore_command(i,ignore):                          
                           continue                                     
                  else:                                                 
                            pass                                      
                  i=i.strip("\n")                                     
                  if not i.startswith(" "):                           
                              if double_probel:                       
                                  double_probel=False                 
                                  b[temp_b_key]=temp_b_val            
                                  print(temp_key)                     
                                  result_slov[temp_key]=b             
                                  print(result_slov[temp_key])        
                                  temp_b_key=""                       
                                  temp_b_val=[]                       
                                  b={}                                
                                  first_time=True                     
                                  temp_key=i                          
                                  continue                            
                              else:                                   
                                  pass                                
                              if help_slov[i]==empty_list:            
                                  temp_key=i                          
                                  result_slov.setdefault(i,empty_list)
                                  continue                            
                              else:                             
                                  result_slov.setdefault(i)     
                                  result_slov[temp_key]=temp_val
                                  temp_key=i
                                  temp_val=[]
                  else:
                      if help_slov[temp_key]==False:
                          temp_val.append(i)
###Same as task 7.4 , adding I to the temp_val , and then to the result_slov###
                      else:
                          i=i[1:]
                          if not i.startswith(" "):
                              if first_time:
                                  temp_b_key=i
                                  first_time=False
                                  continue
                              else:
                                  pass
                              b.setdefault(i)
                              if probel:
### if there was a string with 2 spaces , and now with 1 space- add to auxilary dict b###
###temp_b_key- keys of b , temp_b_val values of b###
                                 b[temp_b_key]=temp_b_val
                                 temp_b_key=i
                                 temp_b_val=[]
                              else:
                                 b[temp_b_key]=empty_list
                                 temp_b_key=i
                              probel=False
                          else:
                              probel=True
                              temp_b_val.append(i)  
                              double_probel=True
          return(result_slov)
      

