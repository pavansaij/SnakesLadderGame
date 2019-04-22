import pygame
import math

def drawsnakesandladders(pygame,gameDisplay,config,board_pos):
    for key,val in config.items():
        try:
            st,en = int(key),int(val)
            if st > en:
                pygame.draw.line(gameDisplay, (255,0,0), board_pos[key], board_pos[val])
            elif st < en:
                pygame.draw.line(gameDisplay, (0,255,0), board_pos[key], board_pos[val])
        except:
            continue

def create_board(config):
    size_b,rows,board_pos = config['size'],config['rows'],{}
    pygame.init()
    white,black,blue = (255,255,255),(0,0,0),(0,0,255)
    gameDisplay = pygame.display.set_mode((800,600))

    pygame.display.set_caption("Snakes and Ladders")
    size   = 48
    center = int(math.sqrt(size**2+size**2))//2
    boardLength = rows
    gameDisplay.fill(white)

    cnt,count = 0,size_b
    for i in range(1,boardLength+1):
        mynum = 9
        for z in range(1,boardLength+1):
            if cnt % 2 == 0:
                pygame.draw.rect(gameDisplay, white,[size*z,size*i,size,size])
            else:
                pygame.draw.rect(gameDisplay, blue, [size*z,size*i,size,size])
            
            cnt +=1
            myfont = pygame.font.SysFont("Comic Sans MS", 18)
            if i%2:
                fnum = count
                label = myfont.render(str(fnum), 1, black)
            else:
                fnum = count-mynum
                label = myfont.render(str(fnum), 1, black)
                mynum-=2
            board_pos[str(fnum)] = [size*z+center,size*i+center]
            gameDisplay.blit(label, (size*z+10, size*i+10))
            count-=1
        cnt-=1
    
    for key,val in config.items():
        pygame.event.get()
        try:
            st,en = int(key),int(val)
            val = str(val)
            if st > en:
                pygame.draw.line(gameDisplay, (255,0,0), (board_pos[key][0],board_pos[key][1]), (board_pos[val][0],board_pos[val][1]), 2)
            elif st < en:
                pygame.draw.line(gameDisplay, (0,255,0), (board_pos[key][0],board_pos[key][1]), (board_pos[val][0],board_pos[val][1]), 2)
        except:
            continue


    pygame.draw.rect(gameDisplay,black,[size,size,boardLength*size,boardLength*size],1)    
    pygame.display.update()
    return [board_pos,pygame]