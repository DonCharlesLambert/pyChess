from tkinter import *
from PIL import Image
from PIL import ImageTk

class Chess:
    WIDTH = 400 # Square
    BOARD_SIZE = 360
    BOARD_START = 20
    TILE_SIZE = int(BOARD_SIZE/8)

    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, width=self.WIDTH, height=self.WIDTH)
        self.canvas.pack()
        self.board = []
        self.create_board()
        window.mainloop()

    def create_board(self):
        tile = 0
        for x in range(self.BOARD_START, self.BOARD_START + self.BOARD_SIZE, self.TILE_SIZE):
            for y in range(self.BOARD_START, self.BOARD_START + self.BOARD_SIZE, self.TILE_SIZE):
                self.board.append(BoardTile(self.canvas, tile, x=x, y=y, size=self.TILE_SIZE))
                tile = (tile + 1) % 2
            tile = (tile + 1) % 2


class BoardTile:
    LIGHT_BROWN = 0
    DARK_BROWN = 1
    LIGHT_GREY = 2
    DARK_GREY = 3

    def __init__(self, canvas, tile, **kwargs):
        image = 'img/brown_light_square.png'
        if tile == self.DARK_BROWN:
            image = 'img/brown_dark_square.png'
        elif tile == self.LIGHT_GREY:
            image = 'img/grey_light_square.png'
        elif tile == self.DARK_GREY:
            image = 'img/grey_dark_square.png'
        self.sprite = self.resize(image, int(360/8), int(360/8))
        self.canvas = canvas
        self.canvas.create_image(kwargs['x'], kwargs['y'], image=self.sprite, anchor="nw")

    @staticmethod
    def resize(directory, width, height):
        img = Image.open(directory)
        img = img.resize((width, height), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(img)
        return photoImg

Chess()
