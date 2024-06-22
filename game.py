import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.geometry("300x200")
        self.master.configure(background="#f0f0f0")

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Choose your move:", font=("Arial", 14), fg="#00698f").pack(pady=10)

        button_frame = tk.Frame(self.master, bg="#f0f0f0")
        button_frame.pack()

        self.rock_image = ImageTk.PhotoImage(Image.open("rock.jpg"))
        self.paper_image = ImageTk.PhotoImage(Image.open("paper.jpg"))
        self.scissors_image = ImageTk.PhotoImage(Image.open("scissors.jpg"))

        moves = ['Rock', 'Paper', 'Scissors']
        for move in moves:
            if move == 'Rock':
                button = tk.Button(button_frame, image=self.rock_image, command=lambda m=move: self.play(m), 
                                   bg="#4CAF50", fg="white", font=("Arial", 12), width=10)
            elif move == 'Paper':
                button = tk.Button(button_frame, image=self.paper_image, command=lambda m=move: self.play(m), 
                                   bg="#4CAF50", fg="white", font=("Arial", 12), width=10)
            else:
                button = tk.Button(button_frame, image=self.scissors_image, command=lambda m=move: self.play(m), 
                                   bg="#4CAF50", fg="white", font=("Arial", 12), width=10)
            button.image = self.rock_image if move == 'Rock' else self.paper_image if move == 'Paper' else self.scissors_image
            button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 12), fg="#00698f")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.master, text="Score: You 0, Computer 0", font=("Arial", 12), fg="#00698f")
        self.score_label.pack()

    def play(self, user_choice):
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        winner = self.determine_winner(user_choice, computer_choice)
        self.update_score(winner)
        self.display_result(user_choice, computer_choice, winner)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif ((user_choice == 'Rock' and computer_choice == 'Scissors') or
              (user_choice == 'Scissors' and computer_choice == 'Paper') or
              (user_choice == 'Paper' and computer_choice == 'Rock')):
            return "user"
        else:
            return "computer"

    def update_score(self, winner):
        if winner == "user":
            self.user_score += 1
        elif winner == "computer":
            self.computer_score += 1
        self.score_label.config(text=f"Score: You {self.user_score}, Computer {self.computer_score}")

    def display_result(self, user_choice, computer_choice, winner):
        result = f"You chose {user_choice}. The computer chose {computer_choice}.\n"
        if winner == "tie":
            result += "It's a tie!"
        elif winner == "user":
            result += "You win!"
        else:
            result += "You lose!"
        self.result_label.config(text=result)

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if not play_again:
            self.master.quit()

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()