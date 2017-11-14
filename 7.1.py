def generate_acces(access):
     access_template = ['interface {}','switchport mode access',
 	'switchport access vlan {}',
  'switchport nonegotiate',
  'spanning-tree portfast',
 'spanning-tree bpduguard enable']
	result=[]
	for i in access:
          for y in access_template:
              if y.startswith("interface"):
                 result.append(y.format(i))
            elif y.endswith("vlan {}"):
                  result.append(y.format(access[i]))
               else:
                  result.append(y)
	print(result)
	return result
 

