import math

import numpy as np
import pygame
import sys
import board as boardd
import random
import win as win
import button
import pygame_menu
import minimax
import gui
from variables import *

def game():
    display.fill((0, 0, 0))
    turn = random.randint(PLAYER, AI)
    boardd.print_board(board)
    pygame.display.update()
    gui.gui_board()
    gui.chips_board(board)
    pygame.display.update()
    gameover = False
    pygame.init()
    global k, prune

    try:
        k = int(k)
    except:
        print('Invalid k')
    print(f'K= {k}')
    print(f'PRUNING: {prune}')

    while  not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(display, BLACK, (0, 0, width, SQUARESIZE))
                x_pos = event.pos[0]
                # print(x_pos)
                if turn == PLAYER:
                    pygame.draw.circle(display, RED, (x_pos, SQUARESIZE/2), RADIUS)

                    pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display, BLACK, (0, 0, width, SQUARESIZE))
                #turn 1
                if turn == PLAYER and not gameover:
                    x_pos = event.pos[0]            #takes x position of mouse click range (0->700)
                    # print(x_pos)
                    column = (x_pos // SQUARESIZE)
                    # print(column)
                    if boardd.valid_location(board,column):
                        row = boardd.next_row(board, column)
                        boardd.drop_piece(board,row,column,PLAYER_PIECE)
                        boardd.print_board(board)
                        if win.wining_move(board,PLAYER_PIECE)==True:
                            print("PLAYER 1 WIN")
                            text = fontt.render("RED WINS", 1 ,RED)
                            display.blit(text, (160,10))
                            gameover = True
                        gui.chips_board(board)
                        turn += 1
                        turn = turn % 2
                        endGame(gameover)
             #turn 2
        if turn == AI and not gameover:
            if prune == True:
                column, minimax_score = minimax.minimax(board, k, ALPHA_WORST_VALUE, BETA_WORST_VALUE, True)
            else:
                column, minimax_score = minimax.minimax_2(board, k, True)

            if boardd.valid_location(board, column):
                row = boardd.next_row(board, column)
                pygame.time.wait(500)
                boardd.drop_piece(board, row, column, AI_PIECE)
                boardd.print_board(board)
                if win.wining_move(board, AI_PIECE) == True:
                    print("PLAYER 2 WIN")
                    text = fontt.render("YELLOW WINS", 1, ORANGE)
                    display.blit(text, (120, 10))
                    gameover = True

                gui.chips_board(board)
                turn += 1
                turn = turn % 2
                endGame(gameover)


def endGame(Gameover):
    if Gameover == True:
        pygame.time.wait(5000)
        # pygame.display.quit()
        pygame.quit()
        sys.exit()

def menu():
    pygame.display.set_caption('Welcome Page')
    value = True
    # load button images
    start_img = pygame.image.load('start_btn.png').convert_alpha()
    exit_img = pygame.image.load('exit_btn.png').convert_alpha()


    # create button instances
    start_button = button.Button(100, 200, start_img, 0.8)
    exit_button = button.Button(450, 200, exit_img, 0.8)

    display.fill((202, 228, 241))

    while  value:

        if start_button.draw(display):
            display.fill((0, 0, 0))
            main()
            break

        if exit_button.draw(display):
            print('EXIT')
            value = False
            pygame.quit()
            sys.exit()

        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                quit = False
                pygame.quit()
                sys.exit()

        pygame.display.update()


def main():  # function to display the main menu
    global display, menu
    display = pygame.display.set_mode(size)
    menu = pygame_menu.Menu('CONNECT FOUR', width, height,
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input('K :', default=k, onchange=setK)
    menu.add.selector('', [('Minimax with alpha-beta pruning', 1), ('Minimax without alpha-beta pruning', 2)],
                      onchange=setPruning)
    menu.add.button('Play', game)
    menu.mainloop(display)

def setPruning(a, b):
    global prune
    prune = not prune


def setK(kInput):
    global k
    k = kInput


if __name__ == '__main__':
    board = boardd.create_board()
    boardd.print_board(board)
    pygame.init()
    fontt = pygame.font.SysFont('Verdana',70)
    menu()






