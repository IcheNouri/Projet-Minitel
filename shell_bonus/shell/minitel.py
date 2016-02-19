#! /usr/bin/env python
# -*-coding: utf-8 -*-
from menu import aff_menu1,aff_menu2,aff_menu4,aff_menu3,aff_menu3bonus,aff_menu_bonus
from infosgeneral import aff_sys_vers,aff_time,aff_kernel_vers,aff_hardware_infos
from infosgeneral2 import file_open_limit,proc_open_limit,list_package
from process import get_proc_list,process_exist,get_pid,process_info,simple_kill,forced_kill,runproc
from infosreseau  import aff_ip,aff_interface,aff_nb_paquets,aff_route,aff_ip_forward
from infosreseau2  import desact_inter,activ_inter,aff_ping,aff_etat_co,aff_ch
import time
import os

def choixinfo():
    aff_menu2()
    c=raw_input(">")
    if c == "1":
        aff_sys_vers()
        choixinfo()
    elif c == "2":
        aff_time()
        choixinfo()
    elif c == "3":
        aff_kernel_vers()
        choixinfo()
    elif c == "4":
        aff_hardware_infos()
        choixinfo()
    elif c == "5":
        file_open_limit()
        choixinfo()
    elif c == "6":
        proc_open_limit()
        choixinfo()
    elif c == "7":
        list_package()
        choixinfo()
    elif c == "0":
        princip()
    else:
        print "Command not found."
        time.sleep(1)
        choixinfo()

def choixinfo2():
    aff_menu3()
    c=raw_input(">")
    if c == "1":
        aff_ip()
        choixinfo2()
    elif c == "2":
        aff_interface()
        choixinfo2()
    elif c == "3":
        aff_nb_paquets()
        choixinfo2()
    elif c == "4":
        aff_route()
        choixinfo2()
    elif c == "5":
        aff_ip_forward()
        choixinfo2()
    elif c == "a":
        choixinfo2bonus()
    elif c == "0":
        princip()
    else:
        print "Command not found."
        time.sleep(1)
        choixinfo2()

def choixinfo2bonus():
    aff_menu3bonus()
    c=raw_input(">")
    if c == "6":
        desact_inter()
        choixinfo2bonus()
    elif c == "7":
        activ_inter()
        choixinfo2bonus()
    elif c == "8":
        aff_ping()
        choixinfo2bonus()
    elif c == "9":
        aff_etat_co()
        choixinfo2bonus()
    elif c == "10":
        aff_ch()
        choixinfo2bonus()
    elif c == "a":
        choixinfo2()
    elif c == "0":
        princip()
    else:
        print "Command not found."
        time.sleep(1)
        choixinfo2bonus()

def choixinfo3():
    aff_menu4()
    c=raw_input(">")
    if c == "0":
        princip()
    elif c == "1":
        get_proc_list()
        choixinfo3()
    elif c == "2":
        print "Processus :"
        c=raw_input(">")
        if c == '':
            print "Invalid command"
            time.sleep(2)
            choixinfo3()
        else:
            print("\033[H\033[J")
            exist = process_info(c)
            if exist == True:
                choix = c
                print("\n====================================================\n")
                print("0 : Retour en arriere :\n")
                print("1 : Arreter le processus :\n")
                print("2 : Forcer l'arret du processus :\n")
                print("====================================================\n")
                c=raw_input(">")
                if c == "1":
                    simple_kill(choix)
                    print("Processus killed \n")
                    time.sleep(2)
                    choixinfo3()
                elif c == "2":
                    forced_kill(choix)
                    print("Processus killed \n")
                    time.sleep(2)
                    choixinfo3()
                elif c == "0":
                    choixinfo3()
            choixinfo3()
    elif c == "3":
        runproc()
        choixinfo3()
    else:
        print "Command not found."
        time.sleep(1)
        choixinfo3()

def princip():
    print("\033[H\033[J")
    aff_menu1()
    c=raw_input(">")
    while c != "quit":
        if c == "1":
            choixinfo()
        elif c == "2":
            choixinfo2()
        elif c == "3":
            choixinfo3()
        elif c == "0":
            return
        else:
            print "Command not found."
        c=raw_input(">")
    return

def principbonus():
    print("\033[H\033[J")
    aff_menu_bonus()
    c=raw_input(">")
    if c == "1":
        princip()
        principbonus()
    elif c == "2":
        os.system('sh /home/sam/pro/shelletna/shell_bonus/lan.sh')

principbonus()
