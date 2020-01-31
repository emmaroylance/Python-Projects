import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import sqlite3
import shutil



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.minsize(725,400)
        self.master.maxsize(725,400)
        self.master.title("Check files")
        self.master.config(bg='#F0F0F0')


        self.btnBrowse1 = Button(self.master, text="Select Source Directory", width=20, height=2, font=("Helvetica", 10), fg='black', bg='#F0F0F0', command=self.browse)
        self.btnBrowse1.grid(row=0, column=0, pady=(70, 0), padx=(25, 0))

        self.btnBrowse2 = Button(self.master, text="Select Destination Directory", width=20, height=2, font=("Helvetica", 10), fg='black', bg='#F0F0F0', command=self.browse2)
        self.btnBrowse2.grid(row=1, column=0, pady=(70, 0), padx=(25, 0))

        self.btnTxtCheck = Button(self.master, text="Find .txt files", width=20, height=2, font=("Helvetica", 10), fg='black', bg='#F0F0F0', command=self.findTxt)
        self.btnTxtCheck.grid(row=2, column=0, pady=(70, 0), padx=(25, 0))



    def browse(self):
        self.path1 = filedialog.askdirectory()
        self.txtFilePath1 = Label(self.master, text="path: {}".format(self.path1), font=("Helvetica", 8), fg='black', width=40, bg='white')
        self.txtFilePath1.grid(row=0, column=1, padx=(40,0), pady=(60,0))


    def browse2(self):
        self.path2 = filedialog.askdirectory()
        self.txtFilePath2 = Label(self.master, text="path: {}".format(self.path2), font=("Helvetica", 8), fg='black', width=40, bg='white')
        self.txtFilePath2.grid(row=1, column=1, padx=(40, 0), pady=(60, 0))


    def findTxt(self):
        for file in os.listdir(self.path1):
            if file.endswith(".txt"):
                source = self.path1
                destination = self.path2
                shutil.move(source, destination)
                fName = os.path.join(self.fPath2, file)
                endTime = os.path.getmtime(self.fName)
                print(file, self.endTime)


    def database(self):

        conn = sqlite3.connect('findTxt.db')

        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_finame TEXT,  col_time INT \
                )")
            conn.commit()
        conn.close()

        conn = sqlite3.connect('findTxt.db')

        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(col_finame, col_time) VALUES (?)", (self.fName, self.endTime))

            conn.commit()
        conn.close()

        conn = sqlite3.connect('findTxt.db')

        with conn:
            cur = conn.cursor()
            cur.execute("SELECT col_finame AND col_time FROM tbl_txt WHERE col_finame LIKE '%.txt'")
            varFile = cur.fetchall()
            print(varFile)



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()