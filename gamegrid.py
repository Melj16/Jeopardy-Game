#!/usr/bin/python
# gamegrid.py

'''class definition for grid graphics of game board'''

__author__ = "Melissa Jiang"
__version__ = "1.0"

import excelrd

class GameGrid:
    def __init__(self, num_categories, num_rows):
        self.columns = num_categories
        self.rows = num_rows

    def draw_gameboard(self, width, height, canvas):
        # write title
        canvas.create_text(width / 2, 50, font=("Helvetica", "48", "bold"), text="Jeopardy!", fill="white")

        # draw vertical lines of grid
        for i in range(self.columns + 1):
            canvas.create_line(((width - 100) / self.columns) * i + 50, 100, \
                               ((width - 100) / self.columns) * i + 50, height - 100, width=5)

        # draw horizontal lines of grid
        for i in range(self.rows + 1):
            canvas.create_line(50, ((height - 250) / self.rows) * i + 150, \
                               width - 50, ((height - 250) / self.rows) * i + 150, width=5)

        # draw top horizontal line of grid
        canvas.create_line(50, 100, width - 50, 100, width=5)

        # open excel file to find catagories
        file = "jeopardyinfo.xls"
        wb = excelrd.open_workbook(file)
        sht = wb.sheet_by_index(0)
        catagory_1 = sht.cell_value(1, 0)
        catagory_2 = sht.cell_value(4, 0)
        catagory_3 = sht.cell_value(7, 0)

        # write catagories
        canvas.create_text(((width - 100) / (2 * self.columns)) + 50, 125, font=("Helvetica", "20", "bold"),
                           text=str(catagory_1), fill="white")
        canvas.create_text((3 * width - 300) / (2 * self.columns) + 50, 125, font=("Helvetica", "20", "bold"),
                           text=str(catagory_2), fill="white")
        canvas.create_text((5 * width - 500) / (2 * self.columns) + 50, 125, font=("Helvetica", "20", "bold"),
                           text=str(catagory_3), fill="white")

        # write values
        for i in range(1, 6, 2):
            canvas.create_text(((i * width - i * 100) / (2 * self.columns)) + 50, (height - 250) /
                               (2 * self.rows) + 150, font=("Helvetica", "40", "bold"), text="$100",
                               fill="yellow", activefill="red", disabledfill="gray")
        for i in range(1, 6, 2):
            canvas.create_text(((i * width - i * 100) / (2 * self.columns)) + 50, (3 * height - 750) /
                               (2 * self.rows) + 150, font=("Helvetica", "40", "bold"), text="$200",
                               fill="yellow", activefill="red", disabledfill="gray")
        for i in range(1, 6, 2):
            canvas.create_text(((i * width - i * 100) / (2 * self.columns)) + 50, (5 * height - 1250) /
                               (2 * self.rows) + 150, font=("Helvetica", "40", "bold"), text="$300",
                               fill="yellow", activefill="red", disabledfill="gray")