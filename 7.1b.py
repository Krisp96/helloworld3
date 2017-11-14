def generate_acces(access,psecurity=False):                    
    ...:     access_template = ['interface {}','switchport mode access','switchport access vlan {}',
    ...:   'switchport nonegotiate',
    ...:   'spanning-tree portfast',
    ...:  'spanning-tree bpduguard enable']
    ...:     port_sec=['switchport port-security maximum 2',
    ...: 'switchport port-security violation restrict']
    ...:     slov={}
    ...:     for i in access:
    ...:           result=[]
    ...:           slov.setdefault(i)  
    ...:           for y in access_template:
    ...:             if y.startswith("interface"):
    ...:                 pass  
    ...:             elif y.endswith("vlan {}"):
    ...:                  result.append(y.format(access[i]))
    ...:             else:
    ...:                 result.append(y)
    ...:           if psecurity:
    ...:                 result.extend(port_sec)
    ...:           slov[i]=result
    ...:           print(slov)
    ...:     return slov
    ...: 

