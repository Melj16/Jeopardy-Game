#!/usr/bin/python
# jeopardy.py

'''classic jeopardy game with tkinter'''

__author__ = "Melissa Jiang"
__version__ = "1.0"

import tkinter as tk
import gamegrid as gg
import tile
import answered as asw
import scoreboard as sb

# create root window and canvas with screen width and height
root = tk.Tk()
root.title("Jeopardy")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(str(w) + "x" + str(h))
canvas = tk.Canvas(root, bg="blue", width=w, height=h)
canvas.pack(side=tk.LEFT)


# use module GameGrid to draw game grid
grid = gg.GameGrid(3, 3)
grid.draw_gameboard(w, h, canvas)

# draw scoreboard
score = tk.IntVar(root)
s = canvas.create_text(60, 50, font=("Helvetica", "20"), text=("Score:", sb.Score.score))
scr_lbl = tk.Label(root, textvariable="score")


def grid_position(x, y):
    # get which row and column the user clicked on the jeopardy board
    row = ((y + (((h - 250) / 3) - 150)) // ((h - 250) / 3))
    col = ((x + (((w - 200) / 3) - 100)) // ((w - 200) / 3))
    return [int(row), int(col)]


def clicked(event):
    # get x and y coordinate of where user clicked
    x = event.x
    y = event.y

    # get row and column of user click
    user_click = grid_position(x, y)

    question_card(user_click)


canvas.bind("<Button-1>", clicked)


def question_card(user_click):
    # check if user has already clicked question

    if asw.Answered.answered[(user_click[0] - 1) + (user_click[1] - 1) * 3] == 0:

        # open question
        if user_click[1] == 1:
            q = tile.Tile(user_click[0])
            q.open_question_card(canvas, s)

        if user_click[1] == 2:
            q = tile.Tile(user_click[0] + 3)
            q.open_question_card(canvas, s)

        if user_click[1] == 3:
            q = tile.Tile(user_click[0] + 6)
            q.open_question_card(canvas, s)


tk.mainloop()
