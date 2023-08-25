import curses 
from curses import wrapper 





def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_test = "Hello world this is some test tesxt for this app!"
    current_test = []

    while True:
        key = stdscr.getkey()

        #check if that is escape key ASCII  "a" = 97 "A" = 65 ....
        if ord(key) == 27:
            break

        current_test.append(key)

        stdscr.clear()
        stdscr.addstr(target_test)

        for char in current_test:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()
    

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)