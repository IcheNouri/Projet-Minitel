
from datetime import timedelta
import platform
import os
import time

def aff_sys_vers():
    print("\033[H\033[J")
    print("\033[31mVersion du systeme d'exploitation : \033[0m\n")
    sys=platform.release()
    print(sys)
    print "\n0 : Retour en arriere:"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "\033[31mCommand not found\033[0m"
        time.sleep(2)


def aff_time():
    print("\033[H\033[J")
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
    print("\033[31mUptime : \033[0m\n")
    print(uptime_string)
    print "\n0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "\033[31mCommand not found\033[0m"
        time.sleep(2)


def aff_kernel_vers():
    print("\033[H\033[J")
    print("\033[31mVersion du Kernel : \033[0m\n")
    sys=platform.version()
    print(sys)
    print "\n0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "\033[31mCommand not found\033[0m"
        time.sleep(2)

def  aff_hardware_infos():
    print("\033[H\033[J")
    print("\033[31mInfos cpu : \033[0m\n")
    cpu=os.popen('lscpu')
    cpu1=cpu.read()
    print(cpu1),"\n"
    print("\033[31mInfos memoire : \033[0m\n")
    free=os.popen('free -t')
    free1=free.read()
    print(free1)
    print("\033[31mInfos disque dur : \033[0m\n")
    disk=os.popen('df -h')
    disk1=disk.read()
    print(disk1)
    print "0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "\033[31mCommand not found\033[0m"
        time.sleep(2)
