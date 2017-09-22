network=raw_input("Vvedite network        ")
network=network.strip(" ")
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

net_list=[0,0,0,0] 
mask=int(mask[0])   
x=int(mask/8)                               
y=mask%8                      
z=4-x                 
if mask==24:               
             net_list[0]=255                      
             net_list[1]=255                                          
             net_list[2]=255                      
             net_list[3]=0                           
else:                                       
          if x==0:                                
              n=7                                 
              for i in range (y):                 
                      net_list[0]=net_list[0]+2**n
                      n=n-1          
              net_list[1]=0          
              net_list[2]=0          
              net_list[3]=0            
          else:                        
               if y==0:                
                  j=0                     
                  for j in range(x):        
                      net_list[j]=255       
                  j=1                       
                  for j in range (z):                  
                       net_list[-j-1]=0                
               else:                                   
                       j=0                             
                       for j in range (x):             
                           net_list[j]=255 
    		       n=7                  
                       for j in range(y):   
                           net_list[x]=net_list[x]+2**n
                           n=n-1                       
                       for j in range (z-1):           
                         net_list[-j-1]=0  
for i in range (5):
         if i==0:
             print("\n" * 5)
             print("MASK:")
         if i==4:
             print("\n")
             for j in range (4):
                print("%-15s" % bin(net_list[j])[2:].zfill(8) ),
         else:
                print("%-15d" % net_list[i]  ),            
                                                      



  

