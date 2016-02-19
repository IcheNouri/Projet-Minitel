# -*-coding: utf-8 -*-

import os, sys
import time
import curses

def aff_ip(princip_window):
    princip_window.clear()
    princip_window.addstr(6,30,"Adresse IP : ",curses.color_pair(1))
    princip_window.addstr(8,30,"")
    ip= os.popen("ifconfig eth0 | grep -E 'inet addr:' | cut -d: -f2 | awk '{ print $1}'")
    ip2 = ip.read()
    princip_window.addstr(ip2)
    princip_window.addstr(17,0,"0 : Retour en arriere :")
    c = princip_window.getch()
    if c == ord("0"):
        princip_window.clear()
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        aff_ip(princip_window)
    return

def aff_interface(princip_window):
    princip_window.clear()
    princip_window.addstr(4,25,"Interface existantes : ",curses.color_pair(1))
    princip_window.addstr(6,0,"")
    inter = os.popen("ifconfig -s")
    inter2 = inter.read()
    princip_window.addstr(inter2)
    princip_window.addstr(17,0,"0 : Retour en arriere :")
    c = princip_window.getch()
    if c == ord("0"):
        princip_window.clear()
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        aff_interface(princip_window)
        return

def aff_nb_paquets(princip_window):
    princip_window.clear()
    princip_window.addstr(4,22,"Nombre de paquets transmis/recu : ",curses.color_pair(1))
    rx= os.popen("ifconfig eth0 | grep -E 'RX packets:' | cut -d: -f2 | awk '{ print $1}'")
    rx2 = rx.read()
    tx= os.popen("ifconfig eth0 | grep -E 'TX packets:' | cut -d: -f2 | awk '{ print $1}'")
    tx2 = tx.read()
    princip_window.addstr(6,23,"Nombre de paquets recu: ")
    princip_window.addstr(rx2)
    princip_window.addstr(8,23,"Nombre de paquets transmis: ")
    princip_window.addstr(tx2)
    princip_window.addstr(17,0,"0 : Retour en arriere :")
    c = princip_window.getch()
    if c == ord("0"):
        princip_window.clear()
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        aff_nb_paquets(princip_window)
    return

def aff_route(princip_window):
    princip_window.clear()
    princip_window.addstr(4,30,"Route : ",curses.color_pair(1))
    princip_window.addstr(6,0,"")
    rout = os.popen("route -n")
    rout2 = rout.read()
    princip_window.addstr(rout2)
    princip_window.addstr(17,0,"0 : Retour en arriere :")
    c = princip_window.getch()
    if c == ord("0"):
        princip_window.clear()
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        aff_route(princip_window)
        return

def aff_ip_forward(princip_window):
    princip_window.clear()
    princip_window.addstr(6,30,"Fordward : ",curses.color_pair(1))
    forward = os.popen("cat /proc/sys/net/ipv4/ip_forward")
    forward2 = forward.read()
    if int(forward2) == 0:
        princip_window.addstr(8,18,"Le forward de paquet n'est pas active")
    elif int(forward2) == 1:
        princip_window.addstr(8,18,"Le forward de paquet est active")
    princip_window.addstr(17,0,"0 : Retour en arriere :")
    c = princip_window.getch()
    if c == ord("0"):
        princip_window.clear()
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        aff_ip_forward(princip_window)
        return
