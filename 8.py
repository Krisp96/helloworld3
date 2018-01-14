from 8_2a import cdp_neihbors
from draw_network_graph import draw_topology
from sys import argv
file_names=argv[1:]
result_slov={}
for a in file_names:
	with open(a,"r") as f:
		res_string=""
		for line in f:
			res_string=res_string+line
	result_slov.update(cdp_neihbors(res_string))
	#print(result_slov)
draw_topology(result_slov)

