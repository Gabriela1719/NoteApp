from tkinter import *
from NoteDB import NoteDB
from Note import Note
from tkinter import messagebox
from tkinter import font

class EditNote:
    def __init__(self):
        pass
    def update_callback(self,note):
        title = self.note_title.get()
        if len(title) <=0:
            messagebox.showinfo("Invalid Action","Unesite naslov bilješke..")
            return
        msg=self.text.get("1.0",'end-1c')
        if len(msg) <=0:
            messagebox.showinfo("Invalid Action","Unesite bilješku..")
            return
        try:
            obj=Note(idt=note.get_idt(),msg=msg,title=title)
            self.db.update_note(obj)
            self.dash.list_all_callback()
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()

            messagebox.showinfo("Success","Bilješka uspješno ažurirana..")

        except Exception as e:
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            messagebox.showinfo("Greška","Bilješka nije ažurirana. Pokušajte ponovno.")

    def cancel_callback(self):
        self.dash.root.attributes('-disabled', False)
        self.root.destroy()
    def delete_callback(self,note):
        try:
            self.db.delete_note(note)
            self.dash.list_all_callback()
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()

            messagebox.showinfo("Success","Bilješka izbrisana..")

        except Exception as e:
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()

            messagebox.showinfo("Greška","Bilješka nije izbrisana. Pokušajte ponovno.")

    def initUI(self,dash,db,note):
        self.dash=dash
        self.dash.root.attributes('-disabled', True)
        self.db=db
        self.root = Tk()
        self.root.geometry("500x600")
        self.root.protocol("WM_DELETE_WINDOW", self.cancel_callback)
        self.root.title("Ažuriranje bilješke")
        self.Font_note = font.Font(family='Comic sans ms', size=12)
        self.add_label=Label(self.root,text="Ažuriraj bilješku",font=('Comic sans ms',14,'bold'))
        self.note_label=Label(self.root,text="Naslov",font=('Comic sans ms',12))
        self.note_label.place(x=10,y=55)
        self.add_label.place(x=170,y=20)
        self.title_var=StringVar()
        self.note_title=Entry(self.root,textvariable = self.title_var,justify='center',font=('Comic sans ms',12),width=46)
        self.note_title.insert(END,note.get_title())
        self.note_title.place(x=10, y=80)
        self.text = Text(self.root,font=('Comic sans ms',12),width=55,height=14)
        self.text.insert('1.0',note.get_msg())
        self.text.place(x=0,y=120)
        self.scroll = Scrollbar(self.root, orient=VERTICAL, command=self.text.yview)
        self.text['yscroll'] = self.scroll.set

        #self.scroll.pack(side="right", fill="y")
        self.scroll.place(x=485,y=120,height=330)
        time="Stvoreno : "+str(note.get_time())
        self.time_label=Label(self.root,text=time,font=self.Font_note)
        self.time_label.place(x=140,y=475)
        self.save_button=Button(self.root,bg="#27242c",fg="white",text="Ažuriraj",font=('Comic sans ms',11),width=12,command=lambda:self.update_callback(note))
        self.save_button.place(x=330,y=530)
        self.delete_button=Button(self.root,bg="#27242c",fg="white",text="Izbriši",font=('Comic sans ms',11),command=lambda:self.delete_callback(note),width=12)
        self.delete_button.place(x=180,y=530)
        self.cancel_button=Button(self.root,bg="#27242c",fg="white",text="Odustani",font=('Comic sans ms',11),command=lambda:self.cancel_callback(),width=12)
        self.cancel_button.place(x=40,y=530)
        self.root.mainloop()