# from tkinter import*
# from tkinter import ttk
# root=Tk() 

# pw=ttk.PanedWindow(root,orient=HORIZONTAL)
# pw.pack(fill=BOTH,expand=True)

# frame1=ttk.Frame(pw,relief=SUNKEN)
# frame2=ttk.Frame(pw,relief=SUNKEN)

# pw.add(frame1,weight=1)
# pw.add(frame2,weight=3)

# root.geometry("400x200")
# root.title("pythonLobby.com")
# root.mainloop()




from tkinter import*
from tkinter import ttk
root=Tk() 

pw=ttk.PanedWindow(root,orient=HORIZONTAL)
pw.pack(fill=BOTH,expand=True)

frame1=ttk.Frame(pw,relief=SUNKEN)
frame2=ttk.Frame(pw,relief=SUNKEN)

pw.add(frame1,weight=1)
pw.add(frame2,weight=3)

root.geometry("50x100")
root.title("pythonLobby.com")
root.mainloop()

# from tkinter import*
# from tkinter import ttk

# root=Tk()

# pw=title.panedwindow(root,orient=HORIZONTAL)
# pw.pack(fill=BOTH,expand=True)

# frame1=ttk.Frame(pw,relief=SUNKEN)
# frame2=ttk.Frame(pw,relief=SUNKEN)


