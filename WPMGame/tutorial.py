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
    current_text = []

    while True:
        stdscr.clear()
        stdscr.addstr(target_test)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getkey()

        #check if that is escape key ASCII  "a" = 97 "A" = 65 ....
        if ord(key) == 27:
            break
        
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
                current_text.append(key)
                



    

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)