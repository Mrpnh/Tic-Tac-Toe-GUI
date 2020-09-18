# Importing and Initializing pygame

import pygame
import time
pygame.mixer.init()
pygame.init()

# Game specific Vaiables

screenSize=300
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
exit_game=False
game_over=False
check_list=[]
count_set=set()
score=1

# Initial Board

board=[str(i+1) for i in range(9)]

# Resetting Board

def resetBoard(board):
    board=[str(i+1) for i in range(9)]
    return board

# Initializing window

gameWindow = pygame.display.set_mode((screenSize,screenSize+100))
gameCap = pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

# loading image

crossImg = pygame.image.load('cross.jpg')
crossImg = pygame.transform.scale(crossImg, (90,90))
circleImg = pygame.image.load('circle.jpg')
circleImg = pygame.transform.scale(circleImg, (80,90))

# Displaying Image

def displayImg(pos_x,pos_y):
   return [5+100*pos_x,5+100*pos_y]

# Filling 'X' or 'O' in desired postion by entering the number of that position

def filldetails(pos,score):
    global board    
    if board[pos-1]!='X' and board[pos-1]!='O':
        if score%2==0:
            board[pos-1]='X'
        else:
            board[pos-1]='O'
    global count_set
    count_set.add(pos)

# Text Rendering


def textRender(text,color,x,y,text_size):
     font=pygame.font.SysFont(None,text_size)
     screenText=font.render(text,True,color)
     gameWindow.blit(screenText,(x,y))

# Checking If the board Full or not

def isFill():
    global count_set
    if len(count_set)==9:
        textRender("Wait for another game...",white,50,screenSize+72,25)
        return True

# Welcome window

def welcome():
    global exit_game
    global game_over
    count=1
    while not exit_game:
        if exit_game==True:
            break
        elif game_over==True or count==1:
            global board
            global count_set
            global check_list
            global score
            pygame.Surface.fill(gameWindow,white)
            textRender("Welcome to Tic-Tac-Toe", black,40,150,30)
            textRender("By", black,140,180,20)
            textRender("MRPNH", red,100,210,40)
            textRender("Press Space Bar To Play",black,50,300,25)
            for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    exit_game=True
               if event.type==pygame.KEYDOWN:
                   if event.key==pygame.K_SPACE:
                       pygame.mixer.music.load('music.mp3')
                       pygame.mixer.music.play()
                       gameloop()
                       board=resetBoard(board)
                       check_list=[]
                       count_set=set()
                       score=1
                    
        pygame.display.update()
        clock.tick(60)

# Game loop

def gameloop():
    global exit_game
    global game_over
    game_over=False
    while not exit_game:
        pygame.Surface.fill(gameWindow,white)
        pygame.draw.rect(gameWindow, black,(0,300,300,100))
        for i in range(1,3):
            pygame.draw.line(gameWindow, black, (100*i,0) , (100*i,screenSize),2)
            pygame.draw.line(gameWindow, black, (0,100*i) , (screenSize,100*i),2)

        if game_over==True:
             time.sleep(2)
             break   

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                              
                  pos = pygame.mouse.get_pos()
                  global score
                  score+=1
                  if pos[0]<100 and pos[1]<100:
                     check_list.append(displayImg(0,0))
                     filldetails(1,score)
                  if pos[0]>100 and pos[0]<200 and pos[1]<100:
                     check_list.append(displayImg(1,0))
                     filldetails(2,score)
                  if pos[0]>200 and pos[0]<300 and pos[1]<100:
                     check_list.append(displayImg(2,0))
                     filldetails(3,score) 
                  if pos[0]<100 and pos[1]>100 and pos[1]<200:
                     check_list.append(displayImg(0,1))
                     filldetails(4,score)
                  if pos[0]>100 and pos[0]<200 and pos[1]>100 and pos[1]<200:
                     check_list.append(displayImg(1,1))
                     filldetails(5,score)
                  if pos[0]>200 and pos[0]<300 and pos[1]>100 and pos[1]<200:
                     check_list.append(displayImg(2,1))
                     filldetails(6,score)
                  if pos[0]<100 and pos[1]>200 and pos[1]<300:
                     check_list.append(displayImg(0,2))
                     filldetails(7,score)
                  if pos[0]>100 and pos[0]<200 and pos[1]>200 and pos[1]<300:
                     check_list.append(displayImg(1,2))
                     filldetails(8,score)
                  if pos[0]>200 and pos[0]<300 and pos[1]>200 and pos[1]<300:
                     check_list.append(displayImg(2,2))
                     filldetails(9,score)
          
        for x,y in check_list:
              index_value=check_list.index([x,y])
              if index_value%2==0:
                  gameWindow.blit(crossImg,(x,y))
              else:
                  gameWindow.blit(circleImg,(x,y))
        
        game_over=isFill()
        line=isWin(board)
        if line[4]==True:
            pygame.draw.line(gameWindow, black, (line[0],line[2]), (line[1],line[3]),8)
            textRender(line[5]+" Won !",white,82,screenSize+20,55)
            textRender("Wait for another game...",white,50,screenSize+72,25)
            game_over=True
    
    
        pygame.display.update()

    


# Checking if a player Won or not

def isWin(bo):
      if bo[0]==bo[1]==bo[2]:
          return (50,250,50,50,True,bo[0])
      if bo[3]==bo[4]==bo[5]:
          return (50,250,150,150,True,bo[3])
      if bo[6]==bo[7]==bo[8]:
          return (50,250,250,250,True,bo[6])
      if bo[0]==bo[3]==bo[6]:
          return (50,50,50,250,True,bo[0])
      if bo[1]==bo[4]==bo[7]: 
          return (150,150,50,250,True,bo[1])
      if bo[2]==bo[5]==bo[8]:
          return (250,250,50,250,True,bo[2])
      if bo[0]==bo[4]==bo[8]:
          return (50,250,50,250,True,bo[0])                    
      if bo[2]==bo[4]==bo[6]:
          return (250,50,50,250,True,bo[2])
      return (0,0,0,0,False,0)



# Main Function

if __name__ == '__main__':
        welcome()
        pygame.quit()
        quit()


            
    
    
