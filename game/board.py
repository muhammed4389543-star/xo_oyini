# board.py
import pygame
from settings import *

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board = [[EMPTY for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.winning_line = None

    def draw_lines(self):
        # Gorizontal chiziqlar
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
        # Vertikal chiziqlar
        pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == PLAYER_O:
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, 
                                       (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                        int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), 
                                       CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[row][col] == PLAYER_X:
                    pygame.draw.line(self.screen, CROSS_COLOR, 
                                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                    pygame.draw.line(self.screen, CROSS_COLOR, 
                                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def available_square(self, row, col):
        return self.board[row][col] == EMPTY

    def is_full(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == EMPTY:
                    return False
        return True

    def check_win(self, player):
        # Vertikal tekshirish
        for col in range(BOARD_COLS):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                self.draw_vertical_winning_line(col, player)
                return True

        # Gorizontal tekshirish
        for row in range(BOARD_ROWS):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                self.draw_horizontal_winning_line(row, player)
                return True

        # Diagonal tekshirish (pastga)
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            self.draw_desc_diagonal(player)
            return True

        # Diagonal tekshirish (yuqoriga)
        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            self.draw_asc_diagonal(player)
            return True

        return False

    # Qizil chiziq chizish funksiyalari
    def draw_vertical_winning_line(self, col, player):
        posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.line(self.screen, RED_COLOR, (posX, 15), (posX, HEIGHT - 15), WIN_LINE_WIDTH)

    def draw_horizontal_winning_line(self, row, player):
        posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.line(self.screen, RED_COLOR, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH)

    def draw_asc_diagonal(self, player):
        pygame.draw.line(self.screen, RED_COLOR, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)

    def draw_desc_diagonal(self, player):
        pygame.draw.line(self.screen, RED_COLOR, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)
    
    def reset(self):
        self.board = [[EMPTY for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
