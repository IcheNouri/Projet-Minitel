# -*-coding: utf-8 -*-

import os, sys
import time
import curses

def desact_inter(princip_window):
    princip_window.clear()
    princip_window.addstr(4,20,"Desactivation de l'interface Ethernet : ",curses.color_pair(1))
    princip_window.addstr(6,0,"============================================================================")
    princip_window.addstr(7,20,"1 : Desactiver l'interface Ethernet :")
    princip_window.addstr(9,20,"2 : Annuler l'operation :")
    princip_window.addstr(10,0,"============================================================================")
    c = princip_window.getch()
    if c == ord("1"):
        os.system("ifconfig eth0 down")
        princip_window.clear()
        princip_window.addstr(8,20,"L'interface Ethernet a ete desactive",curses.color_pair(1))
        princip_window.refresh()
        time.sleep(2)
    elif c == ord("2"):
        princip_window.clear()
        princip_window.addstr(8,25,"Operation annulee",curses.color_pair(1))
        princip_window.refresh()
        time.sleep(2)
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        desact_inter(princip_window)
    return

def activ_inter(princip_window):
    princip_window.clear()
    princip_window.addstr(4,20,"Activation de l'interface Ethernet : ",curses.color_pair(1))
    princip_window.addstr(6,0,"============================================================================")
    princip_window.addstr(7,20,"1 : Activer l'interface Ethernet :")
    princip_window.addstr(9,20,"2 : Annuler l'operation :")
    princip_window.addstr(10,0,"============================================================================")
    c = princip_window.getch()
    if c == ord("1"):
        os.system("ifconfig eth0 up")
        princip_window.clear()
        princip_window.addstr(8,20,"L'interface Ethernet a ete active",curses.color_pair(1))
        princip_window.refresh()
        time.sleep(2)
    elif c == ord("2"):
        princip_window.clear()
        princip_window.addstr(8,25,"Operation annulee",curses.color_pair(1))
        princip_window.refresh()
        time.sleep(2)
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        activ_inter(princip_window)
    return

def aff_ping(princip_window):
    princip_window.clear()
    princip_window.addstr(2,30,"Ping: ",curses.color_pair(1))
    princip_window.refresh()
    var = os.popen("ping -c5 eth0")
    var2 = var.read()
    princip_window.addstr(4,0,var2)
    princip_window.addstr(17,0,"0 :Retour en arriere :")
    #princip_window.addstr(10,0,"0 : Retour au menu principal :")
    c = princip_window.getch()
    if c == ord('q') or c == ord('Q'):
        sys.exit()

def aff_etat_co(princip_window):
    princip_window.clear()
    princip_window.addstr(0,0,"Etat des connexions: ")
    princip_window.refresh()
    os.system("netstat")
    # princip_window.addstr(1,0,var)
    # princip_window.addstr(17,0,"0 : Retour en arriere :")
    c = princip_window.getch()
    if c == ord("0"):
        princip_window.clear()
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        aff_etat_co(princip_window)
    return

def act_ip(princip_window):
    princip_window.clear()
    princip_window.addstr(4,12,"Activation ou Desactivation du routage IP : ",curses.color_pair(1))
    princip_window.addstr(6,0,"============================================================================")
    princip_window.addstr(8,20,"1 : Activer le routage IP :")
    princip_window.addstr(10,20,"2 : Desactiver le routage IP :")
    princip_window.addstr(12,20,"3 : Annulee l'operation:")
    princip_window.addstr(13,0,"============================================================================")
    c = princip_window.getch()
    if c == ord("1"):
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
        princip_window.clear()
        princip_window.addstr(8,25,"Activation du routage IP",curses.color_pair(1))
        princip_window.refresh()
        time.sleep(2)
    elif c == ord("2"):
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        princip_window.clear()
        princip_window.addstr(8,25,"Desactivation du routage IP",curses.color_pair(1))
        princip_window.refresh()
        time.sleep(2)
    elif c == ord("3"):
        princip_window.clear()
        princip_window.addstr(8,25,"Operation annulee",curses.color_pair(1))
        princip_window.refresh()
        time.sleep(2)
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        act_ip(princip_window)
    return
