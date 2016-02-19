import psutil, os, signal
import subprocess
from subprocess import check_output
import time

def get_proc_list():
    print("\033[H\033[J")
    print("\033[31mListe des processus : \033[0m\n")
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

def process_info(process_name):
    exist = process_exist(process_name)
    if exist == False:
        print "Process is not running"
        time.sleep(2)
        return False
    else:
        pid = get_pid(process_name)
        pid = "".join(pid)
        array = info_from_pid(pid)
        commande = command(pid)
        print array[0]
        print array[4]
        print array[5]
        print "Command:",commande[0]
        print array[1]
        return True

def simple_kill(process_name):
    exist = process_exist(process_name)
    pid = get_pid(process_name)
    pid = "".join(pid)
    if exist == False:
        print "Process is not running"
    else:
        os.kill(int(pid), signal.SIGTERM)
        try:
            os.kill(int(pid), 0)
            pass
        except Exception, e:
            raise e
            print "Error to kill , try forced mode"


def forced_kill(process_name):
    exist = process_exist(process_name)
    pid = get_pid(process_name)
    pid = "".join(pid)
    if exist == False:
        print "Process is not running"
    else:
        os.kill(int(pid), signal.SIGKILL)
        try:
            os.kill(int(pid), 0)
        except OSError as ex:
            print "error"


def runproc():
    print("\033[H\033[J")
    print("Process :")
    c=raw_input(">")
    os.system(c)
    time.sleep(1)
