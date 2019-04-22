import Cell as c
class Board():
    def __init__(self,size=100):
        self.board = [None]*size
    
    def fillboard(self,id,pos,dest):
        cell = c.Cell(id,dest,pos)
        self.board[id-1] = cell