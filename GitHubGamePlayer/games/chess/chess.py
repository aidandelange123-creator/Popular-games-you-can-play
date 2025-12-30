import pygame
import sys

# Chess game implementation
class ChessGame:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Constants
        self.WIDTH, self.HEIGHT = 560, 560
        self.SQUARE_SIZE = self.WIDTH // 8
        self.FPS = 60
        
        # Colors
        self.LIGHT_SQUARE = (240, 217, 181)
        self.DARK_SQUARE = (181, 136, 99)
        self.HIGHLIGHT = (124, 252, 0, 150)  # Light green with transparency
        self.SELECTED = (186, 202, 68, 150)  # Yellow-green with transparency
        
        # Set up display
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("GitHub Game Player - Chess Game")
        self.clock = pygame.time.Clock()
        
        # Initialize the board
        self.board = self.initialize_board()
        self.selected_piece = None
        self.valid_moves = []
        self.turn = 'white'  # White starts
        self.game_over = False
        self.winner = None
        
        # Font
        self.font = pygame.font.SysFont(None, 36)
        
    def initialize_board(self):
        # Create an 8x8 board with starting positions
        board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['..', '..', '..', '..', '..', '..', '..', '..'],
            ['..', '..', '..', '..', '..', '..', '..', '..'],
            ['..', '..', '..', '..', '..', '..', '..', '..'],
            ['..', '..', '..', '..', '..', '..', '..', '..'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        return board
    
    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = self.LIGHT_SQUARE if (row + col) % 2 == 0 else self.DARK_SQUARE
                pygame.draw.rect(self.screen, color, 
                                (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, 
                                 self.SQUARE_SIZE, self.SQUARE_SIZE))
                
                # Highlight selected piece and valid moves
                if self.selected_piece and self.selected_piece == (row, col):
                    s = pygame.Surface((self.SQUARE_SIZE, self.SQUARE_SIZE), pygame.SRCALPHA)
                    s.fill(self.SELECTED)
                    self.screen.blit(s, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif (row, col) in self.valid_moves:
                    s = pygame.Surface((self.SQUARE_SIZE, self.SQUARE_SIZE), pygame.SRCALPHA)
                    s.fill(self.HIGHLIGHT)
                    self.screen.blit(s, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
        
        # Draw pieces
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != '..':
                    self.draw_piece(piece, row, col)
    
    def draw_piece(self, piece, row, col):
        # Simple representation of chess pieces using letters
        piece_char = piece[1]
        color = (0, 0, 0) if piece[0] == 'b' else (255, 255, 255)
        
        # Get text surface
        text_surf = self.font.render(piece_char, True, color)
        text_rect = text_surf.get_rect()
        
        # Center the text in the square
        text_rect.center = (col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2,
                           row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2)
        
        self.screen.blit(text_surf, text_rect)
    
    def get_piece_color(self, piece):
        if piece == '..':
            return None
        return 'white' if piece[0] == 'w' else 'black'
    
    def get_piece_type(self, piece):
        if piece == '..':
            return None
        return piece[1]
    
    def get_valid_moves(self, row, col):
        piece = self.board[row][col]
        if piece == '..':
            return []
        
        piece_color = self.get_piece_color(piece)
        piece_type = self.get_piece_type(piece)
        
        # Only allow moves for the current player's turn
        if (piece_color == 'white' and self.turn != 'white') or \
           (piece_color == 'black' and self.turn != 'black'):
            return []
        
        moves = []
        
        if piece_type == 'p':  # Pawn
            direction = -1 if piece_color == 'white' else 1
            
            # Move forward
            new_row = row + direction
            if 0 <= new_row < 8 and self.board[new_row][col] == '..':
                moves.append((new_row, col))
                
                # Initial double move
                if (piece_color == 'white' and row == 6) or \
                   (piece_color == 'black' and row == 1):
                    new_row2 = row + 2 * direction
                    if self.board[new_row2][col] == '..':
                        moves.append((new_row2, col))
            
            # Capture diagonally
            for dc in [-1, 1]:
                new_col = col + dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target_piece = self.board[new_row][new_col]
                    if target_piece != '..' and self.get_piece_color(target_piece) != piece_color:
                        moves.append((new_row, new_col))
        
        elif piece_type == 'R':  # Rook
            # Horizontal and vertical moves
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row + dr, col + dc
                while 0 <= r < 8 and 0 <= c < 8:
                    target_piece = self.board[r][c]
                    if target_piece == '..':
                        moves.append((r, c))
                    elif self.get_piece_color(target_piece) != piece_color:
                        moves.append((r, c))
                        break
                    else:
                        break
                    r += dr
                    c += dc
        
        elif piece_type == 'N':  # Knight
            for dr, dc in [(2, 1), (2, -1), (-2, 1), (-2, -1), 
                           (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                r, c = row + dr, col + dc
                if 0 <= r < 8 and 0 <= c < 8:
                    target_piece = self.board[r][c]
                    if target_piece == '..' or self.get_piece_color(target_piece) != piece_color:
                        moves.append((r, c))
        
        elif piece_type == 'B':  # Bishop
            for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                r, c = row + dr, col + dc
                while 0 <= r < 8 and 0 <= c < 8:
                    target_piece = self.board[r][c]
                    if target_piece == '..':
                        moves.append((r, c))
                    elif self.get_piece_color(target_piece) != piece_color:
                        moves.append((r, c))
                        break
                    else:
                        break
                    r += dr
                    c += dc
        
        elif piece_type == 'Q':  # Queen
            # Combine rook and bishop moves
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), 
                           (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                r, c = row + dr, col + dc
                while 0 <= r < 8 and 0 <= c < 8:
                    target_piece = self.board[r][c]
                    if target_piece == '..':
                        moves.append((r, c))
                    elif self.get_piece_color(target_piece) != piece_color:
                        moves.append((r, c))
                        break
                    else:
                        break
                    r += dr
                    c += dc
        
        elif piece_type == 'K':  # King
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    r, c = row + dr, col + dc
                    if 0 <= r < 8 and 0 <= c < 8:
                        target_piece = self.board[r][c]
                        if target_piece == '..' or self.get_piece_color(target_piece) != piece_color:
                            moves.append((r, c))
        
        return moves
    
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.board[from_row][from_col]
        
        # Check if move is valid
        if (to_row, to_col) not in self.get_valid_moves(from_row, from_col):
            return False
        
        # Move the piece
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = '..'
        
        # Check for pawn promotion (simplified - always promote to queen)
        if piece[1] == 'p' and (to_row == 0 or to_row == 7):
            self.board[to_row][to_col] = piece[0] + 'Q'
        
        # Switch turns
        self.turn = 'black' if self.turn == 'white' else 'white'
        
        # Check for game over conditions (simplified)
        has_white_king = any('wK' in row for row in self.board)
        has_black_king = any('bK' in row for row in self.board)
        
        if not has_white_king:
            self.game_over = True
            self.winner = 'black'
        elif not has_black_king:
            self.game_over = True
            self.winner = 'white'
        
        return True
    
    def handle_click(self, pos):
        col = pos[0] // self.SQUARE_SIZE
        row = pos[1] // self.SQUARE_SIZE
        
        if self.selected_piece:
            # Try to move the selected piece
            if (row, col) in self.valid_moves:
                self.move_piece(self.selected_piece[0], self.selected_piece[1], row, col)
                self.selected_piece = None
                self.valid_moves = []
            elif self.board[row][col] != '..' and \
                 self.get_piece_color(self.board[row][col]) == self.turn:
                # Select a new piece
                self.selected_piece = (row, col)
                self.valid_moves = self.get_valid_moves(row, col)
            else:
                # Deselect
                self.selected_piece = None
                self.valid_moves = []
        else:
            # Select a piece if it's the current player's turn
            if self.board[row][col] != '..' and \
               self.get_piece_color(self.board[row][col]) == self.turn:
                self.selected_piece = (row, col)
                self.valid_moves = self.get_valid_moves(row, col)
    
    def run(self):
        print("GitHub Game Player - Chess Game")
        print("Loading...")
        print("Chess game started!")
        print("Click on a piece to select it, then click on a highlighted square to move.")
        print("White: Player 1, Black: Player 2")
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        self.handle_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            # Draw everything
            self.screen.fill((0, 0, 0))
            self.draw_board()
            
            # Draw game info
            turn_text = self.font.render(f"Turn: {self.turn.capitalize()}", True, (255, 255, 255))
            self.screen.blit(turn_text, (10, self.HEIGHT - 40))
            
            if self.game_over:
                winner_text = self.font.render(f"Game Over! {self.winner.capitalize()} wins!", True, (255, 255, 0))
                text_rect = winner_text.get_rect(center=(self.WIDTH//2, self.HEIGHT//2))
                pygame.draw.rect(self.screen, (0, 0, 0), text_rect.inflate(20, 10))
                self.screen.blit(winner_text, text_rect)
            
            pygame.display.flip()
            self.clock.tick(self.FPS)
        
        pygame.quit()
        if self.game_over:
            print(f"Game Over! {self.winner.capitalize()} wins!")
        else:
            print("Game ended by user.")

def main():
    game = ChessGame()
    game.run()

if __name__ == "__main__":
    main()