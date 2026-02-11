# main.py
import pygame
import sys
import asyncio
from settings import *
from board import Board
from ai import AI

# Pygame ni ishga tushirish
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('X&O - Tic Tac Toe')
screen.fill(BG_COLOR)

class Game:
    def __init__(self):
        self.board = Board(screen)
        self.ai = AI()
        self.player = PLAYER_X  # O'yin X bilan boshlanadi
        self.gamemode = 'pvp'   # Boshlanishiga 'pvp' (odamga qarshi odam)
        self.running = True
        self.game_over = False
        self.board.draw_lines()

    def make_move(self, row, col):
        if self.board.available_square(row, col):
            self.board.mark_square(row, col, self.player)
            self.board.draw_figures()
            
            if self.board.check_win(self.player):
                self.game_over = True
            elif self.board.is_full():
                self.game_over = True # O'yin tugaganini belgilaymiz
            
            if not self.game_over:
                self.next_turn()
            return True
        return False

    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_gamemode(self):
        if self.gamemode == 'pvp':
            self.gamemode = 'ai'
            pygame.display.set_caption('X&O - Botga qarshi (AI)')
        else:
            self.gamemode = 'pvp'
            pygame.display.set_caption('X&O - Do\'st bilan (PvP)')
        self.restart()

    def restart(self):
        screen.fill(BG_COLOR)
        self.board.reset()
        self.board.draw_lines()
        self.player = PLAYER_X
        self.game_over = False

async def main():
    game = Game()

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

            if event.type == pygame.KEYDOWN:
                # 'G' tugmasi bosilsa rejim o'zgaradi (PvP <-> AI)
                if event.key == pygame.K_g:
                    game.change_gamemode()
                
                # 'R' tugmasi bosilsa o'yin qayta boshlanadi
                if event.key == pygame.K_r:
                    game.restart()

            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                mouseX = event.pos[0] # x
                mouseY = event.pos[1] # y

                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if game.board.available_square(clicked_row, clicked_col):
                    game.make_move(clicked_row, clicked_col)

                    # Agar AI rejimi bo'lsa va o'yin tugamagan bo'lsa, Bot yuradi
                    if game.gamemode == 'ai' and not game.game_over and game.player == PLAYER_O:
                        # Bot o'ylashi uchun ozgina pauza (vizual effekt uchun)
                        pygame.display.update()
                        pygame.time.delay(300) 
                        
                        ai_move = game.ai.pick_move(game.board)
                        if ai_move:
                            game.make_move(ai_move[0], ai_move[1])

        pygame.display.update()
        await asyncio.sleep(0)
    
    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())
