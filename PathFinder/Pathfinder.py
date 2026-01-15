import curses
import time
import queue

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(1,0,"Hello welcome to PathFinder")
    stdscr.refresh()
    stdscr.getch()
curses.wrapper(main)