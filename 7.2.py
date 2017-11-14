def trunk_gen(trunk):
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
     

