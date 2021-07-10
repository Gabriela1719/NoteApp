from tkinter import *
from tkinter import messagebox
from tkinter import font

from NoteDB import NoteDB
from Note import Note
class AddNewNote:
    def __init__(self):
        pass
    def add_new_callback(self):
        title = self.note_title.get()
        msg=self.text.get("1.0",'end-1c')
        if len(title) <=0:
            messagebox.showinfo("Invalid Action","Unesite naslov bilješke..")
            return
        if len(msg) <=0:
            messagebox.showinfo("Invalid Action","Unesite bilješku..")
            return
        try:
            obj=Note(msg=msg,title=title)
            self.db.add_note(obj)
            self.dash.list_all_callback()
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()

            messagebox.showinfo("Success","Bilješka spremljena..")
        except Exception as e:
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            messagebox.showinfo("Error","Bilješka nije dodana. Pokušajte ponovno")
    def cancel_callback(self):
        self.dash.root.attributes('-disabled', False)
        self.root.destroy()
    def initUI(self,dash,db):
        self.dash=dash
        self.dash.root.attributes('-disabled', True)
        self.db=db
        self.root = Tk()
        self.root.geometry("500x550")
        self.root.protocol("WM_DELETE_WINDOW", self.cancel_callback)
        self.root.title("Dodavanje nove bilješke")
        self.Font = font.Font(family='Helvetica', size=15, weight='bold')
        self.Font_search_text = font.Font(family='Helvetica', size=15)
        self.Font_search_btn = font.Font(family='Helvetica', size=10, weight='bold')
        self.Font_note = font.Font(family='Helvetica', size=12)
        self.add_label=Label(self.root,text="Dodaj novu bilješku",font=('Comic sans ms',14,'bold'))
        self.note_label=Label(self.root,text="Naslov",font=('Comic sans ms',12))
        self.note_label.place(x=10,y=55)
        self.add_label.place(x=170,y=20)
        self.title_var=StringVar()
        self.note_title=Entry(self.root,textvariable = self.title_var,justify='center',font=('Comic sans ms',12),width=46)
        self.note_title.place(x=10, y=80)
        self.text = Text(self.root,font=('Comic sans ms',12),width=55,height=14)
        self.text.place(x=0,y=120)
        self.scroll = Scrollbar(self.root, orient=VERTICAL, command=self.text.yview)
        self.text['yscroll'] = self.scroll.set

        #self.scroll.pack(side="right", fill="y")
        self.scroll.place(x=485,y=120,height=330)
        self.save_button=Button(self.root,bg="#27242c",fg="white",text="Spremi",font=('Comic sans ms',11),width=12,command=lambda:self.add_new_callback())
        self.save_button.place(x=300,y=480)
        self.cancel_button=Button(self.root,bg="#27242c",fg="white",text="Odustani",font=('Comic sans ms',11),command=lambda:self.cancel_callback(),width=12)
        self.cancel_button.place(x=100,y=480)
        self.root.mainloop()