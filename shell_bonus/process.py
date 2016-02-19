import psutil, os, signal
import subprocess
from subprocess import check_output
import time
import curses

def get_proc_list(princip_window):
    princip_window.clear()
    princip_window.addstr("\033[H\033[J")
    princip_window.addstr("\033[31mListe des processus : \033[0m\n")
    processoutput = subprocess.Popen(['ps', '-U', '0'], stdout=subprocess.PIPE)
    out, donnees = processoutput.communicate()
    print(out)
    print "0 : Retour en arriere :"
    c=raw_input(">")
    if c == "0":
        return
    else:
        print "Command not found"
        time.sleep(2)

def process_exist(process_name):
	tmp = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE).communicate()[0]
	proccount = tmp.count(process_name)

	if proccount > 0:
	    return True
	else:
		return False

def process_exists(process_name):
	tmp = subprocess.Popen(['ps', ''], stdout=subprocess.PIPE).communicate()[0]
	proccount = tmp.count(process_name)

	if proccount > 0:
	    return True
	else:
		return False

def get_pid(process_name):
    array = []
    processoutput = subprocess.Popen(['pgrep', process_name], stdout=subprocess.PIPE)
    out, donnees = processoutput.communicate()
    i = 0
    j = 0
    for line in out:
        if line == "\n":
            return array
        array.append(line)
        i=i+1

def info_from_pid(pid):
    array = []
    with open(os.path.join('/proc/', pid, 'status'), 'r') as pidfile:
    	lignes = pidfile.readlines()
    	i = 0
    	for line in lignes:
    		array.append(line)
    		i=i+1
    	return array

def command(pid):
	array = []
	with open(os.path.join('/proc/', pid, 'comm'), 'r') as pidfile:
		lignes = pidfile.readlines()
		for line in lignes:
			array.append(line)
	return array

def process_info(princip_window, my_str):
    exist = process_exist(my_str)
    if exist == False:
        princip_window.clear()
        princip_window.addstr(8,20,"Process is not running",curses.color_pair(1))
        princip_window.refresh()
        time.sleep(2)
        return False
    else:
        pid = get_pid(my_str)
        pid = "".join(pid)
        array = info_from_pid(pid)
        commande = command(pid)
        var = "".join(array[0])
        var1 = "".join(array[4])
        var2 = "".join(array[5])
        var3 = "".join(array[1])
        princip_window.addstr(1,22,var)
        princip_window.addstr(2,22,var1)
        princip_window.addstr(3,22,var2)
        princip_window.addstr(4,22,var)
        princip_window.addstr(5,22,var3)
        princip_window.refresh()
        return True

def simple_kill(princip_window, process_name):
    exist = process_exist(process_name)
    pid = get_pid(process_name)
    pid = "".join(pid)
    if exist == False:
        princip_window.clear()
        princip_window.addstr(8,20,"Process is not running",curses.color_pair(1))
        time.sleep(2)
    else:
        os.kill(int(pid), signal.SIGTERM)
        princip_window.clear()
        princip_window.addstr(8,20,"Process is stopped",curses.color_pair(1))
        time.sleep(2)
        princip_window.clear()
        try:
            os.kill(int(pid), 0)
            pass
        except Exception, e:
            pass


def forced_kill(princip_window, process_name):
    exist = process_exist(process_name)
    pid = get_pid(process_name)
    pid = "".join(pid)
    if exist == False:
        princip_window.clear()
        princip_window.addstr(8,20,"Process is not running",curses.color_pair(1))
        time.sleep(2)
    else:
        os.kill(int(pid), signal.SIGKILL)
        princip_window.clear()
        princip_window.addstr(8,20,"Process is stopped",curses.color_pair(1))
        time.sleep(2)
        princip_window.clear()
        try:
            os.kill(int(pid), 0)
        except OSError as ex:
            pass

def runproc(princip_window):
    princip_window.clear()
    curses.echo()
    curses.curs_set(1)
    princip_window.addstr(8,25,"Process :",curses.color_pair(1))
    mystr = princip_window.getstr()
    os.system(mystr)
    time.sleep(2)
    curses.noecho()
    curses.curs_set(0)
    princip_window.clear()
    princip_window.refresh()
