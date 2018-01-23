from tkinter import *
from classes.mainwindow import *

def main():
    tk = Tk()
    tk.title("Generator świadectw")
    tk.geometry("500x{0}".format(tk.winfo_screenwidth(), tk.winfo_screenheight()))
    frame = Frame(tk)
    frame.grid()
    window = MainWindow(tk)
    tk.mainloop()


main()
