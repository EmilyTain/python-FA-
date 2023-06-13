import tkinter
from tkinter import*

emily = tkinter.Tk()
emily.title('Automatic Username')
emily.minsize(height=200,width=300)

def combine():
    firstname = str(firstentry.get())
    secondname = str(secondentry.get())
    result = firstname + secondname
    thirdentry.insert(0,result)

def clear():
    firstentry.delete(0,END)
    secondentry.delete(0,END)
    thirdentry.delete(0,END)

def exit():
    emily.destroy()

labelf = tkinter.LabelFrame(emily, text='Username Suggestion', font=('Arial',12))
labelf.grid(column=0,row=0,padx=100,pady=100)

firstlabel = tkinter.Label(labelf, text='First Name :', font=('Arial',10))
firstlabel.grid(column=0, row=0)
firstentry = tkinter.Entry(labelf,bd=5)
firstentry.grid(column=1,row=0)

seclabel = tkinter.Label(labelf, text='Second Name :', font=('Arial',10))
seclabel.grid(column=0, row=1)
secondentry = tkinter.Entry(labelf,bd=5)
secondentry.grid(column=1,row=1)

thirdlabel = tkinter.Label(labelf, text='Suggested :', font=('Arial',10))
thirdlabel.grid(column=0, row=2)
thirdentry = tkinter.Entry(labelf,bd=5)
thirdentry.grid(column=1,row=2)

gobutton = Button(labelf,text='Combine', width=8, height=1, font=('Arial',12), command=combine)
gobutton.grid(column=1,row=3)

gobutton = Button(labelf,text='Clear', width=8, height=1, font=('Arial',12), command=clear)
gobutton.grid(column=2,row=3)

gobutton = Button(text='Exit', width=8, height=1, font=('Arial',12), command=exit)
gobutton.grid(column=3,row=3)

emily.mainloop()


