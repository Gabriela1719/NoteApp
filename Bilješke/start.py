from tkinter import *
from NoteDB import NoteDB
from dashboard import Dashboard
from tkinter import messagebox

if __name__=="__main__":
    try:

        db=NoteDB(username="root",password="")
        Dashboard().initUI(db)
    except Exception as e:
        messagebox.showinfo("Greška","Nije moguće ostvariti konekciju s bazom.")