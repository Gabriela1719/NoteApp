import pymysql as mysql
from Note import Note
class NoteDB:
    def __init__(self,username="",password=""):
        try:
            NoteDB.db=mysql.connect(host="localhost",user=username,password=password,database="noteapp")
            NoteDB.cursor=NoteDB.db.cursor()
        except Exception as e:
            raise
    def add_note(self,note):
        q="insert into note(title,msg) values('%s','%s')"%(note.get_title(),note.get_msg())
        try:
            NoteDB.cursor.execute(q)
            NoteDB.db.commit()
        except Exception as e:
            print(e)
            NoteDB.db.rollback()
            raise
    def get_one_note(self,idt):
        q="select * from note where id=%d"%(idt)
        try:
            NoteDB.cursor.execute(q)
            result=NoteDB.cursor.fetchall()
            obj=Note(idt=result[0],title=result[1],msg=result[2],time=result[3])
            return obj
        except Exception as e:
            raise
    def get_all_notes(self):
        q="select * from note order by time desc;"
        try:
            NoteDB.cursor.execute(q)
            notes=[]
            results=NoteDB.cursor.fetchall()
            for result in results:
                obj=Note(idt=result[0],title=result[1],msg=result[2],time=result[3])
                notes.append(obj)
            return notes
        except Exception as e:
            raise
    def update_note(self,note):
        q="update note set title='%s',msg='%s' where id=%d"%(note.get_title(),note.get_msg(),note.get_idt())
        try:
            NoteDB.cursor.execute(q)
            NoteDB.db.commit()
        except Exception as e:

            NoteDB.db.rollback()
            raise
    def search_notes(self,query):
        q="select * from note where title like '%{0}%' order by time desc".format(query)
        try:
            NoteDB.cursor.execute(q)
            notes=[]
            results=NoteDB.cursor.fetchall()
            for result in results:
                obj=Note(idt=result[0],title=result[1],msg=result[2],time=result[3])
                notes.append(obj)
            return notes
        except Exception as e:
            raise
    def delete_note(self,note):
        q="delete from note where id=%d"%(note.get_idt())
        try:
            NoteDB.cursor.execute(q)
            NoteDB.db.commit()
        except Exception as e:
            NoteDB.db.rollback()
            raise
