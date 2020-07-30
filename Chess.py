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
        self.pieces = []
        self.create_game()
        window.mainloop()

    def create_game(self):
        tile = 0
        location = [1, 1]
        for y in range(self.BOARD_START, self.BOARD_START + self.BOARD_SIZE, self.TILE_SIZE):
            for x in range(self.BOARD_START, self.BOARD_START + self.BOARD_SIZE, self.TILE_SIZE):
                self.add_board_tile(x, y, tile)
                self.conditionally_add_game_piece(x, y, location)

                tile = (tile + 1) % 2
                location[0] += 1
            tile = (tile + 1) % 2
            location[0] = 1
            location[1] += 1

    def add_board_tile(self, x, y, tile):
        self.board.append(BoardTile(self.canvas, tile, x=x, y=y, size=self.TILE_SIZE))

    def conditionally_add_game_piece(self, x, y, location):
        colour = None
        piece = None
        if location[1] in [7, 8]:
            colour = "white"
        elif location[1] in [1, 2]:
            colour = "black"

        if location[1] in [2, 7]:
            piece = 'pawn'
        elif location[0] in [1, 8]:
            piece = 'rook'
        elif location[0] in [2, 7]:
            piece = 'knight'
        elif location[0] in [3, 6]:
            piece = 'bishop'
        elif location[0] == 4:
            piece = 'king'
        elif location[0] == 5:
            piece = 'queen'

        if colour is not None and piece is not None:
            self.add_game_piece(x, y, location, piece, colour)

    def add_game_piece(self, x, y, location, piece, colour):
        offset = 10
        piece = Piece((location[0], location[1]), piece, colour, size=self.TILE_SIZE-offset)
        self.pieces.append(piece)
        piece.inital_draw(self.canvas, x + offset/2, y + offset/2)


class BoardTile:
    LIGHT_BROWN = 0
    DARK_BROWN = 1
    LIGHT_GREY = 2
    DARK_GREY = 3

    def __init__(self, canvas, tile, **kwargs):
        directory = self._get_tile_directory(tile)
        self.canvas = canvas
        self.size = self._get_size(kwargs)
        self.sprite = self._resize(directory, self.size, self.size)
        self.canvas_image = self.canvas.create_image(kwargs['x'], kwargs['y'], image=self.sprite, anchor="nw")

    def _get_tile_directory(self, tile):
        image = 'img/brown_light_square.png'
        if tile == self.DARK_BROWN:
            image = 'img/brown_dark_square.png'
        elif tile == self.LIGHT_GREY:
            image = 'img/grey_light_square.png'
        elif tile == self.DARK_GREY:
            image = 'img/grey_dark_square.png'
        return image

    @staticmethod
    def _get_size(kwargs):
        if 'size' in kwargs:
            return kwargs['size']
        else:
            return int(360 / 8)

    @staticmethod
    def _resize(directory, width, height):
        img = Image.open(directory)
        img = img.resize((width, height), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(img)
        return photoImg


class Piece:
    def __init__(self, position, piece, colour, **kwargs):
        self.position = position
        self.piece_moves = []
        # a list of tuples (1, 0) and (2, 0) for a pawn on first go, context-free added to position
        self.size = self._get_size(kwargs)
        self.piece = piece
        self.colour = colour
        self.sprite = self._get_sprite()
        self.canvas_image = None

    @staticmethod
    def _resize(directory, width, height):
        img = Image.open(directory)
        img = img.resize((width, height), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(img)
        return photoImg

    @staticmethod
    def _get_size(kwargs):
        if 'size' in kwargs:
            return kwargs['size']
        else:
            return int(360/8)

    def _get_sprite(self):
        colour_suffix = ''
        if self.colour != 'black':
            colour_suffix = '_w'
        directory = 'img/' + self.piece + colour_suffix + '.png'
        return self._resize(directory, self.size, self.size)

    def inital_draw(self, canvas, x, y):
        canvas.create_image(x, y, image=self.sprite, anchor="nw")


class Pawn(Piece):
    def __init__(self, position, colour, **kwargs):
        super(Pawn, self).__init__(position, 'pawn', colour, **kwargs)


Chess()
