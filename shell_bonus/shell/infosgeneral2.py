import os
import time

def file_open_limit():
    print("\033[H\033[J")
    print("\033[31mLimite de fichiers ouverts : \033[0m\n")
    fich=os.popen('ulimit -n')
    fich1=fich.read()
    print(fich1)
    print "0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "Command not found"
        time.sleep(2)

def proc_open_limit():
    print("\033[H\033[J")
    print("\033[31mLimite de processus ouverts : \033[0m\n")
    proc=os.popen('ulimit' ' -p')
    proc1=proc.read()
    print(proc1)
    print "0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "Command not found"
        time.sleep(2)

def list_package():
    print("\033[H\033[J")
    print("====================================================\n")
    print("0 : retour en arriere \n")
    print("1 : Liste de paquets installes \n")
    print("2 : Liste detaillee \n")
    print("====================================================\n")
    c=raw_input(">")
    if c == "1":
        pack=os.popen('dpkg --get-selections')
        pack1=pack.read()
        print("\033[31mListe des paquets installes : \033[0m\n")
        print(pack1)
        print "0 : Retour en arriere :"
        c=raw_input(">")
        if c == "0":
            list_package()
        else:
            print "Command not found"
            time.sleep(2)
    elif c == "2":
        pack=os.popen('dpkg -l')
        pack1=pack.read()
        print("\033[31mListe detaillee des paquets installes : \033[0m\n")
        print(pack1)
        print "0 : Retour en arriere :"
        c=raw_input(">")
        if c == "0":
            list_package()
        else:
            print "Command not found"
            time.sleep(2)
    elif c == "0":
        return
    else:
        print "Command not found"
        time.sleep(2)
