from tkinter import *
from random import randint

choices = ["PAPER", "ROCK", "SCISSORS"]

class Application:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")
        master.geometry("300x100")

        self.userChoice = "User Choice"
        self.computerChoice = "Computer Choice"
        self.winner = ""

        self.userChoiceLabel = Label(master, text = self.userChoice, width = 20)
        self.computerChoiceLabel = Label(master, text = self.computerChoice, width = 20)
        self.winnerLabel = Label(master, text = self.winner, width = 20)

        self.userChoiceLabel.grid(row = 0, column = 0)
        self.computerChoiceLabel.grid(row = 1, column = 0)
        self.winnerLabel.grid(row = 2, column = 0)

        # The lambda function is a wrapper for the real function that gets executed. 
        self.rockButton = Button(master, text = 'ROCK', command = lambda: self.setRock())
        self.paperButton = Button(master, text = 'PAPER', command = lambda: self.setPaper())
        self.scissorsButton = Button(master, text = 'SCISSORS', command = lambda: self.setScissors())
        
        self.rockButton.grid(row = 0, column = 1)
        self.paperButton.grid(row = 1, column = 1)
        self.scissorsButton.grid(row = 2, column = 1)

    def setUserChoice(self, choice): self.userChoice = choice
    def getUserChoice(self): return self.userchoice

    def setComputerChoice(self, computer): self.computerChoice = computer
    def getComputerChoice(self): return self.computerChoice

    def setWinner(self, winner): self.winner = winner
    def getWinner(self): return self.winner

    def compare(self, user, computer):
        #print(user)
        #print(computer)
        if user == "ROCK":
            if computer == "ROCK":
                self.setWinner("TIE")
                self.winnerLabel.configure(text = "TIE")
                return "TIE"
            if computer == "PAPER":
                self.setWinner("LOSE")
                self.winnerLabel.configure(text = "YOU'RE A LOSE", bg = "red")
                return "LOSE"
            if computer == "SCISSORS":
                self.setWinner("WIN")
                self.winnerLabel.configure(text = "YOU'RE WINNER", bg = "green")
                return "WIN"
        elif user == "PAPER":
            if computer == "ROCK":
                self.setWinner("WIN")
                self.winnerLabel.configure(text = "YOU'RE WINNER", bg = "green")
                return "WIN"
            if computer == "PAPER":
                self.setWinner("TIE")
                self.winnerLabel.configure(text = "TIE")
                return "TIE"
            if computer == "SCISSORS":
                self.setWinner("LOSE")
                self.winnerLabel.configure(text = "YOU'RE A LOSE", bg = "red")
                return "LOSE"
        elif user == "SCISSORS":
            if computer == "ROCK":
                self.setWinner("LOSE")
                self.winnerLabel.configure(text = "YOU'RE A LOSE", bg = "red")
                return "LOSE"
            if computer == "PAPER":
                self.setWinner("WIN")
                self.winnerLabel.configure(text = "YOU'RE WINNER", bg = "green")
                return "WIN"
            if computer == "SCISSORS":
                self.setWinner("TIE")
                self.winnerLabel.configure(text = "TIE")
                return "TIE"
        else:
            self.setWinner("ERROR")
            self.winnerLabel.configure(text = "ERROR")
            return "ERROR"

    def createComputerChoice(self): 
        # Create the computer's choice using a random number
        computer = choices[randint(0, 2)]
        self.setComputerChoice(computer)
        self.computerChoiceLabel.configure(text = computer)

        # Compare the values to determine who wins
        whoWins = self.compare(self.userChoice, self.computerChoice)
        #print(self.winner)
        
    def setRock(self): 
        self.setUserChoice("ROCK")
        self.userChoiceLabel.configure(text = "User Choice: ROCK")
        print("ROCK")
        self.createComputerChoice()

    def setPaper(self): 
        self.setUserChoice("PAPER")
        self.userChoiceLabel.configure(text = "User Choice: PAPER")
        print("PAPER")
        self.createComputerChoice()

    def setScissors(self): 
        self.setUserChoice("SCISSORS")
        self.userChoiceLabel.configure(text = "User Choice: SCISSORS")
        print("SCISSORS")
        self.createComputerChoice()

    def getUserChoice(self):
        return userchoice

root = Tk()
my_gui = Application(root)
root.mainloop()
