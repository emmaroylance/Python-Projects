from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.minsize(725,275)
        self.master.maxsize(725,275)
        self.master.title("Ask Directory")
        self.master.config(bg='#F0F0F0')

        self.btnBrowse1 = Button(self.master, text="Browse...", width=16, height=2, font=("Helvetica", 10), fg='black', bg='#F0F0F0', command=self.browse)
        self.btnBrowse1.grid(row=0, column=0, pady=(70, 0), padx=(25, 0))


    def browse(self):
        path = filedialog.askdirectory()
        self.txtFilePath1 = Label(self.master, text="path: {}".format(path), font=("Helvetica", 8), fg='black', width=40)
        self.txtFilePath1.grid(row=0, column=1, padx=(40,0), pady=(60,0))




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

