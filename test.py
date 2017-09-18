In [149]: if mask==24:
     ...:           net_list[0]=255
     ...:           net_list[1]=255
     ...:           net_list[2]=255
     ...:           net_list[3]=0
     ...: if x==0:
     ...:         net_list[0]=2**mask
     ...:         net_list[1,2,3]=0
     ...: else:
     ...:     if y==0:
     ...:       for j in range(x):
     ...:                 net_list[j-1]=255
     ...:       j=1
     ...:       for j in range (z):
     ...:                 net_list[-j]=0
     ...:     else:
     ...:         for j in range (x):
     ...:                 net_list[j-1]=255
     ...:                 net_list[x]=2**y
     ...:         j=1     
     ...:         for j in range (z-1):
     ...:                 net_list[-j]=0


