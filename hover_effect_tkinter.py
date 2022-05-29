from tkinter import *
w=Tk()
w.geometry('500x500')


def bttn(x,y,text,ecolor,lcolor,cmd):
    def on_entera(e):
        myButton1['background'] = ecolor #ffcc66
        myButton1['foreground']= lcolor  #000d33

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground']= ecolor

    myButton1 = Button(w,text=text,
                   width=42,
                   height=2,
                   fg=ecolor,
                   border=0,
                   bg=lcolor,
                   activeforeground=lcolor,
                   activebackground=ecolor,
                       command=cmd)
                  
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)

def cmd():
    print('ajsdf')
def cmd1():
    print('lol')
bttn(0,0,'A C E R','#ffcc66','#141414',cmd)
bttn(0,37,'A P P L E','#25dae9','#141414',cmd1)
bttn(0,74,'D E L L','#ffcc66','#141414',cmd1)
bttn(0,110,"A S U S" ,'#25dae9' , '#141414',cmd1)

'''
def bttn(x,y,text,ecolor,lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor #ffcc66
        myButton1['foreground']= lcolor  #000d33

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground']= ecolor

    myButton1 = Button(w,
                       font=('Century Gothic',20),
                       text=text,
                #   width=42,
                #   height=2,
                       fg=ecolor,
                       border=0,
                       bg=lcolor,
                       activeforeground=lcolor,
                       activebackground=ecolor,
                       padx=4
                       )
                  
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)


bttn(0,0,'A C E R','#ffcc66','#141414')

'''


w.mainloop()
