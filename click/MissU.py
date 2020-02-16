import tkinter as tk
import random
import time
import os
import tkinter.font as tkFont 

# IMGPATH1 = "C:/Users/"+os.getlogin()+"/Desktop/img/cat.gif"
# IMGPATH2 = "C:/Users/"+os.getlogin()+"/Desktop/img/dog.gif"
IMGPATH1 = "img/cat.gif"
IMGPATH2 = "img/dog.gif"
TITLE = "Missing You"
QUES = "我想你了，你有想我吗？"
YES = "有"
NO = "没有"
YESREPLY = "\n(*/ω\*)\n(づ￣ 3￣)づ ❤ ❤ ❤\n真乖~~~"
NOREPLY = "..." 
# size
SPACE = 100
# window
WINWIDTH = 800
WINHEIGHT = 600
WINX = 400
WINY = 100
TOPWIDTH = 200
TOPHEIGHT = 100
TOPWIDTH1 = 400
TOPHEIGHT1 = 400
# button place
BUTTONWIDTH = 100
BUTTONHEIGHT = 30
LEFTX = 180 
by = 550
bx = 500
changed=False


# new class TK can't be closed
class NewTk(tk.Tk):
    def destroy(self):
        pass


# new window
win = NewTk()
win_loc = "{}x{}+{}+{}".format(WINWIDTH,WINHEIGHT,WINX,WINY)
win.geometry(win_loc)
win.title(TITLE)
frame = tk.Frame(win, width = WINWIDTH, height = WINHEIGHT)
frame.pack()


# font setting ,after new window, or will be wrong
quesft = tkFont.Font(family = "微软雅黑",size = 14, weight = tkFont.BOLD)
ansft = tkFont.Font(family = "微软雅黑",size = 14, weight = tkFont.BOLD)

# question
q = tk.Label(frame,text = QUES,font = quesft)
q.place(x = LEFTX,y = 20)

# picture
photo = tk.PhotoImage(file = IMGPATH1)
imgLabel = tk.Label(frame,image = photo)
imgLabel.place(x = LEFTX,y = 80)


# click yes function
def clickyes():
    top = tk.Toplevel()
    # pop-up window in middle
    top_x=int(WINX+WINWIDTH/2-TOPWIDTH/2)
    top_y=int(WINY+WINHEIGHT/2-TOPHEIGHT/2)
    top_loc="{}x{}+{}+{}".format(TOPWIDTH,TOPHEIGHT,top_x,top_y)
    top.geometry(top_loc)
    # add text
    tk.Label(top,text = YESREPLY).pack()
    win.update()
    time.sleep(2)
    
    top = tk.Toplevel()
    # pop-up window in middle
    top_x=int(WINX+WINWIDTH/2-TOPWIDTH1/2)
    top_y=int(WINY+WINHEIGHT/2-TOPHEIGHT1/2)
    top_loc="{}x{}+{}+{}".format(TOPWIDTH1,TOPHEIGHT1,top_x,top_y)
    top.geometry(top_loc)
    # add img
    photo = tk.PhotoImage(file = IMGPATH2)
    tk.Label(top,image = photo).pack()
    win.update()
    time.sleep(2)
    # close all windows
    # exit()
    win.quit()

# button
b0 = tk.Button(frame,text = YES,font = ansft,command = clickyes)
b0.place(x = LEFTX,y = by,width = BUTTONWIDTH,height = BUTTONHEIGHT)

b1 = tk.Button(frame,text = NO,font = ansft)
b1.place(x = bx,y = by,width = BUTTONWIDTH,height = BUTTONHEIGHT)


# click no function
def clickno(event):
    global changed
    if changed:
        b1.place(x = bx,y = by)
        b0.place(x = LEFTX,y = by)
        changed = False
    else:
        b0.place(x = bx,y = by)
        b1.place(x = LEFTX,y = by)
        changed = True

b1.bind("<Motion>",clickno)

win.mainloop()

# Reference：https://github.com/BigShuang/liaomei
# package：pyinstaller -F -w xxx.py