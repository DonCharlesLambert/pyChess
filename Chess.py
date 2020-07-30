from tkinter import *
from PIL import Image
from PIL import ImageTk

class Chess:
    WIDTH = 400
    HEIGHT = 400

    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()
        self.board = BoardTile(self.canvas, 0, x=200, y=200)
        window.mainloop()


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
        self.sprite = self.resize(image, int(400/8), int(400/8))
        self.canvas = canvas
        self.canvas.create_image(kwargs['x'], kwargs['y'], image=self.sprite)

    @staticmethod
    def resize(directory, width, height):
        img = Image.open(directory)
        img = img.resize((width, height), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(img)
        return photoImg

Chess()
