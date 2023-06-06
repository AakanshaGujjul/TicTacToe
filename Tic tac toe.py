
from tkinter import *
from tkinter import messagebox

r=Tk()
r.title('Tic tac toe')

messagebox.askquestion('Question','Do you want to start?')

count=0
clicked=True
winner=False

def tiegame():
    if count==9 and winner==False:
        messagebox.showinfo('Winner','It was a tied game')

def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def check():
    
    global winner
    if b1['text']=='X' and b2['text']=='X' and b3['text']=='X':
        winner=True
        b1.config(bg="yellow")
        b2.config(bg="yellow")
 
        b3.config(bg="yellow")
        messagebox.showinfo('Winner','X won the match')
        disable()
        
    elif b1['text']=='X' and b4['text']=='X' and b7['text']=='X':
        winner=True
        b1.config(bg="yellow")
        b4.config(bg="yellow")

        b7.config(bg="yellow")
        messagebox.showinfo('Winner','X won the match')
        disable()
    elif b8['text']=='X' and b4['text']=='X' and b6['text']=='X':
        winner=True
        b8.config(bg="yellow")
        b4.config(bg="yellow")

        b6.config(bg="yellow")
        messagebox.showinfo('Winner','X won the match')
        disable()
        
    elif b9['text']=='X' and b5['text']=='X' and b7['text']=='X':
        winner=True
        b9.config(bg="yellow")
        b5.config(bg="yellow")

        b7.config(bg="yellow")
        messagebox.showinfo('Winner','X won the match')
        disable()
        
    elif b1['text']=='X' and b8['text']=='X' and b9['text']=='X':
        winner=True
        b1.config(bg="yellow")
        b8.config(bg="yellow")

        b9.config(bg="yellow")
        messagebox.showinfo('Winner','X won the match')
        disable()
        
    elif b9['text']=='X' and b4['text']=='X' and b3['text']=='X':
        winner=True
        b9.config(bg="yellow")
        b4.config(bg="yellow")

        b3.config(bg="yellow")
        messagebox.showinfo('Winner','X won the match')
        disable()

########IF STATEMENT FOR O

    if b1['text']=='O' and b2['text']=='O' and b3['text']=='O':
        winner=True
        b1.config(bg="yellow")
        b2.config(bg="yellow")

        b3.config(bg="yellow")
        messagebox.showinfo('Winner','O won the match')
        
    elif b1['text']=='O' and b4['text']=='O' and b7['text']=='O':
        winner=True
        b1.config(bg="yellow")
        b4.config(bg="yellow")

        b7.config(bg="yellow")
        messagebox.showinfo('Winner','O won the match')
        disable()
        
    elif b2['text']=='O' and b4['text']=='O' and b5['text']=='O':
        winner=True
        b2.config(bg="yellow")
        b4.config(bg="yellow")
        b5.config(bg="yellow")
        messagebox.showinfo('Winner','O won the match')
        disable()
        
    elif b3['text']=='O' and b6['text']=='O' and b7['text']=='O':
        winner=True
        b3.config(bg="yellow")
        b6.config(bg="yellow")

        b7.config(bg="yellow")
        messagebox.showinfo('Winner','O won the match')
        disable()
        
    elif b8['text']=='O' and b4['text']=='O' and b6['text']=='O':
        winner=True
        b8.config(bg="yellow")
        b4.config(bg="yellow")

        b6.config(bg="yellow")
        messagebox.showinfo('Winner','O won the match')
        disable()
        
    elif b9['text']=='O' and b5['text']=='O' and b7['text']=='O':
        winner=True
        b9.config(bg="yellow")
        b5.config(bg="yellow")

        b7.config(bg="yellow")
        messagebox.showinfo('Winner','O won the match')
        disable()
        
    elif b1['text']=='O' and b8['text']=='O' and b9['text']=='O':
        winner=True
        b1.config(bg="yellow")
        b8.config(bg="yellow")

        b9.config(bg="yellow")
        messagebox.showinfo('Winner','O won the match')
        disable()
        
    elif b9['text']=='O' and b4['text']=='O' and b3['text']=='O':
        winner=True
        b9.config(bg="yellow")
        b4.config(bg="yellow")

        b3.config(bg="yellow")
        messagebox.showinfo('Winner','O won the match')
        disable()
def b_click(b):
    global count,clicked


    if b['text']==' ' and clicked==True:
        b['text']='X'
        clicked=False
        count+=1
        check()
        tiegame()

    elif b['text']==' ' and clicked==False:
        b['text']='O'
        clicked=True
        count+=1
        check()
        tiegame()

    else:
        messagebox.showerror('Error','You cannot press any occupied button')

        
        
b1=Button(r,text=' ', width=20,height=10,command=lambda:b_click(b1))
b1.grid(row=0,column=0)

b2=Button(r,text=' ', width=20,height=10,command=lambda:b_click(b2))
b2.grid(row=1,column=0)

b3=Button(r,text=' ', width=20,height=10,command=lambda:b_click(b3))
b3.grid(row=2,column=0)

b4=Button(r,text=' ', width=20,height=10,command=lambda:b_click(b4))
b4.grid(row=1,column=1)

b5=Button(r,text=' ', width=20,height=10,command=lambda:b_click(b5))
b5.grid(row=1,column=2)

b6=Button(r,text=' ', width=20,height=10,command=lambda:b_click(b6))
b6.grid(row=2,column=1)

b7=Button(r,text=' ', width=20,height=10,command=lambda:b_click(b7))
b7.grid(row=2,column=2)

b8=Button(r,text=' ', width=20,height=10,command=lambda:b_click(b8))
b8.grid(row=0,column=1)

b9=Button(r,text=' ', width=20,height=10,command=lambda:b_click(b9))
b9.grid(row=0,column=2)


r.mainloop()
