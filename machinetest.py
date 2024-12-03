from tkinter import*
root =Tk()
root.title("FORM")
root.geometry('300x200')

lbl=Label(root,text="NAME",font=("normal",10), bg=("white"), fg=("black"))

lbl.place(x=10,y=10)

entry=Entry(bg="black",fg="white")
entry.place(x=95,y=10)

lbl=Label(root,text="AGE",font=("normal",10), bg=("white"), fg=("black"))
lbl.place(x=10,y=50)

entry=Entry(bg="black",fg="white")
entry.place(x=95,y=50)

lbl=Label(root,text="PHONE NUMBER",font=("normal",10), bg=("white"), fg=("black"))

lbl.place(x=8,y=90)

entry=Entry(bg="black",fg="white")
entry.place(x=129,y=92)

btn=Button(root,text="log in",font=("normal",8), bg=("BLACK"), fg=("white"))
btn.place(x=120,y=140)






root.mainloop()