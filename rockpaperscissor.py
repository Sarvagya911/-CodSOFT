import tkinter as tk
from random import choice

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("300x200")

        # Initialize scores
        self.player_score = 0
        self.computer_score = 0

        # Create score labels
        self.player_score_label = tk.Label(self.window, text="Player Score: 0")
        self.player_score_label.pack()

        self.computer_score_label = tk.Label(self.window, text="Computer Score: 0")
        self.computer_score_label.pack()

        # Create result label
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        # Create buttons
        self.rock_button = tk.Button(self.window, text="Rock", command=self.play_rock)
        self.rock_button.pack()

        self.paper_button = tk.Button(self.window, text="Paper", command=self.play_paper)
        self.paper_button.pack()

        self.scissors_button = tk.Button(self.window, text="Scissors", command=self.play_scissors)
        self.scissors_button.pack()

    def computer_choice(self):
        """Return a random choice from rock, paper, or scissors"""
        return choice(["rock", "paper", "scissors"])

    def play(self, player_choice):
        """Play a round of rock paper scissors"""
        computer_choice = self.computer_choice()
        if player_choice == computer_choice:
            self.result_label['text'] = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            self.player_score += 1
            self.player_score_label['text'] = f"Player Score: {self.player_score}"
            self.result_label['text'] = f"{player_choice.capitalize()} beats {computer_choice}! Player wins!"
        else:
            self.computer_score += 1
            self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"
            self.result_label['text'] = f"{computer_choice.capitalize()} beats {player_choice}! Computer wins!"

    def play_rock(self):
        """Play a round with rock as the player's choice"""
        self.play("rock")

    def play_paper(self):
        """Play a round with paper as the player's choice"""
        self.play("paper")

    def play_scissors(self):
        """Play a round with scissors as the player's choice"""
        self.play("scissors")

    def run(self):
        """Run the game"""
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()