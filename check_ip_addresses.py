import subprocess     
def check_ip_addresses(ip_address):
	reply = subprocess.run(['ping', '-c', '3', '-n', ip_address],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	return reply.stdout.decode("utf-8")
	
	
