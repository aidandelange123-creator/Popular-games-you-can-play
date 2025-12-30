import random
import time
import os

class SnakeGame:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.snake = [(width//2, height//2)]
        self.direction = (1, 0)  # Start moving right
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False

    def generate_food(self):
        while True:
            food = (random.randint(0, self.width-1), random.randint(0, self.height-1))
            if food not in self.snake:
                return food

    def move(self):
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % self.width, (head_y + dy) % self.height)

        # Check if game over (snake hits itself)
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # Check if food eaten
        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop()

    def change_direction(self, new_direction):
        # Prevent 180-degree turns
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Score: {self.score}")
        print("+" + "-" * self.width + "+")
        
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Place snake
        for i, (x, y) in enumerate(self.snake):
            grid[y][x] = 'O' if i == 0 else 'o'  # Head is 'O', body is 'o'
        
        # Place food
        grid[self.food[1]][self.food[0]] = '*'
        
        for row in grid:
            print("|" + "".join(row) + "|")
        
        print("+" + "-" * self.width + "+")
        print("Use WASD to move. Press Ctrl+C to quit.")

def main():
    print("GitHub Game Player - Snake Game")
    print("Loading...")
    time.sleep(1)
    
    game = SnakeGame()
    
    # For Windows
    if os.name == 'nt':
        import msvcrt
        print("Use WASD to move. Press 'q' to quit.")
        try:
            while not game.game_over:
                game.draw()
                
                # Check for keyboard input
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    if key == 'q':
                        print("\nGame quit by user.")
                        return
                    elif key == 'w':
                        game.change_direction((0, -1))  # Up
                    elif key == 's':
                        game.change_direction((0, 1))   # Down
                    elif key == 'a':
                        game.change_direction((-1, 0))  # Left
                    elif key == 'd':
                        game.change_direction((1, 0))   # Right
                
                game.move()
                time.sleep(0.2)  # Game speed
                
        except KeyboardInterrupt:
            print("\nGame interrupted by user.")
            return
    else:
        # For Unix/Linux/MacOS - using curses
        import curses
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.keypad(True)
        curses.noecho()
        
        try:
            print("Use arrow keys to move. Press 'q' to quit.")
            while not game.game_over:
                # Refresh the screen
                stdscr.clear()
                stdscr.addstr(0, 0, f"Score: {game.score}")
                
                # Draw the game grid
                grid = [[' ' for _ in range(game.width)] for _ in range(game.height)]
                
                # Place snake
                for i, (x, y) in enumerate(game.snake):
                    grid[y][x] = 'O' if i == 0 else 'o'  # Head is 'O', body is 'o'
                
                # Place food
                grid[game.food[1]][game.food[0]] = '*'
                
                # Print the grid
                for i, row in enumerate(grid):
                    stdscr.addstr(i + 2, 0, "|" + "".join(row) + "|")
                
                stdscr.addstr(game.height + 3, 0, "Use arrow keys to move. Press 'q' to quit.")
                stdscr.refresh()
                
                # Get input
                key = stdscr.getch()
                if key == ord('q'):
                    print("\nGame quit by user.")
                    return
                elif key == curses.KEY_UP:
                    game.change_direction((0, -1))  # Up
                elif key == curses.KEY_DOWN:
                    game.change_direction((0, 1))   # Down
                elif key == curses.KEY_LEFT:
                    game.change_direction((-1, 0))  # Left
                elif key == curses.KEY_RIGHT:
                    game.change_direction((1, 0))   # Right
                
                game.move()
                time.sleep(0.2)  # Game speed
                
        except KeyboardInterrupt:
            print("\nGame interrupted by user.")
            return
        finally:
            curses.endwin()
    
    print(f"\nGame Over! Final Score: {game.score}")

if __name__ == "__main__":
    main()