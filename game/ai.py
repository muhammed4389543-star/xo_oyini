# ai.py
import random
from settings import *

class AI:
    def __init__(self):
        pass

    def pick_move(self, board_obj):
        # Bo'sh kataklarni topish
        empty_sqrs = []
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board_obj.available_square(row, col):
                    empty_sqrs.append((row, col))
        
        # Agar bo'sh joy bo'lsa, tasodifiy birini tanlash
        if len(empty_sqrs) > 0:
            return random.choice(empty_sqrs)
        return None
