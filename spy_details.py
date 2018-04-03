from datetime import datetime
class Spy:
    def __init__ (self,name,salutation,age,ratings):
        self.salutation=salutation
        self.name=self.salutation + " " + name
        self.age=age
        self.ratings=ratings
        self.is_online=True
        self.chats=[ ]
        self.current_status_message=None

spy=Spy('Anjali','Ms.',25,3.7)

class ChatMessage:
    def __init__ (self,message,sent_by_me):
        self.message=message
        self.time=datetime.now()
        self.sent_by_me=sent_by_me