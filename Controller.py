from Board import Board
from Player import Player
import random
import json
import Create_Board
import sys

size = 100
dice = [1,2,3,4,5,6]

class Game():
    def __init__(self,playerscnt,names):
        self.plcount = playerscnt
        self.players = self.constructPlayers(playerscnt,names)
        self.board = Board()
        self.snakesandlad = self.importJson()
        board_pygame = Create_Board.create_board(self.snakesandlad)
        self.board_pos = board_pygame[0]
        self.pygame = board_pygame[1]
        self.CompleteBoard()
        self.currentplayer = 0

    def importJson(self):
        with open(r'F:\\Python\\Programs\\PyGame\\board.json') as f:
            return json.load(f)

    def constructPlayers(self,count,names):
        res = []
        for i in range(count):
            res.append(Player(names[i]))
        return res

    def CompleteBoard(self):
        for i in range(1,size+1):
            if str(i) in self.snakesandlad:
                self.board.fillboard(i,self.board_pos[str(i)],self.snakesandlad[str(i)])
            else:
                self.board.fillboard(i,self.board_pos[str(i)],i)

    def MovePos(self,player):
        dice_num = random.choice(dice)
        if dice_num+player.pos+1 <= 100:
            player.move(dice_num)
            if dice_num == 6:
                self.MovePos(player)

    def play(self):
        player = self.players[self.currentplayer]
        self.MovePos(player)
        self.currentplayer = (self.currentplayer+1)%self.plcount
    
    def quit_game(self):
        self.pygame.quit()
        sys.exit()

game = Game(2,["prasad","madhu"])
while True:
    game.pygame.event.get()