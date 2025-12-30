import random
import time

def simulate_chess():
    print("GitHub Game Player - Chess Game")
    print("Loading...")
    print("Chess game simulation started!")
    print("White: Player 1, Black: Player 2")
    print("Standard chess rules apply")
    
    # Initial board setup (simplified representation)
    board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    
    def print_board():
        print("\n  a b c d e f g h")
        for i, row in enumerate(board):
            print(8-i, end=' ')
            for piece in row:
                print(piece, end=' ')
            print(8-i)
        print("  a b c d e f g h")
    
    def simulate_game():
        print("\nGame starting...")
        print_board()
        
        moves = 0
        max_moves = 20  # Simulate up to 20 moves
        white_turn = True
        
        while moves < max_moves:
            print(f"\n{'White' if white_turn else 'Black'}'s turn")
            
            # Simulate a move
            piece_moved = random.choice(['P', 'N', 'B', 'R', 'Q', 'K'])
            if not white_turn:
                piece_moved = piece_moved.lower()
            
            # Find a piece to move
            moved = False
            for i in range(8):
                for j in range(8):
                    if board[i][j] == piece_moved:
                        # Simple movement simulation
                        new_row = i + random.choice([-2, -1, 1, 2])
                        new_col = j + random.choice([-2, -1, 1, 2])
                        
                        # Check if move is within bounds
                        if 0 <= new_row < 8 and 0 <= new_col < 8:
                            # Check if destination is empty or has opponent's piece
                            if board[new_row][new_col] == '.' or \
                               (white_turn and board[new_row][new_col].islower()) or \
                               (not white_turn and board[new_row][new_col].isupper()):
                                
                                # Make the move
                                captured = board[new_row][new_col] != '.'
                                board[new_row][new_col] = board[i][j]
                                board[i][j] = '.'
                                
                                print(f"{'White' if white_turn else 'Black'} moved {board[new_row][new_col]} from {chr(97+j)}{8-i} to {chr(97+new_col)}{8-new_row}")
                                if captured:
                                    print(f"Captured {'Black' if white_turn else 'White'} piece!")
                                
                                moved = True
                                break
                if moved:
                    break
            
            if not moved:
                # If couldn't find a piece to move, try any valid piece
                for i in range(8):
                    for j in range(8):
                        piece = board[i][j]
                        if (white_turn and piece.isupper() and piece != '.') or \
                           (not white_turn and piece.islower() and piece != '.'):
                            
                            # Simple movement simulation
                            new_row = i + random.choice([-1, 1])
                            new_col = j + random.choice([-1, 1])
                            
                            # Check if move is within bounds
                            if 0 <= new_row < 8 and 0 <= new_col < 8:
                                # Check if destination is empty or has opponent's piece
                                if board[new_row][new_col] == '.' or \
                                   (white_turn and board[new_row][new_col].islower()) or \
                                   (not white_turn and board[new_row][new_col].isupper()):
                                    
                                    # Make the move
                                    captured = board[new_row][new_col] != '.'
                                    board[new_row][new_col] = board[i][j]
                                    board[i][j] = '.'
                                    
                                    print(f"{'White' if white_turn else 'Black'} moved {board[new_row][new_col]} from {chr(97+j)}{8-i} to {chr(97+new_col)}{8-new_row}")
                                    if captured:
                                        print(f"Captured {'Black' if white_turn else 'White'} piece!")
                                    
                                    moved = True
                                    break
                    if moved:
                        break
            
            print_board()
            
            # Check for checkmate (simplified)
            if random.random() > 0.95:  # 5% chance of game ending
                winner = "White" if white_turn else "Black"
                print(f"\nCheckmate! {winner} wins!")
                return
            
            white_turn = not white_turn
            moves += 1
            
            # Small delay to simulate game pace
            time.sleep(1)
        
        print("\nGame ended after maximum moves!")
        print("Result: Draw by move limit")
    
    simulate_game()

def main():
    print("GitHub Game Player - Chess Game")
    print("Loading...")
    
    simulate_chess()

if __name__ == "__main__":
    main()