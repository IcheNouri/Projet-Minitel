import os, sys
import time
import curses

def file_open_limit(princip_window):
    princip_window.clear()
    princip_window.addstr(6,23,"Limite de fichiers ouverts : ",curses.color_pair(1))
    princip_window.addstr(8,33,"")
    fich=os.popen('ulimit -n')
    fich1=fich.read()
    princip_window.addstr(fich1)
    princip_window.addstr(17,0,"0 : Retour au menu principal :")
    princip_window.refresh()
    c = princip_window.getch()
    if c == ord("0"):
        princip_window.clear()
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        file_open_limit(princip_window)
    return

def proc_open_limit(princip_window):
    princip_window.clear()
    princip_window.addstr(6,23,"Limite de processus ouverts : ",curses.color_pair(1))
    princip_window.addstr(8,33,"")
    fich=os.popen('ulimit' ' -p')
    fich1=fich.read()
    princip_window.addstr(fich1)
    princip_window.addstr(17,0,"0 : Retour au menu principal :")
    princip_window.refresh()
    c = princip_window.getch()
    if c == ord("0"):
        princip_window.clear()
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        file_open_limit(princip_window)
    return

def list_package(princip_window):
    princip_window.clear()
    princip_window.addstr(0,0,"====================================================")
    princip_window.addstr(1,0,"0 : retour en arriere ")
    princip_window.addstr(3,0,"1 : Liste de paquets installes ")
    princip_window.addstr(5,0,"2 : Liste detaillee ")
    princip_window.addstr(7,0,"====================================================")
    princip_window.refresh()
    c = princip_window.getch()
    if c == ord("1"):
        princip_window.clear()
        pack=os.popen('dpkg --get-selections')
        pack1=pack.read()
        princip_window.addstr("Liste des paquets installes : ")
        princip_window.addstr(pack1)
        princip_window.addstr(17,0,"0 : Retour au menu principal :")
        princip_window.refresh()
        c = princip_window.getch()
        if c == ord("0"):
            princip_window.clear()
            list_package(princip_window)
        # else:
        #     print "Command not found"
        #     time.sleep(2)
    elif c == ord("2"):
        princip_window.clear()
        pack=os.popen('dpkg -l')
        pack1=pack.read()
        princip_window.addstr("Liste detaillee des paquets installes : ")
        princip_window.addstr(pack1)
        princip_window.addstr("0 : Retour au menu principal :")
        princip_window.refresh()
        c = princip_window.getch()
        if c == ord("0"):
            princip_window.clear()
            list_package()
        # else:
        #     princip_window.addstr "Command not found"
        #     time.sleep(2)
    if c == ord("0"):
        princip_window.clear()
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        list_package(princip_window)
    return
