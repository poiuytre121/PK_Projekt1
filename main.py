from tkinter import *
from tkinter import messagebox
from classes.mainwindow import *

def main():
    tk = Tk()
    tk.title("Generator świadectw")
    tk.geometry("{0}x{1}+0+0".format(tk.winfo_screenwidth(), tk.winfo_screenheight()))
    frame = Frame(tk)
    frame.grid()
    window = MainWindow(tk)
    tk.mainloop()


main()
