try:
	import time
	import os
	import sys
	import random as rd
	import requests
except ImportError:
	print(RED + "[+] " + WHITE + "Ejecuta el instalador primero con 'python3 installer.py'")

BLACK = '\033[1;30m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
RESET = '\033[1;39m'

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)

def banner():
	print(RED + """
██╗    ██╗███████╗██████╗     ███████╗   ██╗    ██╗    █████╗ ████████╗
██║    ██║██╔════╝██╔══██╗    ██╔════╝   ██║    ██║   ██╔══██╗╚══██╔══╝
██║ █╗ ██║█████╗  ██████╔╝    ███████╗   ██║ █╗ ██║   ███████║   ██║   
██║███╗██║██╔══╝  ██╔══██╗    ╚════██║   ██║███╗██║   ██╔══██║   ██║   
╚███╔███╔╝███████╗██████╔╝    ███████║██╗╚███╔███╔╝██╗██║  ██║██╗██║   
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝╚═╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝   
                            By Xaykz
                         TikTok: @xaykz
""")

def menu():
	print(RED + "==> " + WHITE + "Para poner tu index, ponelo en la ruta 'webs/'")
	print(RED + "--> " + WHITE + "1 Defacear")
	print(RED + "--> " + WHITE + "2 Generar webs")
	print(RED + "--> " + WHITE + "3 Ver contenido del archivo de paginas a defacear")
	print(RED + "--> " + WHITE + "4 Añadir una pagina a la lista de pagina a intentar defacear")
	print(RED + "--> " + WHITE + "5 Ver paginas que probablemente se pudieron defacear")
	print()

def main():
	banner()
	while True:
		menu()
		peticion = input(RED + "$ " + WHITE + "Selecciona una option > ")
		if peticion == "2":
			try:
				print(RED + "$ " + WHITE + "Ejemplo: org, com, co.za, co.il, sa, gob, gov")
				print(RED + "$ " + WHITE + "Recomendados: com, org, sa, co.il")
				extension = input(RED + "$ " + WHITE + "Extension > ")
				while True:
					l1 = rd.choice("abcdefghijklmnopqrstuvwxyz0123456789")
					l2 = rd.choice("abcdefghijklmnopqrstuvwxyz0123456789")
					l3 = rd.choice("abcdefghijklmnopqrstuvwxyz0123456789")
					l4 = rd.choice("abcdefghijklmnopqrstuvwxyz0123456789")
					l5 = rd.choice("abcdefghijklmnopqrstuvwxyz0123456789")
					l6 = rd.choice("abcdefghijklmnopqrstuvwxyz0123456789")
					pagina = "http://" + l1 + l2 + l3 + l4 + l5 + l6 + "." + extension + "\n"
					pagina2 = "http://" + l1 + l2 + l3 + l4 + l5 + l6 + "." + extension
					try:
						r = requests.get(pagina2)
						if r.status_code == 200:
							print(GREEN + "$ " + pagina2 + WHITE + " - Existe")
							a = open("webs/target.txt", "a")
							a.write(pagina2+"\n")
							a.close()
					except:
						print(RED + "$ " + pagina2 + WHITE + " - No existe")
			except KeyboardInterrupt:
				print("Cerrando...")
		elif peticion == "1":
			try:
				os.system("cd webs && python3 deface.py")
			except KeyboardInterrupt:
				print("Cerrando...")
		elif peticion == "3":
			print(RED + "$ " + WHITE + "Contenido del archivo de paginas a defacear:")
			print()
			try:
				a = open("webs/target.txt", "r")
				b = a.read()
				print(WHITE + b)
				a.close()
			except FileNotFoundError:
				print(RED + "El archivo '" + WHITE + "target.txt" + RED + "' no fue encontrado")
		elif peticion == "4":
			print(RED + "$ " + WHITE + "Ejemplo: http://ejemplo.com")
			while True:
				pagina = input(RED + "$ " + WHITE + "Pagina > ")
				try:
					r = requests.get(pagina)
					if r.status_code == 200:
						print(GREEN + "$ " + pagina + WHITE + " - Existe")
						a = open("webs/target.txt", "a")
						a.write(pagina+"\n")
						a.close()
				except:
					print(RED + "$ " + pagina + WHITE + " - No Existe")
		elif peticion == "5":
			print(RED + "$ " + WHITE + "Paginas que probablemente se pudieron defacear:")
			print()
			try:
				a = open("webs/defaceadas.txt", "r")
				b = a.read()
				print(WHITE + b)
				a.close()
			except FileNotFoundError:
				print(RED + "El archivo '" + WHITE + "defaceadas.txt" + RED + "' no fue encontrado")

if __name__ == '__main__':
	main()