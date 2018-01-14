from my_func import generate_acces
from my_func import trunk_gen
from my_func import get_int_vlan_map
from my_func import ignore_command
a=raw_input("vvedite config com    ")
b=raw_input("end file      ")
with open(a,"r") as f:
	trunk,access=get_int_vlan_map(a)
	print(trunk,access)
	with open (b,"w") as F:
		print>>F,generate_acces(access)
		print>>F,trunk_gen(trunk)

