
from datetime import timedelta
import curses, sys
import platform
import os
import time


def aff_sys_vers(princip_window):
    princip_window.addstr(6, 20,"Version du systeme d'exploitation :", curses.color_pair(1))
    sys=platform.release()
    princip_window.addstr(8, 27,sys)
    princip_window.addstr(17, 0,"0 : Retour en arriere")
    c = princip_window.getch()
    if c == ord("0"):
        princip_window.clear()
    elif c == ord('q') or c == ord('Q'):
        return True
    else:
        aff_sys_vers(princip_window)
    return False


def aff_time(princip_window):
    princip_window.clear()
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
    princip_window.addstr(6, 32,"Uptime :", curses.color_pair(1))
    princip_window.addstr(8, 29,uptime_string)
    princip_window.addstr(17, 0,"0 : Retour en arriere :")
    c = princip_window.getch()
    if c == ord('q') or c == ord('Q'):
        sys.exit()
    elif c == ord("0"):
        princip_window.clear()
        # return
    else:
        aff_time(princip_window)

def aff_kernel_vers(princip_window):
    princip_window.clear()
    princip_window.addstr(6,27,"Version du Kernel :",curses.color_pair(1))
    sys=platform.version()
    princip_window.addstr(8,12,sys)
    princip_window.addstr(17,0,"0 : Retour en arriere :")
    c = princip_window.getch()
    if c == ord("0"):
        princip_window.clear()
        return
    elif c == ord('q') or c == ord('Q'):
        return True
    else:
        aff_kernel_vers(princip_window)
    return False

def sous_menu(princip_window):
    princip_window.clear()
    princip_window.addstr(4, 0,"============================================================================")
    princip_window.addstr(6,25,"1- Info cpu")
    princip_window.addstr(8,25,"2- Infos memoire")
    princip_window.addstr(10,25,"3- Infos disque dur")
    princip_window.addstr(12,25,"0 : Retour en arriere :")
    princip_window.addstr(14, 0,"============================================================================")
    princip_window.refresh()
    # if c == ord('q') or c == ord('Q'):
    #     sys.exit()

def  aff_hardware_infos(princip_window):
    sous_menu(princip_window)
    c = princip_window.getch()
    if c == ord('1'):
        princip_window.clear()
        princip_window.addstr(0,0,"Info cpu: ")
        cpu = os.popen('lscpu')
        cpu1 = cpu.read()
        princip_window.addstr(cpu1)
        # princip_window.addstr(17,0,"0 : Retour en arriere :")
        princip_window.refresh()
        c = princip_window.getch()
        if c == ord('0'):
            aff_hardware_infos(princip_window)
    if c == ord('2'):
        princip_window.clear()
        princip_window.addstr(4,26,"Infos memoire : ",curses.color_pair(1))
        princip_window.addstr(6,0,"")
        free=os.popen('free -t')
        free1=free.read()
        princip_window.addstr(free1)
        princip_window.addstr(17,0,"0 : Retour en arriere :")
        princip_window.refresh()
        c = princip_window.getch()
        if c == ord('0'):
            aff_hardware_infos(princip_window)
    if c == ord('3'):
        princip_window.clear()
        princip_window.addstr(2,23,"Infos disque dur : ",curses.color_pair(1))
        princip_window.addstr(4,0,"")
        disk=os.popen('df -h')
        disk1=disk.read()
        princip_window.addstr(disk1)
        princip_window.addstr(17,0,"0 : Retour en arriere :")
        princip_window.refresh()
        c = princip_window.getch()
        if c == ord('0'):
            aff_hardware_infos(princip_window)
        elif c == ord('q') or c == ord('Q'):
            sys.exit()
    elif c == ord("0"):
        princip_window.clear()
        return
    elif c == ord('q') or c == ord('Q'):
        sys.exit()
    else:
        aff_hardware_infos(princip_window)
