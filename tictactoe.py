from tkinter import *

class Board():
    def __init__(self):
        self.who_move = "X"
        self.cells = ["","","","","","","","","",""]
        self.window = Tk(className=" TicTacToe")
        self.b1 = Button(self.window,text=self.cells[1], width=10, height=5, command=self.b1_pressed, bg="white")
        self.b1.grid(row=1, column=1)
        self.b2 = Button(self.window,text=self.cells[2], width=10, height=5, command=self.b2_pressed, bg="white")
        self.b2.grid(row=1, column=2)
        self.b3 = Button(self.window,text=self.cells[3], width=10, height=5, command=self.b3_pressed, bg="white")
        self.b3.grid(row=1, column=3)
        self.b4 = Button(self.window,text=self.cells[4], width=10, height=5, command=self.b4_pressed, bg="white")
        self.b4.grid(row=2, column=1)
        self.b5 = Button(self.window,text=self.cells[5], width=10, height=5, command=self.b5_pressed, bg="white")
        self.b5.grid(row=2, column=2)
        self.b6 = Button(self.window,text=self.cells[6], width=10, height=5, command=self.b6_pressed, bg="white")
        self.b6.grid(row=2, column=3)
        self.b7 = Button(self.window,text=self.cells[7], width=10, height=5, command=self.b7_pressed, bg="white")
        self.b7.grid(row=3, column=1)
        self.b8 = Button(self.window,text=self.cells[8], width=10, height=5, command=self.b8_pressed, bg="white")
        self.b8.grid(row=3, column=2)
        self.b9 = Button(self.window,text=self.cells[9], width=10, height=5, command=self.b9_pressed, bg="white")
        self.b9.grid(row=3, column=3)
        self.restartButton = Button(self.window, text="ReStart", width=33, height=3, command=self.restartButton_pressed, bg="grey")
        self.restartButton.grid(row=4, column=1, columnspan=3)
        self.result = Label(self.window, width=33, height=2, text="")
        self.result.grid(row=5, column=1, columnspan=3)

    def isWinner(self):
        if self.cells[1] == self.cells[2] == self.cells[3] != "":
            self.b1.config(bg="blue")
            self.b2.config(bg="blue")
            self.b3.config(bg="blue")
            return True
        elif self.cells[4] == self.cells[5] == self.cells[6] != "":
            self.b4.config(bg="blue")
            self.b5.config(bg="blue")
            self.b6.config(bg="blue")
            return True
        elif self.cells[7] == self.cells[8] == self.cells[9] != "":
            self.b7.config(bg="blue")
            self.b8.config(bg="blue")
            self.b9.config(bg="blue")
            return True
        elif self.cells[1] == self.cells[4] == self.cells[7] != "":
            self.b1.config(bg="blue")
            self.b4.config(bg="blue")
            self.b7.config(bg="blue")
            return True
        elif self.cells[2] == self.cells[5] == self.cells[8] != "":
            self.b2.config(bg="blue")
            self.b5.config(bg="blue")
            self.b8.config(bg="blue")
            return True
        elif self.cells[3] == self.cells[6] == self.cells[9] != "":
            self.b3.config(bg="blue")
            self.b6.config(bg="blue")
            self.b9.config(bg="blue")
            return True
        elif self.cells[1] == self.cells[5] == self.cells[9] != "":
            self.b1.config(bg="blue")
            self.b5.config(bg="blue")
            self.b9.config(bg="blue")
            return True
        elif self.cells[3] == self.cells[5] == self.cells[7] != "":
            self.b3.config(bg="blue")
            self.b5.config(bg="blue")
            self.b7.config(bg="blue")
            return True
        else:
            return False

    def finish_game(self):
        self.b1.config(state=DISABLED)
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)
        self.b4.config(state=DISABLED)
        self.b5.config(state=DISABLED)
        self.b6.config(state=DISABLED)
        self.b7.config(state=DISABLED)
        self.b8.config(state=DISABLED)
        self.b9.config(state=DISABLED)
        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        self.result.config(text=self.who_move + " wins!")

    def b1_pressed(self):
        self.cells[1]=self.who_move
        self.b1.config(text=self.cells[1], state = DISABLED)
        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        winner_exist = self.isWinner()
        if winner_exist:
            self.finish_game()


    def b2_pressed(self):
        self.cells[2]=self.who_move
        self.b2.config(text=self.cells[2], state = DISABLED)
        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        winner_exist = self.isWinner()
        if winner_exist:
            self.finish_game()

    def b3_pressed(self):
        self.cells[3] = self.who_move
        self.b3.config(text=self.cells[3], state=DISABLED)
        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        winner_exist = self.isWinner()
        if winner_exist:
            self.finish_game()

    def b4_pressed(self):
        self.cells[4] = self.who_move
        self.b4.config(text=self.cells[4], state=DISABLED)
        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        winner_exist = self.isWinner()
        if winner_exist:
            self.finish_game()

    def b5_pressed(self):
        self.cells[5] = self.who_move
        self.b5.config(text=self.cells[5], state=DISABLED)
        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        winner_exist = self.isWinner()
        if winner_exist:
            self.finish_game()

    def b6_pressed(self):
        self.cells[6] = self.who_move
        self.b6.config(text=self.cells[6], state=DISABLED)
        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        winner_exist = self.isWinner()
        if winner_exist:
            self.finish_game()

    def b7_pressed(self):
        self.cells[7] = self.who_move
        self.b7.config(text=self.cells[7], state=DISABLED)
        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        winner_exist = self.isWinner()
        if winner_exist:
            self.finish_game()

    def b8_pressed(self):
        self.cells[8] = self.who_move
        self.b8.config(text=self.cells[8], state=DISABLED)
        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        winner_exist = self.isWinner()
        if winner_exist:
            self.finish_game()

    def b9_pressed(self):
        self.cells[9] = self.who_move
        self.b9.config(text=self.cells[9], state=DISABLED)
        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        winner_exist = self.isWinner()
        if winner_exist:
            self.finish_game()

    def restartButton_pressed(self):
        self.cells = ["", "", "", "", "", "", "", "", "", ""]
        self.b1.config(text=self.cells[1], state=NORMAL, bg="white")
        self.b2.config(text=self.cells[2], state=NORMAL, bg="white")
        self.b3.config(text=self.cells[3], state=NORMAL, bg="white")
        self.b4.config(text=self.cells[4], state=NORMAL, bg="white")
        self.b5.config(text=self.cells[5], state=NORMAL, bg="white")
        self.b6.config(text=self.cells[6], state=NORMAL, bg="white")
        self.b7.config(text=self.cells[7], state=NORMAL, bg="white")
        self.b8.config(text=self.cells[8], state=NORMAL, bg="white")
        self.b9.config(text=self.cells[9], state=NORMAL, bg="white")
        self.result.config(text="")

Board()
mainloop()
