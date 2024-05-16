import tkinter as tk
from tkinter import messagebox

class 三目並べ:
    def __init__(self, master):
        self.master = master
        self.master.title("3目並べ")
        self.current_player = "○"  # 先行は○
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text="", width=5, height=2,
                                                font=("Helvetica", 20),  # フォントサイズを大きく設定
                                                command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("勝者", f"{self.current_player} の勝ちです！")
                self.reset_game()
            elif self.check_board_full():
                messagebox.showinfo("引き分け", "引き分けです！")
                self.reset_game()
            else:
                self.current_player = "×" if self.current_player == "○" else "○"  # 先行と後攻を交代

    def check_winner(self):
        # 行をチェック
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
        # 列をチェック
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != "":
                return True
        # 対角線をチェック
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_game(self):
        self.current_player = "○"  # 先行を○にリセット
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = 三目並べ(root)
    root.mainloop()