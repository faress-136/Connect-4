from variables import *

def gui_board():           #for building frame black circles with blue rectangle
    for c in range(COLUMN):
        for r in range(ROW):
            pygame.draw.rect(display, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE) )
            #rect(surface, color, Rect, width=0)
            pygame.draw.circle(display, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE + SQUARESIZE+SQUARESIZE/2)), RADIUS )
            #circle(surface, color, pos, radius, width =0)      +SquareSize/2 --> half rectangle(offset)
    pygame.display.update()

def chips_board(board):           #for building chips red circles and orange circles
    for c in range(COLUMN):
        for r in range(ROW):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(display, RED, (int(c*SQUARESIZE + SQUARESIZE/2), height-int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS )
                #NO + square size  as we fill from the first bottom circle

            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(display, ORANGE, (int(c*SQUARESIZE + SQUARESIZE/2), height-int(r*SQUARESIZE +SQUARESIZE/2)), RADIUS )
            #circle(surface, color, pos, radius, width =0)      +SquareSize/2 --> half rectangle

    pygame.display.update()

