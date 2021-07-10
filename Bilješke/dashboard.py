from tkinter import *
from tkinter import ttk
from NoteDB import NoteDB
from Note import Note
from editnote import EditNote
from addnewnote import AddNewNote
from tkinter import messagebox
from tkinter import font
from PIL import Image
class Dashboard:
    def __init__(self):
        pass
    def show_notes(self,notes):
        i=0
        self.curr_notes=notes
        self.listbox.delete(0,self.listbox.size())
        for note in notes:
            self.listbox.insert(i,str(note.get_title()))
            if i%2==0:
                self.listbox.itemconfig(i,bg="#d3d3d3")
            i+=1
    def search_callback(self):
        if len(self.var.get())<=0:
             messagebox.showinfo("Invalid Action","Please Enter Search Entry")
             return
        notes=self.db.search_notes(self.var.get())
        if len(notes) ==0:
              messagebox.showinfo("Info","No match Found")
        else:
              self.show_notes(notes)
    def list_all_callback(self):
        try:
            notes=self.db.get_all_notes()
            self.show_notes(notes)
        except Exception as e:
            print(e)
            messagebox.showinfo("Error","Could Not Fetch Notes")
    def edit_callback(self):
        try:
            EditNote().initUI(self,self.db,self.curr_notes[self.listbox.curselection()[0]])
        except Exception as e:
            pass
    def add_callback(self):
        AddNewNote().initUI(self,self.db)

    def initUI(self,db):
        self.db=db
        self.root = Tk()
        self.root.geometry("990x600")
        self.root.title("BilješkeApp ")
        self.Font = font.Font(family='Comic sans ms', size=12)
        self.Font_naslov=font.Font(family='Comic sans ms', size=20, weight="bold")
        self.Font_search_text = font.Font(family='Comic sans ms', size=12)
        self.Font_search_btn = font.Font(family='Comic sans ms', size=10)
        self.Font_note = font.Font(family='Comic sans ms', size=12)
        self.naslov=Label(self.root, text="Bilješke", font=self.Font_naslov)
        self.naslov.place(x=430, y=40)
        self.add_button=Button(self.root, width=20,bg="#27242c",fg="white",text="Dodaj novu bilješku",font=self.Font,bd=0, command=lambda:self.add_callback())
        self.add_button.place(x=670,y=250)
        self.list_all_btn=Button(self.root,width=20,bg="#27242c",fg="white",text="Izlistaj sve bilješke",font=self.Font,bd=0,command=lambda:self.list_all_callback())
        self.list_all_btn.place(x=670,y=350)
        self.search_label=Label(self.root,text="Pretraži bilješke",font=self.Font, width=50)
        self.search_label.place(x=430,y=120)
        self.note_label=Label(self.root,text="-- Popis svih bilješki --",font=self.Font)
        self.note_label.place(x=200,y=120)
        self.var=StringVar()
        self.search_box=Entry(self.root,width=20,textvariable=self.var,font=self.Font_search_text)
        self.search_box.place(x=620,y=150)
        self.search_button=Button(self.root,bg="#27242c",fg="white",text="Pretraži",font=self.Font_search_btn,width=13,command=lambda:self.search_callback())
        self.search_button.place(x=830,y=150)

        self.listbox = Listbox(self.root,selectmode=SINGLE,width=55,font=self.Font_note,height=16)
        self.scroll = Scrollbar(self.root, orient=VERTICAL, command=self.listbox.yview)
        self.listbox['yscroll'] = self.scroll.set

        #self.scroll.pack(side="right", fill="y")
        self.scroll.place(x=580,y=150,height=390)
        self.list_all_callback()

        self.listbox.bind('<<ListboxSelect>>', lambda l:self.edit_callback())
        self.listbox.place(x=30,y=150)

        self.root.mainloop()


