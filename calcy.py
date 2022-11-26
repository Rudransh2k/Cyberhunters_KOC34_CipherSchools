from tkinter import *
import math

def click(value):
    ex = entryfld.get()
    ans=''
    if value=="del":
        ans=ex[0:len(ex)-1]
    elif value=="C":
        ex=entryfld.delete(0,END)
    elif value=="√2":
        ans=math.sqrt(eval(ex))
    elif value=="sin":
        ans=math.sin(math.radians(eval(ex)))
    elif value=="cos":
        ans=math.cos(math.radians(eval(ex)))
    elif value=="tan":
        ans=math.tan(math.radians(eval(ex)))
    elif value=="->deg":
        ans=math.degrees(eval(ex))
    elif value=="->rad":
        ans=math.radians(eval(ex))
    elif value=="a\u02b8":
        entryfld.insert(END,'**')
        return
    elif value=="+":
        entryfld.insert(END,'+')
        return

    elif value=="-":
        entryfld.insert(END,'-')
        return

    elif value=="/":
        entryfld.insert(END,'/')
        return

    elif value=="X":
        entryfld.insert(END,'*')
        return

    elif value=="%":
        entryfld.insert(END,'%')
        return

    elif value=="=":
        ans=eval(ex)
    elif value=="log":
        ans=math.log(eval(ex))
    else:
        entryfld.insert(END,value)
        return
    entryfld.delete(0,END)
    entryfld.insert(0,ans)


root=Tk()
root.title("Scientific Calculator")
root.config(bg='grey20')
root.geometry('660x575')

entryfld=Entry(root,font=('arial',20,'bold')
               ,bg='gray30',fg='black',bd=5,relief=SUNKEN,width=30)
entryfld.grid(row=0,column=0,columnspan=5)



button_list=["C","del","+","-","X",
             "1","2","3","sin","/",
             "4","5","6","cos","tan",
             "7","8","9","->deg","->rad",
             ".","0","=",
             "%","√2","log","00","a\u02b8","(",")"]

rowval=1
colval=0

for i in button_list:

    button=Button(root,width=6,height=2,bd=2,relief=RAISED,text=i,bg='grey4',fg='white',
              font=('arial',18,'bold'),
                  command=lambda button=i: click(button))
    button.grid(row=rowval,column=colval)
    colval+=1

    if colval>4:
        rowval+=1
        colval=0
root.mainloop()