# settings.py

# Ekran o'lchamlari
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Ranglar (RGB)
BG_COLOR = (28, 170, 156)  # Orqa fon (firuza rang)
LINE_COLOR = (23, 145, 135) # Chiziqlar rangi
CIRCLE_COLOR = (239, 231, 200) # O (Nolik) rangi - och sariq
CROSS_COLOR = (84, 84, 84)   # X (Iks) rangi - to'q kulrang
RED_COLOR = (255, 0, 0)      # Yutish chizig'i

# O'yinchi belgilari
PLAYER_X = 1
PLAYER_O = 2
EMPTY = 0
