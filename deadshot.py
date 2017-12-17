#encoding: utf-8

import mechanize
from mechanize import Browser
from bs4 import BeautifulSoup
import socket,socks
import requests,sys,os

class color():
	lila="\033[95m"
	azul="\033[94m"
	amarillo="\033[93m"
	rojo="\033[91m"
	cyan="\033[36m"
	negrita="\033[1m"


def presentacion():
	skull=u"""
        $               
   *1▒g▒#▒$▒▒1▒,Q     
  ▒▒▒▒▒▒▒▒▓▒▒▒▒▒                       
#/▒▒▒▒▓▒▒▒▓▒▒▓▒g
1▒▒▒▒▓▓▒▓▓▒▓▒▒▒▓\  
 /@ $@@,0▒▒1▒|7$e$, 
       4j7▒4! 
|       #7Y*       \ 
4▒    #▒4▒▓9      4 
$▒9g e@▒▒!4▒▒$-  #e  
|▒▒▒▒▒#|   |e▓▒▒▓$e 
Yeg▒▓\,   $9▒▒▒e÷4  
 gp@l▒▒,▒▒Y@▒▒M7 7       
 , ▒▒@1▒▒▒▓9÷▒▒4Q  
    "▓  /Q▒-▒▒7,0$ 
 !     ▒▒    
 \▒\▒         ▒440 
 1▒\▒    *▒0    ▒ 
  1▓9▒▒▓# ▒*▓   ÷  
    e▒▒▒▓▒▒  ▓▒▒▒ 
       g               \n                                                                                                                             
"""    
	if (sys.platform != 'win32' or sys.platform != 'win64'):
		print color.cyan+color.negrita+skull	
	else:
		print skull
	

def tor():
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",9050,True)
	socket.socket=socks.socksocket
	r= requests.get("http://www.ip-adress.eu/")
	html=BeautifulSoup(r.text,'lxml')
	span = html.find_all('span')
	for etiquetas in span:
		if (sys.platform != 'win32' or sys.platform != 'win64'):
			print color.lila+"[**]IP: "+etiquetas.text	
		else:
			print "[**]IP: "+etiquetas.text
		

def magia(tecla):
	os.system('cls')
	siclo=True
	while siclo==True:
		presentacion()
		if tecla=="":
			if ( sys.platform != 'win64' or sys.platform != 'win32'):
				print color.azul+"\t1.Empezar"
				print color.rojo+"\t2.salir"
			else:
				print "\t1.Empezar"
				print "\t2.salir"
			try:
				opcion=int(raw_input("[+]: "))
				if opcion==1:
					a=True
					while a==True:
						os.system('cls')
						presentacion()
						try:
							tor()	
						except ImportError,e:
							if ( sys.platform != 'win64' or sys.platform != 'win32'):
								print color.rojo+"[ALERTA] No se tiene instalado el modulo socks"
							else:
								print "[ALERTA] No se tiene instalado el modulo socks"
						
						link=raw_input("[*URL*] ")
						spidy_1(link)
						print "------------------Urls de interes-------------------------"
						spidy_2(link)
						print "----------------------------------------------------------"
						print "\t1.Otro Escaneo(Por defecto)\t2.salir\n"
						opcion4=int(raw_input("[+] "))
						if opcion4!=1:
							os.system('cls')
							a=False
				elif opcion==2:
					os.system('cls')
					presentacion()
					print "\t\tCreditos a"
					print "------------------------------------------------------------------------"
					print "\t\t[La concha de tu hermana] "
					break	
			
			except Exception,e:
				if(sys.platform != 'win32' or sys.platform != 'win64'):
					print color.rojo+"[!] ERROR ALGO SE FUE AL CARJO!\n"
				else:
					print "[!] ERROR ALGO SE FUE AL CARJO!\n"
			
		else:
			print "se acabo"
			siclo=False

def spidy_1(url):
	"""todo lo que viene acontinuacion es para que la pagina trate al script como un navegador
	de lo contrario saldra un 403 o forbbiden MALDITOS FORBBIDEN"""
	br = Browser()
	# browser basic setup (for simulate a real web browser)<----todo para simular un navegador :D
	br.set_handle_equiv(True) # cuando tratar HTML http-equiv headers como HTTP headers
	br.set_handle_redirect(True) # para los redirect loops
	br.set_handle_referer(True) # para annadir un referer al objeto request
	br.set_handle_robots(False) # ignorar robots.txt
	br.set_debug_http(False) # bueno para la fase de development
	br.set_debug_responses(False) # mas debuggeo
	br.set_debug_redirects(False) # mas aun
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1) # puede usarse: br.set_handle_refresh(False)
	# para simular Firefox desde Fedora :)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	br.open(url)
	for link in br.links():
		print link.text,link.url

def spidy_2(url):
	"""todo lo que viene acontinuacion es para que la pagina trate al script como un navegador
	de lo contrario saldra un 403 o forbbiden MALDITOS FORBBIDEN"""
	br = Browser()
	# browser basic setup (for simulate a real web browser)<----todo para simular un navegador :D
	br.set_handle_equiv(True) # cuando tratar HTML http-equiv headers como HTTP headers
	br.set_handle_redirect(True) # para los redirect loops
	br.set_handle_referer(True) # para annadir un referer al objeto request
	br.set_handle_robots(False) # ignorar robots.txt
	br.set_debug_http(False) # bueno para la fase de development
	br.set_debug_responses(False) # mas debuggeo
	br.set_debug_redirects(False) # mas aun
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1) # puede usarse: br.set_handle_refresh(False)
	# para simular Firefox desde Fedora :)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	#x=['php?id=','php?ID=','php?decl_id=','pageid=','staff_id=','php?category=','php?'] #expresiones regulares, las mas comunes
	br.open(url)
	for link in br.links():
		if (re.search('php.id=|php.category=|php.idcategoria=|pageid=|php.ID=|php.decl_id|staff_id=',link.url)):# el . significa cualquier caracter el | es OR
			print link.url

presentacion()
tecla=raw_input("[*]presione enter para continuar...")
magia(tecla)
