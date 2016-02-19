# #!/usr/bin/env python
from menu import aff_menu1,aff_menu2,aff_menu4,aff_menu3
from infosgeneral import aff_sys_vers,aff_time,aff_kernel_vers,aff_hardware_infos
from infosgeneral2 import file_open_limit,proc_open_limit,list_package
from process import get_proc_list,process_exist,get_pid,process_info,simple_kill,forced_kill
from infosreseau  import aff_ip,aff_interface,aff_nb_paquets,aff_route,aff_ip_forward
import time, os
import curses

stdscr =  curses.initscr()

curses.noecho()
curses.cbreak()
curses.curs_set(0)

if curses.has_colors():
	curses.start_color()

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

stdscr.addstr("RANDOM QUOTES", curses.A_REVERSE)
stdscr.chgat(-1, curses.A_REVERSE)

stdscr.addstr(curses.LINES-1, 0, "Choose option, 'Q' to quit")

# stdscr.chgat(curses.LINES-1,7, 1, curses.A_BOLD | curses.color_pair(2))

stdscr.chgat(curses.LINES-1,16, 1, curses.A_BOLD | curses.color_pair(1))

quote_window = curses.newwin(curses.LINES-2,curses.COLS, 1,0)

quote_text_window = quote_window.subwin(curses.LINES-6,curses.COLS-4, 3,2)
princip_window = quote_text_window.subwin(curses.LINES-6,curses.COLS-4, 3,2)

quote_text_window.addstr(5, 10, "1-Partie1", curses.color_pair(4))
quote_text_window.addstr(8, 10, "2-Partie2", curses.color_pair(4))
quote_text_window.addstr(11, 10, "3-Partie3", curses.color_pair(4))

quote_window.box()

stdscr.noutrefresh()
quote_window.noutrefresh()
princip_window.noutrefresh()

curses.doupdate()

while True:
	c = quote_window.getch()

	if c == ord('1'):
		# quote_text_window.clear()
		aff_hardware_infos(princip_window)
		princip_window.refresh()
		var = quote_window.getch()
		if var == ord('0'):
			princip_window.clear()
			# quote_text_window.addstr("Bienvenu")
			quote_text_window.refresh()
		# quote_text_window.clear()
		# quote_text_window.addstr(get_new_joke())

	elif c == ord('q') or c == ord('Q'):
		break

	stdscr.noutrefresh()
	quote_window.noutrefresh()
	quote_text_window.noutrefresh()
	curses.doupdate()

curses.nocbreak()
curses.echo()
curses.curs_set(1)

curses.endwin()

# import curses, traceback

# def main(stdscr):
#     # Frame the interface area at fixed VT100 size
#     global screen
#     screen = stdscr.subwin(23, 79, 0, 0)
#     screen.box()
#     screen.hline(2, 1, curses.ACS_HLINE, 77)
#     screen.refresh()

#     # Define the topbar menus
#     file_menu = ("File", "file_func()")
#     proxy_menu = ("Proxy Mode", "proxy_func()")
#     doit_menu = ("Do It!", "doit_func()")
#     help_menu = ("Help", "help_func()")
#     exit_menu = ("Exit", "EXIT")
#     # Add the topbar menus to screen object
#     # topbar_menu((file_menu, proxy_menu, doit_menu,
#     #              help_menu, exit_menu))

#     # Enter the topbar menu loop
#     # while topbar_key_handler():
#     #     draw_dict()




# # def file_func():
# # 	s = curses.newwin(5,10,2,1)
# # 	s.box()
# # 	s.addstr(1,2, "I", hotkey_attr)
# # 	s.addstr(1,3, "nput", menu_attr)
# # 	s.addstr(2,2, "O", hotkey_attr)
# # 	s.addstr(2,3, "utput", menu_attr)
# # 	s.addstr(3,2, "T", hotkey_attr)
# # 	s.addstr(3,3, "ype", menu_attr)
# # 	s.addstr(1,2, "", hotkey_attr)
# # 	s.refresh()
# # 	c = s.getch()
# # 	if c in (ord('I'), ord('i'), curses.KEY_ENTER, 10):
# # 	  curses.echo()
# # 	  s.erase()
# # 	  screen.addstr(5,33, " "*43, curses.A_UNDERLINE)
# # 	  cfg_dict['source'] = screen.getstr(5,33)
# # 	  curses.noecho()
# # 	else:
# # 	  curses.beep()
# # 	  s.erase()
# # 	return CONTINUE

# try:
#   # Initialize curses
#   stdscr=curses.initscr()
#   # Turn off echoing of keys, and enter cbreak mode,
#   # where no buffering is performed on keyboard input
#   curses.noecho()
#   curses.cbreak()

#   # In keypad mode, escape sequences for special keys
#   # (like the cursor keys) will be interpreted and
#   # a special value like curses.KEY_LEFT will be returned
#   stdscr.keypad(1)
#   main(stdscr)                    # Enter the main loop
#   # Set everything back to normal
#   stdscr.keypad(0)
#   curses.echo()
#   curses.nocbreak()
#   curses.endwin()                 # Terminate curses
# except:
#   # In event of error, restore terminal to sane state.
#   stdscr.keypad(0)
#   curses.echo()
#   curses.nocbreak()
#   curses.endwin()
#   traceback.print_exc()           # Print the exception



