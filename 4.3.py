int_type=raw_input("Enter interface mode (access/trunk)   ")
int_num=raw_input("Enter interface type and number    ")
vlan_num=raw_input("Enter vlan(s) number(s)    ")
access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']
vivod= { 
"access": access_template ,
"trunk" : trunk_template
}
print('\n' + '-' * 30)
print('interface {}'.format(int_num))
print('\n'.join(vivod[int_type]).format(vlan_num))

