#!/usr/bin/env python3
"""
Tic Tac Toe game implementation
A classic two-player game
"""

def print_board(board):
    """Print the current game board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board):
    """Check if there's a winner"""
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != " ":
            return board[pattern[0]]
    return None

def is_board_full(board):
    """Check if the board is full (tie)"""
    return " " not in board

def tic_tac_toe():
    """Main Tic Tac Toe game function"""
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X, Player 2: O")
    
    board = [" "] * 9
    current_player = "X"
    
    while True:
        print_board(board)
        
        # Get valid move
        while True:
            try:
                move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Please enter a number between 1 and 9.")
                elif board[move] != " ":
                    print("That position is already taken!")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
        
        # Make move
        board[move] = current_player
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! Congratulations!")
            break
        
        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie! Good game!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()