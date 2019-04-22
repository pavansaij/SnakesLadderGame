class Cell():
    def __init__(self,id,dest,pos):
        self.id = id
        self.rowcol = pos
        self.did = dest if dest else id