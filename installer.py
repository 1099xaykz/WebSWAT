import os
import time

BLACK = '\033[1;30m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
RESET = '\033[1;39m'

def banner():
	print(RED + """
██╗    ██╗███████╗██████╗     ███████╗   ██╗    ██╗    █████╗ ████████╗
██║    ██║██╔════╝██╔══██╗    ██╔════╝   ██║    ██║   ██╔══██╗╚══██╔══╝
██║ █╗ ██║█████╗  ██████╔╝    ███████╗   ██║ █╗ ██║   ███████║   ██║   
██║███╗██║██╔══╝  ██╔══██╗    ╚════██║   ██║███╗██║   ██╔══██║   ██║   
╚███╔███╔╝███████╗██████╔╝    ███████║██╗╚███╔███╔╝██╗██║  ██║██╗██║   
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝╚═╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝   
                            INSTALLER
""")

def main():
	print(GREEN + "[+] " + WHITE + "Instalando...")
	time.sleep(2)
	print(WHITE + "Probando distintas formas de instalar" + RED)
	time.sleep(1)
	os.system("pip install requests")
	os.system("py -m install requests")
	os.system("python -m install requests")
	time.sleep(1)
	print(GREEN + """
---------------------------------------------------------
-                     WEB SWAT TOOL                     -
-                INSTALADO CORRECTAMENTE                -
-                ejecuta: python3 main.py               -
---------------------------------------------------------
""")
	exit()

if __name__ == '__main__':
	main()