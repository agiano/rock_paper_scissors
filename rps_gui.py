import random
import tkinter as tk

W = 0
T = 0
L = 0


def reset():
    label.config(text="Enter a choice (rock, paper, or scissors): ")


def update_score(result):
    global W, T, L
    if "win" in result:
        W += 1
    elif "lose" in result:
        L += 1
    elif "tie" in result:
        T += 1

    score.config(text=f"Score: {W} W - {T} T - {L} L")


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "rock beats scissors. you win"
        else:
            return "paper beats rock. you lose"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock. you win"
        else:
            return "scissors cuts paper. you lose"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper. you win"
        else:
            return "rock smashes scissors. you lose"
    else:
        return "Choose rock, paper, or scissors."


def on_enter(e):
    player = entry.get()

    computer = random.choice(["rock", "paper", "scissors"])
    result = check_win(player, computer)
    label.config(text=result)
    update_score(result)

    root.after(3000, reset)


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x350")

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=1)


label = tk.Label(
    root,
    text="Enter a choice (rock, paper, or scissors): ",
    font=("Times New Roman", 16),
)
label.grid(column=1, row=1, sticky="s")

entry = tk.Entry(root, width=30)
entry.grid(column=1, row=2, sticky="n")

score = tk.Label(root, text="Score: 0 W - 0 T - 0 L")
score.grid(column=1, row=3, sticky="n")

entry.bind("<Return>", on_enter)

root.mainloop()
