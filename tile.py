#!/usr/bin/python
# question.py

'''class definition for questions'''

__author__ = "Melissa Jiang"
__version__ = "1.0"

import excelrd
import tkinter as tk
import string
import answered as asw
import scoreboard as sb


class Tile:
    def __init__(self, row):
        # open and read excel file
        file = "jeopardyinfo.xls"
        wb = excelrd.open_workbook(file)
        sht = wb.sheet_by_index(0)

        self.row = row
        self.category = sht.cell_value(row, 0)
        self.question = sht.cell_value(row, 1)
        self.answer = sht.cell_value(row, 2)
        self.value = sht.cell_value(row, 3)
        self.explanation = sht.cell_value(row, 4)

    def open_question_card(self, main_canvas, s):
        # create root window and canvas for question card
        question = self.question
        ans = str(self.answer)
        val = self.value
        expln = self.explanation
        q_window = tk.Tk()
        q_window.geometry("1000x500")
        q_window.title("Question!")
        canvas = tk.Canvas(q_window, bg="violet", width=1000, height=500)
        canvas.pack(side=tk.LEFT)
        canvas.create_text(500, 50, font=("Helvetica", "40", "bold"), text="Question:")
        canvas.create_text(500, 150, font=("Helvetica", "30"), text=str(question))

        # create input box for user
        lbl = tk.Label(q_window, font=("Helvetica", "17"), text="Your Answer: ")
        lbl.pack()
        lbl.place(x=380, y=220)
        entry = tk.Entry(q_window)
        entry.pack()
        entry.place(x=500, y=220)

        def check_answer():
            answer = str(entry.get())
            a = answer.lower()

            # get rid of special characters in the user's answer
            #for char in a:
                #if char in string.punctuation:
                    #a = a.replace(char, '')

            a_list = answer.split()
            submit.destroy()
            give_up.destroy()

            if ans == a:
                canvas.create_text(500, 370, text=("That is correct! " + expln))
                tk.Button(q_window, text="Continue", command=destroy_window).place(x=500, y=410)
                sb.Score.change_score(val)
            else:
                canvas.create_text(500, 370, text=("Sorry, that is incorrect. " + expln))
                tk.Button(q_window, text="Continue", command=destroy_window).place(x=500, y=410)
                sb.Score.change_score(-val)

            asw.Answered.answered[self.row - 1] = 1

            main_canvas.itemconfig(s, font=("Helvetica", "20"), text=("Score:", sb.Score.score))

        def destroy_window():
            q_window.destroy()
            asw.Answered.answered[self.row - 1] = 1
            should_end_game()

        # create submit button
        give_up = tk.Button(q_window, text='I give up :(', command=destroy_window)
        give_up.place(x=500, y=300)
        submit = tk.Button(q_window, text='Submit', command=check_answer)
        submit.place(x=500, y=260)

        def should_end_game():
            if asw.Answered.answered == [1, 1, 1,
                                         1, 1, 1,
                                         1, 1, 1]:
                end_game()
            else:
                pass

        def end_game():
            end_screen = tk.Tk()
            end_screen.title("Game Over")
            end_screen.geometry("500x500")
            can = tk.Canvas(end_screen, bg="lightgreen", width=500, height=500)
            can.pack(side=tk.LEFT)
            can.create_text(250, 250, text="You got $" + str(sb.Score.score))