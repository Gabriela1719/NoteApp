class Note:
    def __init__(self,idt=0,title="",msg="",time=""):
        self.__idt=idt
        self.__title=title
        self.__msg=msg
        self.__time=time
    def get_title(self):
        return self.__title
    def get_msg(self):
        return self.__msg
    def get_idt(self):
        return self.__idt
    def get_time(self):
        return self.__time
    def set_msg(self,msg):
        self.__msg=msg
    def set_idt(self,idt):
        self.__idt=idt
    def set_time(self,time):
        self.__time=time