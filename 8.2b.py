from pars_cdp_neighbour import cdp_neihbors 
from draw_network_graph import draw_topology
string="""SW1>show cdp neighbors

Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R1           Eth 0/1         122           R S I           2811       Eth 0/0
R2           Eth 0/2         143           R S I           2811       Eth 0/0
R3           Eth 0/3         151           R S I           2811       Eth 0/0"""
draw_topology(cdp_neihbors(string))

