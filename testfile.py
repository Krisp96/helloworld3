import subprocess
def ping_ip(ip_address):
	reply = subprocess.run(['ping', '-c', '3', '-n', ip_address],
	stdout=subprocess.PIPE,
	stderr=subprocess.PIPE)
	if reply.returncode == 0:
		return  reply.stdout.decode('utf-8')
	else:
		return  reply.stderr
print(type(ping_ip("8.8.8.8")))
print(ping_ip('a'))
