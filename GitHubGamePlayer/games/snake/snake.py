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
    
    try:
        while not game.game_over:
            game.draw()
            time.sleep(0.2)  # Game speed
            
            # In a real implementation, we would handle keyboard input
            # For this demo, we'll just move automatically
            game.move()
            
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
        return
    
    print(f"\nGame Over! Final Score: {game.score}")

if __name__ == "__main__":
    main()