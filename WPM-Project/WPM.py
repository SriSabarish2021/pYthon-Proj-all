import curses
import time

def stdr_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello Welcom to WPM Game!")
    stdscr.addstr("\nPress any key to Continue....")
    stdscr.refresh()
    stdscr.getkey()
    
    # stdscr.getch()    

def typing_txt(stdscr,targettxt,typetxt,wpm):
    
    stdscr.addstr(targettxt)
    stdscr.addstr(1,0,f"Your WPM is = {wpm}")
    for i,char in enumerate(typetxt):
        
        color=curses.color_pair(1)
        if char!=targettxt[i]:
            color= curses.color_pair(2)
        stdscr.addstr(0,i,char,color)


def write_txt(stdscr):
    text="Hello World this is sri sabarish from erode."
    typed_txt=[]
    wpm=0
    strt_time=time.time()
    stdscr.nodelay(True)
    while True:
        elapsed_time=max(time.time()-strt_time,1)
        wpm=round((len(typed_txt)/(elapsed_time/60))/5)
        stdscr.clear()
        typing_txt(stdscr,text,typed_txt,wpm)
        stdscr.refresh()

        if "".join(typed_txt) == text:
            stdscr.nodelay(False)
            break

        try:
            key_values=stdscr.getkey()
        except:
            continue
        if ord(key_values)==27:
            break
    
        if key_values in ("KEY_BACKSPACE",'\b','\x7f'):
            if len(typed_txt)>0:
                typed_txt.pop()

        elif len(text)>len(typed_txt):
            typed_txt.append(key_values)

        





    
def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    
    stdr_screen(stdscr)
    write_txt(stdscr)
    stdscr.addstr(1,0,"Game Has been ended thank you for playing")
    stdscr.getkey()

curses.wrapper(main)
