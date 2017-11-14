 def del_exl(config):                                           
    ...:     with open(config,"r") as f:                                
    ...:         ignore=["!",'duplex', 'alias', 'Current configuration']
    ...:         keys=[]                                              
    ...:         values=[]                                            
    ...:         temp_values=[]                                       
    ...:         cash_keys=""                                         
    ...:         empty_list=[]                                        
    ...:         bad_word=False                                       
    ...:         probel=False                                         
    ...:         first_time=True                                      
    ...:         for i in f:                                          
    ...:             i=i.strip("\n")                                  
    ...:             for line in ignore:                              
    ...:                 if line in i:                                
    ...:                     bad_word=True                            
    ...:                     break                                    
    ...:                 else:                                        
    ...:                     bad_word=False                           
    ...:                     continue                                 
    ...:             if bad_word:                                     
    ...:                 continue                                     
    ...:             else:                                            
    ...:                 pass                                         
    ...:             if not bad_word and not i.startswith(" "):
                 	 print("i ---  ",i,"\n" + "-"*30)               
    ...:                 print(temp_values,"temp_values "+"\n"+"-"*30)  
    ...:                 if first_time:                                 
    ...:                     cash_keys=i                              
    ...:                     first_time=False                         
    ...:                     continue                                 
    ...:                 else:                                        
    ...:                     pass                                     
    ...:                 if not  probel:                              
    ...:                     keys.append(cash_keys)                   
    ...:                     cash_keys=i                              
    ...:                     values.append(empty_list)                
    ...:                     probel=False                             
    ...:                     continue                                 
    ...:                 else:                                        
    ...:                     values.append(temp_values)               
    ...:                     keys.append(cash_keys)                   
    ...:                     cash_keys=i                              
    ...:                     temp_values=[]                           
    ...:                     probel=False                             
    ...:             else:                                            
    ...:                     print(values,"values   "+"\n"+"-"*30)    
    ...:                     print(keys,"keys     "+"\n"+"-"*30)      
    ...:                     temp_values.append(i)                    
    ...:                     probel=True                          
			     continue                                 
    ...:         keys.append(cash_keys)                               
    ...:         values.append(empty_list)                            
    ...:         slovar=dict(zip(keys,values))                        
    ...:     return slovar       
