from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.minsize(725,275)
        self.master.maxsize(725,275)
        self.master.title("Check files")
        self.master.config(bg='#F0F0F0')


        self.varFile1 = StringVar()
        self.varFile2 = StringVar()


        self.btnBrowse1 = Button(self.master, text="Browse...", width=16, height=2, font=("Helvetica", 10), fg='black', bg='#F0F0F0')
        self.btnBrowse1.grid(row=0, column=0, pady=(70,0), padx=(25,0))
        self.btnBrowse2 = Button(self.master, text="Browse...", width=16, height=2, font=("Helvetica", 10), fg='black', bg='#F0F0F0')
        self.btnBrowse2.grid(row=1, column=0, pady=(20, 0), padx=(25,0))

        self.txtFile1 = Entry(self.master, text='', font=("Helvetica", 16), fg='black', width=40)
        self.txtFile1.grid(row=0, column=1, padx=(40,0), pady=(60,0))
        self.txtFile2 = Entry(self.master, text='', font=("Helvetica", 16), fg='black', width=40)
        self.txtFile2.grid(row=1, column=1, padx=(40,0), pady=(15,0))

        self.btnCheck = Button(self.master, text="Check for files...", width=16, height=3, font=("Helvetica", 10), fg='black', bg='#F0F0F0')
        self.btnCheck.grid(row=2, column=0, pady=(20,0), padx=(25,0))

        self.btnClose = Button(self.master, text="Close Program", width=15, height=3, font=("Helvetica", 10), fg='black', bg='#F0F0F0')
        self.btnClose.grid(row=2, column=1, pady=(20,0), padx=(395,0))





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()