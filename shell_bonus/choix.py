from menu import aff_menu2, aff_menu3, aff_menu3bonus, aff_menu4
from infosgeneral import aff_sys_vers, aff_time, aff_kernel_vers,aff_hardware_infos
from infosgeneral2 import file_open_limit, proc_open_limit, list_package
from infosreseau  import aff_ip,aff_interface,aff_nb_paquets,aff_route,aff_ip_forward
from infosreseau2  import desact_inter,activ_inter,aff_ping,aff_etat_co,act_ip
from process import process_info, simple_kill, forced_kill, runproc
import time, curses, sys

def choixinfo(princip_window):
    aff_menu2(princip_window)
    c = princip_window.getch()
    if c == ord('1'):
        princip_window.clear()
        quit = aff_sys_vers(princip_window)
        if quit == True:
            sys.exit()
        var = choixinfo(princip_window)
        if var == ord('0'):
            return var
    elif c == ord("2"):
        aff_time(princip_window)
        var = choixinfo(princip_window)
        if var == ord('0'):
            return var
    elif c == ord("3"):
        quit = aff_kernel_vers(princip_window)
        if quit == True:
            sys.exit()
        var = choixinfo(princip_window)
        if var == ord('0'):
            return var
    elif c == ord("4"):
        aff_hardware_infos(princip_window)
        var = choixinfo(princip_window)
        if var == ord('0'):
            return var
    elif c == ord("5"):
        file_open_limit(princip_window)
        var = choixinfo(princip_window)
        if var == ord('0'):
            return var
    elif c == ord("6"):
        proc_open_limit(princip_window)
        var = choixinfo(princip_window)
        if var == ord('0'):
            return var
    elif c == ord("7"):
        list_package(princip_window)
        var = choixinfo(princip_window)
        if var == ord('0'):
            return var
    elif c == ord('q') or c == ord('Q'):
            sys.exit()
    return c

def choixinfo2(princip_window):
    aff_menu3(princip_window)
    c = princip_window.getch()
    if c == ord("1"):
        aff_ip(princip_window)
        var = choixinfo2(princip_window)
        if var == ord('0'):
            return var
    elif c == ord("2"):
        aff_interface(princip_window)
        var = choixinfo2(princip_window)
        if var == ord('0'):
            return var
    elif c == ord("3"):
        aff_nb_paquets(princip_window)
        var = choixinfo2(princip_window)
        if var == ord('0'):
            return var
    elif c == ord("4"):
        aff_route(princip_window)
        var = choixinfo2(princip_window)
        if var == ord('0'):
            return var
    elif c == ord("5"):
        aff_ip_forward(princip_window)
        var = choixinfo2(princip_window)
        if var == ord('0'):
            return var
    elif c == ord('a'):
        var = choixinfo2bonus(princip_window)
        if var == ord('0'):
            return var
    return c

def choixinfo2bonus(princip_window):
    princip_window.clear()
    aff_menu3bonus(princip_window)
    princip_window.refresh()
    c = princip_window.getch()
    if c == ord("6"):
        desact_inter(princip_window)
        choixinfo2bonus(princip_window)
    elif c == ord("7"):
        activ_inter(princip_window)
        choixinfo2bonus(princip_window)
    elif c == ord("8"):
        aff_ping(princip_window)
        choixinfo2bonus(princip_window)
    elif c == ord("9"):
        act_ip(princip_window)
        choixinfo2bonus(princip_window)
    elif c == ord("a"):
        choixinfo2(princip_window)
    elif c == ord("0"):
        princip_window.clear()
        return
    else:
        choixinfo2bonus(princip_window)

def choixinfo3(princip_window):
    princip_window.clear()
    aff_menu4(princip_window)
    c = princip_window.getch()
    if c == ord("2"):
        princip_window.clear()
        curses.echo()
        curses.curs_set(1)
        princip_window.addstr(8, 25,"Processus :",curses.color_pair(1))
        mystr = princip_window.getstr()
        princip_window.refresh()
        princip_window.clear()
        exist = process_info(princip_window, mystr)
        curses.noecho()
        curses.curs_set(0)
        if exist == True:
            princip_window.addstr(9,0,"============================================================================")
            princip_window.addstr(11,20,"1 : Arreter le processus :")
            princip_window.addstr(12,20,"2 : Forcer l'arret du processus :")
            princip_window.addstr(14,0,"============================================================================")
            c = princip_window.getch()
            if c == ord('0'):
                choixinfo3(princip_window)
            elif c == ord('1'):
                simple_kill(princip_window, mystr)
            elif c == ord('2'):
                forced_kill(princip_window, mystr)
        else:
            choixinfo3(princip_window)
    elif c == ord('3'):
        runproc(princip_window)
        princip_window.clear()
        princip_window.refresh()
        choixinfo3(princip_window)
    return c
