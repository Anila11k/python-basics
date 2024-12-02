from tkinter import*
root=Tk()

m1=Menubutton(root,text="FRIENDS")
m1.menu=Menu(m1)
m1["menu"]=m1.menu
var1=IntVar()
var2=IntVar()
var3=IntVar()
m1.menu.add_checkbutton(label="ANILA",variable=var1,onvalue=1,offvalue=0)
m1.menu.add_radiobutton(label="ABHIJITH",variable=var2)
m1.menu.add_radiobutton(label="NONI",variable=var3)

root.geometry("300x220")
m1.pack()
m1.mainloop()



