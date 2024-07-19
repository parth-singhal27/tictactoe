import tkinter as tk
from tkinter import messagebox

class IntroScreen:
    def __init__(self, root, start_callback):
        self.root = root
        self.start_callback = start_callback
        self.intro_frame = tk.Frame(self.root)
        self.intro_frame.pack()

        intro_label = tk.Label(self.intro_frame, text="Welcome to Tic-Tac-Toe", font=("Arial", 24))
        intro_label.pack(pady=20)

        start_button = tk.Button(self.intro_frame, text="Start Game", font=("Arial", 16), command=self.start_game)
        start_button.pack(pady=20)

    def start_game(self):
        self.intro_frame.pack_forget()
        self.start_callback()

    def show(self):
        self.intro_frame.pack()

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [[None for _ in range(3)] for _ in range(3)]

        self.x_wins = 0
        self.o_wins = 0

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.intro_screen = IntroScreen(self.root, self.start_game)

    def start_game(self):
        self.create_game_screen()

    def create_game_screen(self):
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        self.score_label = tk.Label(self.game_frame, text=self.get_score_text(), font=("Arial", 20))
        self.score_label.grid(row=0, column=0, columnspan=3, pady=(10, 0))

        for row in range(3):
            for col in range(3):
                button = tk.Button(self.game_frame, text="", font=("Arial", 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row + 1, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

        end_button = tk.Button(self.game_frame, text="End Game", font=("Arial", 16), command=self.end_game)
        end_button.grid(row=4, column=0, columnspan=3, pady=(10, 0))

    def on_button_click(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(self.current_player):
                if self.current_player == "X":
                    self.x_wins += 1
                else:
                    self.o_wins += 1
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.update_score()
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for row in range(3):
            if all(self.board[row][col] == player for col in range(3)):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)):
            return True

        if all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(self.board[row][col] is not None for row in range(3) for col in range(3))

    def reset_game(self):
        self.current_player = "X"
        self.board = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

    def update_score(self):
        self.score_label.config(text=self.get_score_text())

    def get_score_text(self):
        return f"Player X: {self.x_wins} wins | Player O: {self.o_wins} wins"

    def end_game(self):
        self.game_frame.pack_forget()
        self.intro_screen.show()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
