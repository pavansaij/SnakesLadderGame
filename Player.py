class Player():
    def __init__(self,name):
        self.pos = 0
        self.name = name
        self.status = True
        self.rank = None
         
    def move(self,inc):
        self.pos+=inc
