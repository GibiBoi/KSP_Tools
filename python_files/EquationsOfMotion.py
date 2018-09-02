from tkinter import *
from tkinter import messagebox
from math import sqrt, fabs


root = Tk()
root.geometry("360x300")
root.configure(background="#3C3F41")
root.iconbitmap("guifileicon.ico")
root.title("Equations Of Motion Calculator")
entryOne = StringVar(root, "u a")
entryTwo = StringVar(root, "u a s")
entryThree = StringVar(root, "u a s")
entryFour = StringVar(root, "u t a")


def maxheight():
    values = list(map(float,entryOne.get().split()))
    ans = -(values[0]**2) / (2 * values[1])
    messagebox.showinfo("Answer", ans)


def tthg():
    values = list(map(float, entryTwo.get().split()))
    ans1 = (values[0]**2 + (2 * values[1] * values[2]))
    if ans1 >= 0:
        ans1 = sqrt(ans1)
    else:
        ans1 = -sqrt(fabs(ans1))
    ans = (ans1 - values[0]) / values[1]
    messagebox.showinfo("Answer", ans)


def vthg():
    values = list(map(float, entryThree.get().split()))
    ans = (values[0]**2 + (2 * values[1] * values[2]))
    if ans >= 0:
        ans = sqrt(ans)
    else:
        ans = -sqrt(fabs(ans))
    messagebox.showinfo("Answer", ans)


def distancefallen():
    values = list(map(float, entryFour.get().split()))
    ans = (values[0] * values[1]) + (0.5 * values[2] * values[1]**2)
    messagebox.showinfo("Answer", ans)


def resetentries():
    entryOne.set("u a")
    entryTwo.set("u a s")
    entryThree.set("u a s")
    entryFour.set("u t a")


def helpwindow():
    messagebox.showinfo("Help", "Values:\nu = Initial velocity\nv = Velocity\na = Acceleration (If gravity, use negative)\nt = Time\ns = Displacement\n\nAll units SI")


labelone = Label(root, text="Max Height", bg="#3C3F41", fg="red").pack()
entryboxone = Entry(root, textvariable=entryOne)
entryboxone.bind('<Return>', (lambda event: maxheight()))
entryboxone.pack()
buttonone = Button(root, text="Calculate", command=maxheight).pack()


labeltwo = Label(root, text="Time To Hit Ground", bg="#3C3F41", fg="red").pack()
entryboxtwo = Entry(root, textvariable=entryTwo)
entryboxtwo.bind('<Return>', (lambda event: tthg()))
entryboxtwo.pack()
buttontwo = Button(root, text="Calculate", command=tthg).pack()


labelthree = Label(root, text="Velocity To Hit Ground", bg="#3C3F41", fg="red").pack()
entryboxthree = Entry(root, textvariable=entryThree)
entryboxthree.bind('<Return>', (lambda event: vthg()))
entryboxthree.pack()
buttonthree = Button(root, text="Calculate", command=vthg).pack()


labelfour = Label(root, text="Distance Fallen", bg="#3C3F41", fg="red").pack()
entryboxfour = Entry(root, textvariable=entryFour)
entryboxfour.bind('<Return>', (lambda event: distancefallen()))
entryboxfour.pack()
buttonfour = Button(root, text="Calculate", command=distancefallen).pack()


"""im = PhotoImage(file="C:/Users/Lewis/Desktop/A folder to work on/scene00217.gif")
labImage1 = Label(root, image=im)
labImage1.pack()"""


menubar = Menu(root)
menubar.add_command(label="Help!", command=helpwindow)
menubar.add_command(label="Reset Entries", command=resetentries)


root.config(menu=menubar)
mainloop()
