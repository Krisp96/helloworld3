 def trunk_gen(trunk):                       
    ...:     trunk_template = ['interfase {}','switchport trunk encapsulation d
    ...: ot1q',                  
    ...:      'switchport mode trunk',
    ...:      'switchport trunk native vlan 999',
    ...:      'switchport trunk allowed vlan   {}']
    ...:     slov={}
    ...:     end_res=[]  
    ...:     for i in trunk:
    ...:              result=[]
    ...:              slov.setdefault(i)
    ...:              for y in trunk_template:
    ...:                  if y.startswith("interfase"):
    ...:                      pass
    ...:                  elif y.startswith("switchport trunk allowed"):
    ...:                      result.append(y.format(",".join([str(a) for a in 
    ...: trunk[i]])))
    ...:                  else:
    ...:                      result.append(y.strip("\n"))
    ...:              slov[i]=result        
    ...:     return slov
    ...:      

