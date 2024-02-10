
from tkinter import *
from tkinter import messagebox


def Save():
    print("Pw Saved") 

def Generate():
    print("Generated")
    return "samplePW"
root = Tk()
root.geometry("800x600")
root.resizable(width=0, height=0)
root.title("Password Generator")
root.configure()

pw = Generate()

password_viewer = Frame(root, bg="dark gray", height=580, width=390)
password_viewer.place(x=400, y=10)

Button(root, text="Save", font="Arial 12 bold", height=1, width=6, command=Save).place(x=100, y=200)
Button(root, text="Generate", font="Arial 12 bold", height=1, width=6, command=Generate).place(x=200, y=200)
Label(root, textvariable=pw, text=pw, font="Arial 12", height=1, width=37, bg="dark gray").place(x=10, y=170)
Label(password_viewer, text="SAVED PWS GO HERE", bg="dark gray").pack()
root.mainloop()