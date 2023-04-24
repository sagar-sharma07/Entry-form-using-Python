from tkinter import*

def saveRecord():
    name=n.get()
    phone=p.get()
    email=e.get()
    course=c.get()
    txt=f"\n{name},{phone},{email},{course}"
    f=open("data.txt","a")
    f.write(txt)
    f.close()
    clrRecord()
    lbl["text"]="Record Saved"

def clrRecord():
    n.delete(0,END)
    p.delete(0,END)
    e.delete(0,END)
    c.delete(0,END)

clr="white"
win=Tk()
win.title("Form1")
win.geometry("500x400+200+100")
win.configure(background="white")

#Labels
Label(text="Student Entery Form",font="Times 20").grid(row=0,column=2,pady=15)
Label(text="Student Name",bg=clr,font="Times 14").grid(row=1,column=1,pady=5,padx=20,sticky="nw")
Label(text="Email Id",bg=clr,font="Times 14").grid(row=2,column=1,pady=5,padx=20,sticky="nw")
Label(text="Phone No",bg=clr,font="Times 14").grid(row=3,column=1,pady=5,padx=20,sticky="nw")
Label(text="Course",bg=clr,font="Times 14").grid(row=4,column=1,pady=5,padx=20,sticky="nw")
lbl=Label(bg=clr,font="Times 14")
lbl.grid(row=7,column=1,pady=5,padx=20,sticky="nw")

#Entries
n=Entry(font="Times 12",bd=2,width='30')
n.grid(row=1,column=2)
e=Entry(font="Times 12",bd=2,width='30')
e.grid(row=2,column=2)
p=Entry(font="Times 12",bd=2,width='30')
p.grid(row=3,column=2)
c=Entry(font="Times 12",bd=2,width='30')
c.grid(row=4,column=2)

#Buttons
Button(text="Save Record",bg='Teal',fg="white",pady=5,width=20,command=saveRecord).grid(pady=10,row=5,column=2)
Button(text="Clear Form",bg='Silver',fg="Teal",pady=5,width=20,command=clrRecord).grid(pady=10,row=6,column=2)

win.mainloop()
