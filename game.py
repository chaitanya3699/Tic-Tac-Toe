import pygame, sys, time, random, math
from pygame.locals import *
from math import inf as infinity
import os

width = 400
height = 400
fps = 30
white = (255, 255, 255)

turn = 'X'
winner = None
draw = None

board = [[None]*3, [None]*3, [None]*3]
pygame.init()

CLOCK = pygame.time.Clock()

surface = pygame.display.set_mode((width, height+100), 0, 32)
pygame.display.set_caption('Tic-tac-toe')

#loading the images
p_img = pygame.image.load("x.png")
p_img = pygame.transform.scale(p_img, (80,80))

c_img = pygame.image.load("o.png")
c_img = pygame.transform.scale(c_img, (80,80))

#function to display the initial window
def draw_board():
    surface.fill((0,0,0))

    pygame.draw.line(surface, white, (width/3, 0), (width/3, height), 7)
    pygame.draw.line(surface, white, (width/3 * 2, 0), (width/3 *2, height), 7)

    pygame.draw.line(surface, white, (0, height/3), (width, height/3), 7)
    pygame.draw.line(surface, white, (0, height/3 * 2), (width, height/3 * 2), 7)

#function to display the status of game
def displayStatus(brd):
    global draw, winner
    getWinner(brd)
    #print(winner)
    if (isBoardFull(brd) == True) and (winner == None):
        draw = True
    
    if draw!=None:
        msg = "It's a Draw!"
    elif winner is None:
        if turn=='X':
            msg = "Your Turn!"
        else:
            msg = "Ai's Turn!"
    else:
        if winner=='X':
            msg = "Player has won this time!"
        elif winner=='O':
            msg = "Computer has won this time!"

    font_obj = pygame.font.Font(None, 30)
    text = font_obj.render(msg, 1, white)

    surface.fill ((0,0,0), (0, 400, 500, 100))
    text_rect = text.get_rect(center = (width/2, 500-50))
    surface.blit(text, text_rect)
    pygame.display.update()

#function which checks if game is over and updates the variable winner
def getWinner(brd):
    global winner,draw

    if (brd[0][0]==brd[0][1]==brd[0][2] and (brd[0][0] is not None)):
        winner = brd[0][0]
    elif (brd[1][0]==brd[1][1]==brd[1][2] and (brd[1][0] is not None)):
        winner = brd[1][0]
    elif (brd[2][0]==brd[2][1]==brd[2][2] and (brd[2][0] is not None)):
        winner = brd[2][0]

    elif (brd[0][0]==brd[1][0]==brd[2][0] and (brd[0][0] is not None)):
        winner = brd[0][0]
    elif (brd[0][1]==brd[1][1]==brd[2][1] and (brd[0][1] is not None)): 
        winner = brd[0][1]
    elif (brd[0][2]==brd[1][2]==brd[2][2] and (brd[0][2] is not None)):
        winner = brd[0][2]

    elif (brd[0][0]==brd[1][1]==brd[2][2] and (brd[0][0] is not None)):
        winner = brd[0][0]
    elif (brd[0][2]==brd[1][1]==brd[2][0] and (brd[0][2] is not None)):
        winner = brd[0][2]

    else:
        winner = None

#function to check if borad is full
def isBoardFull(brd):
    flag = 1
    for row in range(0, 3):
        for col in range(0,3):
            if brd[row][col]==None:
                flag = 0
    if flag==1:
        return True
    else:
        return False

#function to check if a particular player wins or not
def isComplete(state, ltr):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[0][2], state[1][1], state[2][0]],
    ]
    if [ltr,ltr,ltr] in win_state:
        return True
    else:
        return False

#function to check if game is over 
def game_over(state):
    return isComplete(state, 'X') or isComplete(state, 'O')

#function to return the list of empty cells in the board
def getEmptyCells(brd):
    lst = []
    for row in range(0,3):
        for col in range(0,3):
            if brd[row][col] is None:
                lst.append((row,col))
    return lst

#function to draw X or O to the display
def drawXO(r,c):
    global board,turn,width,height
    if r==0:
        x_cord = 30
    elif r==1:
        x_cord = width/3 + 30
    elif r==2:
        x_cord = width/3*2 + 30
    
    if c==0:
        y_cord = 30
    elif c==1:
        y_cord = height/3 + 30
    elif c==2:
        y_cord = height/3 *2 + 30

    board[r][c] = turn

    if(turn=='X'):
        surface.blit(p_img, (y_cord, x_cord))
        turn = 'O'
    else:
        surface.blit(c_img, (y_cord, x_cord))
        turn = 'X'
    pygame.display.update()

#function to print the board to terminal
def printBoard(brd):
    for i in range(0,3):
        print("{} {} {}".format(brd[i][0], brd[i][1], brd[i][2]))

#function to calculate utility of a state
def utility(state):
    if isComplete(state, 'X'):
        score = -1
    elif isComplete(state, 'O'):
        score = 1
    else:
        score = 0
    return score

#minimax function using alpha-beta pruning
def minimax(state, depth,alpha, beta, player):
    
    if depth==0 or game_over(state):
        points = utility(state)
        return [-1, -1, points]

    if player=='O':
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, infinity]

    for (r,c) in getEmptyCells(state):
        state[r][c] = player

        if player== 'O':
            score = minimax(state, depth-1,alpha, beta, 'X')
        else:
            score = minimax(state, depth-1, alpha, beta,'O')

        state[r][c] = None
        score[0] = r;
        score[1] = c;

        if player=='O':
            if (best[2]<score[2]):
                best = score
            alpha = max([alpha, score[2]])
        else:
            if (score[2]<best[2]):
                best = score
            beta = min([beta, score[2]])
        if beta<=alpha:
            break

    return best
    
#function which returns the move of AI 
def aiTurn(brd):
    global winner

    emptyCells = getEmptyCells(brd)
    depth = len(emptyCells)
    
    if depth==0 or winner!=None:
        return (-1, -1)

    move = minimax(brd, depth,-infinity, infinity, 'O')
    return (move[0], move[1])

#function which returns the move of Player
def playerClick(brd):
    global winner
    
    x,y = pygame.mouse.get_pos()
    if (x< width/3):
        col = 0
    elif (x< width/3*2):
        col = 1
    elif (x< width):
        col = 2
    else:
        col = None
    
    if (y< height/3):
        row = 0
    elif (y< height/3*2):
        row = 1
    elif (y< height):
        row = 2
    else:
        row = None

    return (row,col)

#function to play tic-tac-toe
def ticTacToe(brd):
    row,col = playerClick(brd)
    if((row !=None) and (col!=None) and brd[row][col] is None):
        drawXO(row,col)
        displayStatus(brd)
        
        r,c = aiTurn(brd)
        if (r,c)==(-1,-1):
            displayStatus(brd)
        else:
            drawXO(r,c)
            displayStatus(brd)

#main method
def main():
    draw_board()
    displayStatus(board)
    while winner==None and len(getEmptyCells(board))!=0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type is MOUSEBUTTONDOWN:
                ticTacToe(board)

        pygame.display.update()
        CLOCK.tick(fps)

main()