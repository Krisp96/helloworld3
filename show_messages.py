import getpass
import sys
import telnetlib
import time
import re
from concurrent.futures	import ProcessPoolExecutor, as_completed 

#IP = input("vvedite IP   ")
#TIME=input("vvedite vrema avarii   ")
USER="center"
PASSWORD="monitor.3-Rop=7."
lst=[]

def conn_to_messages(IP,TIME):
	up=False
	try:
                with telnetlib.Telnet(IP) as t:
                    t.read_until(b'login:')
                    t.write(USER.encode(encoding="utf-8")+b"\n")
                    t.read_until(b'Password:')
                    t.write(PASSWORD.encode(encoding="utf-8")+b'\n')
                    t.write(b'set cli screen-length 0\n')
                    t.write(b"show log messages | match SNMP_TRAP | match "+TIME.encode(encoding="utf-8")+b'\n')
                #тут ищем в логах трапы с временем которое даём коду
                    time.sleep(8)
                #time.sleep(5)
                    output=t.read_very_eager().decode('utf-8')
                    print(output+"\n")
                    output=output.split("\n")
                    regex=re.compile(".+\s(?P<Device>\S+)-re[01].+down.+ifName (?P<PORT>\S+)") #этим регексом ищем название оборудвания и порт на который надо написать show 
                    for i in output:
                        if regex.search(i)!=None:
                            print("worked out")
                        #print("regex worked out, group() ---   ",regex.search(i).group("PORT"))
                            t.write(b"show interface "+regex.search(i).group("PORT").encode(encoding="utf-8")+b'\n') #пишем show interface *port*
                            Device=re.search(regex,i).group("Device")
                            time.sleep(8)
                        #time.sleep(5)
                        #print("show interface "+regex.search(i).group(PORT))
                            continue
                        else:
                            continue
                    output=t.read_very_eager().decode('utf-8')
                    output=output.split("\n")
                    regex=re.compile("Physical interface:\s+(?P<port>\S+),\s.+Physical link is (?P<UP>\S+)|Description:(?P<description>.+)$")
                    #тут формируем тело оповещения
                    for i in output:
                        if regex.search(i)==None:
                        #print("regex didnt worked out   ",i)
                            continue
                        elif regex.search(i).group("description")!=None and not up:
                        #print("regex worked out   ",i)
                            description=regex.search(i).group("description")
                            a=Device+" "+port+" "+description
                            lst.append(a)
                        #print(Device,port,description)
                        else:
                            if regex.search(i).group("UP")=="Down":
                            #print("regex worked out   ",i)
                                port=regex.search(i).group("port")
                            else:
                                up=True
                    #lst=set(lst)
	except TimeoutError:
                    print(f"{IP} не доступен")
	return lst
#print(output)
