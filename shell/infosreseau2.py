# -*-coding: utf-8 -*-

import os
import time

def desact_inter():
    print("\033[H\033[J")
    print("\033[31mDesactivation de l'interface Ethernet : \033[0m\n")
    print("\n====================================================\n")
    print("1 : Desactiver l'interface Ethernet :\n")
    print("2 : Annuler l'operation :\n")
    print("====================================================\n")
    c=raw_input(">")
    if c == "1":
        os.system("ifconfig eth0 down")
        print "L'interface Ethernet a ete desactive\n"
        time.sleep(1)
    elif c == "2":
        print "Operation annulee\n"
        time.sleep(1)
    else:
        print "\033[31mCommand not found\033[0m"
        time.sleep(2)


def activ_inter():
    print("\033[H\033[J")
    print("\033[31mActivation de l'interface Ethernet : \033[0m\n")
    print("\n====================================================\n")
    print("1 : Activer l'interface Ethernet :\n")
    print("2 : Annuler l'operation :\n")
    print("====================================================\n")
    c=raw_input(">")
    if c == "1":
        os.system("ifconfig eth0 up")
        print "L'interface Ethernet a ete active\n"
        time.sleep(1)
    elif c == "2":
        print "Operation annulee\n"
        time.sleep(1)
    else:
        print "\033[31mCommand not found\033[0m"
        time.sleep(2)


def aff_ping():
    print("\033[H\033[J")
    print("\033[31mPing: \033[0m\n")
    os.system("ping -c10 eth0")
    print "\n0 : Retour au menu principal :"
    c=raw_input(">")

def aff_etat_co():
    print("\033[H\033[J")
    print("\033[31mEtat des connexions: \033[0m\n")
    os.system("netstat")
    print "\n0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "\033[31mCommand not found\033[0m"
        time.sleep(2)

def aff_ch():
    print("\033[H\033[J")
    print("\033[31mAffichage du chemin parcouru par un paquet: \033[0m\n")
    os.system("traceroute eth0")
    print "\n0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "\033[31mCommand not found\033[0m"
        time.sleep(2)
