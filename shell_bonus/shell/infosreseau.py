# -*-coding: utf-8 -*-

import os
import time

def aff_ip():
    print("\033[H\033[J")
    print("\033[31mAdresse IP : \033[0m\n")
    ip= os.popen("ifconfig eth0 | grep -E '^          inet addr:' | cut -d: -f2 | awk '{ print $1}'")
    ip2 = ip.read()
    print(ip2)
    print "0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "Command not found"
        time.sleep(2)

def aff_interface():
    print("\033[H\033[J")
    print("\033[31mInterface existantes : \033[0m\n")
    inter = os.popen("ifconfig -s")
    inter2 = inter.read()
    print(inter2)
    print "0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "Command not found"
        time.sleep(2)

def aff_nb_paquets():
    print("\033[H\033[J")
    print("\033[31mNombre de paquets transmis/reçu : \033[0m\n")
    rx= os.popen("ifconfig eth0 | grep -E '^          RX packets:' | cut -d: -f2 | awk '{ print $1}'")
    rx2 = rx.read()
    tx= os.popen("ifconfig eth0 | grep -E '^          TX packets:' | cut -d: -f2 | awk '{ print $1}'")
    tx2 = tx.read()
    print "Nombre de paquets reçu: ", rx2
    print "Nombre de paquets transmis: ", tx2
    print "0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "Command not found"
        time.sleep(2)

def aff_route():
    print("\033[H\033[J")
    print("\033[31mRoute : \033[0m\n")
    rout = os.popen("route -n")
    rout2 = rout.read()
    print(rout2)
    print "0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "Command not found"
        time.sleep(2)


def aff_ip_forward():
    print("\033[H\033[J")
    print("\033[31mRoute : \033[0m\n")
    forward = os.popen("cat /proc/sys/net/ipv4/ip_forward")
    forward2 = forward.read()
    if int(forward2) == 0:
        print "Le forward de paquet n'est pas active"
    elif int(forward2) == 1:
        print "Le forward de paquet est active"
    print "\n0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "Command not found"
        time.sleep(2)
