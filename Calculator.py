from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.geometry("250x310")
root.title("Calculator GUI")
root.resizable(False,False)

def click(event):
    
    if (scvalue.get() == "0"):
        scvalue.set("")
        screen.update()
    b=event.widget
    text=b['text']
    ex = screen.get()
    
    if text == '=':
        try:
            ans = eval(ex)
            screen.delete(0,END)
            screen.insert(0,ans)

        except Exception as e:
            print("Error...")
            showerror("Error",e)
            screen.delete(0,END)
        return;

    if text == 'CE':
        screen.delete(0,END)
        screen.insert(0,0)
        return;
        
    screen.insert(END,text)

def clear(event):
    
    b=event.widget
    text=b['text']
    ex = screen.get()
    
    if (scvalue.get() == "0" or len(scvalue.get()) == 1):
            scvalue.set("0")
            screen.update()
            
    elif (len(scvalue.get()) > 1):
        ex=ex[0:len(ex)-1]
        screen.delete(0,END)
        screen.insert(0,ex)

scvalue = StringVar()
scvalue.set("0")
screen = Entry(root,bg="light cyan",textvar=scvalue,font="lucida 15 bold")
screen.pack(fill=X,ipadx=15,pady=15,padx=10)

fb1 = Frame(root,bg="Light Gray")

bc = Button(fb1,text="CE",width=3,pady=8,padx=8,bg="gold2",font="lucida 10 bold",)
bc.bind('<Button-1>',click)

bdiv = Button(fb1,text="/",padx=12,bg="gold2",font="lucida 15 bold")
bdiv.bind('<Button-1>',click)

bmul = Button(fb1,text="*",padx=12,bg="gold2",font="lucida 15 bold")
bmul.bind('<Button-1>',click)

bsub = Button(fb1,text="-",padx=13,bg="gold2",font="lucida 15 bold")
bsub.bind('<Button-1>',click)

fb1.pack()
bc.pack(padx=5,pady=3,side="left")
bdiv.pack(padx=5,pady=3,side="left")
bmul.pack(padx=5,pady=3,side="left")
bsub.pack(padx=5,pady=3,side="left")

f1 = Frame(root,bg="light gray")

b7 = Button(f1,text="7",padx=10.4,bg="wheat1",font="lucida 15 bold")
b7.bind('<Button-1>',click)

b8 = Button(f1,text="8",padx=10,bg="wheat1",font="lucida 15 bold")
b8.bind('<Button-1>',click)

b9 = Button(f1,text="9",padx=10,bg="wheat1",font="lucida 15 bold")
b9.bind('<Button-1>',click)

badd = Button(f1,text="+",padx=10.5,bg="gold2",font="lucida 15 bold")
badd.bind('<Button-1>',click)

f1.pack()
b7.pack(padx=5,pady=3,side="left")
b8.pack(padx=5,pady=3,side="left")
b9.pack(padx=5,pady=3,side="left")
badd.pack(padx=5,pady=3,side="left")

f2 = Frame(root,bg="light gray")

b4 = Button(f2,text="4",padx=10,bg="wheat1",font="lucida 15 bold")
b4.bind('<Button-1>',click)

b5 = Button(f2,text="5",padx=10,bg="wheat1",font="lucida 15 bold")
b5.bind('<Button-1>',click)

b6 = Button(f2,text="6",padx=10,bg="wheat1",font="lucida 15 bold")
b6.bind('<Button-1>',click)

bmod = Button(f2,text="%",padx=8,bg="gold2",font="lucida 15 bold")
bmod.bind('<Button-1>',click)

f2.pack()
b4.pack(padx=5,pady=3,side="left")
b5.pack(padx=5,pady=3,side="left")
b6.pack(padx=5,pady=3,side="left")
bmod.pack(padx=5,pady=3,side="left")

f3 = Frame(root,bg="light gray")

b1 = Button(f3,text="1",padx=10,bg="wheat1",font="lucida 15 bold")
b1.bind('<Button-1>',click)

b2 = Button(f3,text="2",padx=10,bg="wheat1",font="lucida 15 bold")
b2.bind('<Button-1>',click)

b3 = Button(f3,text="3",padx=10,bg="wheat1",font="lucida 15 bold")
b3.bind('<Button-1>',click)

beq = Button(f3,text="=",padx=10,bg="gold2",font="lucida 15 bold")
beq.bind('<Button-1>',click)

f3.pack()
b1.pack(padx=5,pady=3,side="left")
b2.pack(padx=5,pady=3,side="left")
b3.pack(padx=5,pady=3,side="left")
beq.pack(padx=5,pady=3,side="left")

f4 = Frame(root,bg="light gray")

bcl = Button(f4,text="<--",padx=33,bg="gold2",font="lucida 15 bold")
bcl.bind('<Button-1>',clear)

b0 = Button(f4,text="0",padx=10,bg="gold2",font="lucida 15 bold")
b0.bind('<Button-1>',click)

bdec = Button(f4,text=".",padx=13,bg="gold2",font="lucida 15 bold")
bdec.bind('<Button-1>',click)

f4.pack()
bcl.pack(padx=5,pady=3,side="left")
b0.pack(padx=5,pady=3,side="left")
bdec.pack(padx=5,pady=3,side="left")


root.mainloop()
