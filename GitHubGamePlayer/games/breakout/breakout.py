#!/usr/bin/env python3
"""
Breakout game implementation
A classic arcade game where you break bricks with a bouncing ball
"""

import random
import time
import os

def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def breakout():
    """Main Breakout game function"""
    print("Welcome to Breakout!")
    print("Use A/D to move the paddle, Q to quit")
    input("Press Enter to start...")
    
    # Game dimensions
    width = 30
    height = 15
    
    # Game elements
    paddle_x = width // 2 - 2
    paddle_width = 5
    ball_x = width // 2
    ball_y = height // 2
    ball_dx = 1
    ball_dy = 1
    
    # Create bricks
    bricks = []
    for row in range(3):
        for col in range(8):
            bricks.append([col * 4 + 2, row + 2])
    
    score = 0
    
    while True:
        # Clear screen
        clear_screen()
        
        # Draw game board
        board = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Draw bricks
        for brick in bricks:
            if 0 <= brick[1] < height and 0 <= brick[0] < width:
                board[brick[1]][brick[0]] = '#'
                # Add adjacent brick parts
                if brick[0] + 1 < width:
                    board[brick[1]][brick[0]+1] = '#'
                if brick[0] + 2 < width:
                    board[brick[1]][brick[0]+2] = '#'
        
        # Draw paddle
        for i in range(paddle_width):
            px = paddle_x + i
            if 0 <= px < width:
                board[height - 2][px] = '='
        
        # Draw ball
        if 0 <= ball_y < height and 0 <= ball_x < width:
            board[ball_y][ball_x] = 'O'
        
        # Draw board
        print("+" + "-" * width + "+")
        for row in board:
            print("|" + ''.join(row) + "|")
        print("+" + "-" * width + "+")
        print(f"Score: {score}")
        print("Use A/D to move paddle, Q to quit")
        
        # Move ball
        new_ball_x = ball_x + ball_dx
        new_ball_y = ball_y + ball_dy
        
        # Wall collisions
        if new_ball_x <= 0 or new_ball_x >= width - 1:
            ball_dx = -ball_dx
            new_ball_x = ball_x + ball_dx
        if new_ball_y <= 0:
            ball_dy = -ball_dy
            new_ball_y = ball_y + ball_dy
        
        # Paddle collision
        if new_ball_y >= height - 3 and new_ball_y < height - 1:
            if paddle_x <= new_ball_x < paddle_x + paddle_width:
                ball_dy = -ball_dy
                new_ball_y = ball_y + ball_dy
                # Add some angle based on where the ball hits the paddle
                hit_pos = (new_ball_x - paddle_x) / paddle_width
                if hit_pos < 0.3:
                    ball_dx = -1
                elif hit_pos > 0.7:
                    ball_dx = 1
                else:
                    ball_dx = 0  # Make it more vertical if hitting center
        
        # Brick collisions
        hit_brick = False
        for brick in bricks[:]:  # Copy list to iterate safely
            # Check if ball is in the brick area (3 chars wide brick)
            if (brick[1] == new_ball_y and 
                brick[0] <= new_ball_x < brick[0] + 3):
                bricks.remove(brick)
                ball_dy = -ball_dy
                score += 10
                hit_brick = True
                break
        
        if hit_brick:
            new_ball_y = ball_y + ball_dy
        else:
            ball_x = new_ball_x
            ball_y = new_ball_y
        
        # Check if ball fell below paddle (lose condition)
        if ball_y >= height - 1:
            print("Game Over! Ball fell below the paddle.")
            print(f"Final Score: {score}")
            return
        
        # Check if all bricks are broken (win condition)
        if len(bricks) == 0:
            print("Congratulations! You broke all the bricks!")
            print(f"Final Score: {score}")
            return
        
        # Get user input
        print("\nMove paddle (A/D) or Q to quit: ", end='', flush=True)
        try:
            import sys, select
            if select.select([sys.stdin], [], [], 0.5)[0]:
                action = sys.stdin.read(1).lower()
            else:
                action = ''
        except:
            # Fallback for systems without select
            import time
            time.sleep(0.5)
            action = input().lower()
        
        if action == 'q':
            print("Thanks for playing!")
            print(f"Final Score: {score}")
            return
        elif action == 'a' and paddle_x > 0:
            paddle_x -= 1
        elif action == 'd' and paddle_x < width - paddle_width:
            paddle_x += 1

def simple_breakout():
    """A simplified version of Breakout that works with basic input"""
    print("Welcome to Simple Breakout!")
    print("Break all the bricks with the ball using your paddle!")
    
    input("Press Enter to start...")
    
    # Game setup
    width = 20
    height = 12
    paddle_x = width // 2 - 1
    paddle_width = 4
    ball_x = width // 2
    ball_y = height - 4
    ball_dx = 1
    ball_dy = -1
    
    # Create bricks
    bricks = []
    for row in range(2):
        for col in range(6):
            bricks.append([col * 3 + 2, row + 2])
    
    score = 0
    lives = 3
    
    for turn in range(100):  # Game ends after 100 turns if not won
        clear_screen()
        print(f"Score: {score} | Lives: {lives}")
        print("+" + "-" * width + "+")
        
        # Create the game grid
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Draw bricks
        for brick in bricks:
            if 0 <= brick[1] < height and 0 <= brick[0] < width:
                grid[brick[1]][brick[0]] = '#'
                if brick[0] + 1 < width:
                    grid[brick[1]][brick[0]+1] = '#'
        
        # Draw paddle
        for i in range(paddle_width):
            px = paddle_x + i
            if 0 <= px < width:
                grid[height - 2][px] = '='
        
        # Draw ball
        if 0 <= ball_y < height and 0 <= ball_x < width:
            grid[ball_y][ball_x] = 'O'
        
        # Draw grid
        for row in grid:
            print("|" + ''.join(row) + "|")
        
        print("+" + "-" * width + "+")
        print("Controls: A/D to move paddle, Q to quit")
        
        # Get user input
        action = input("Move (A/D) or Q to quit: ").lower()
        
        if action == 'q':
            print(f"Game Over! Final Score: {score}")
            return
        elif action == 'a' and paddle_x > 0:
            paddle_x -= 1
        elif action == 'd' and paddle_x < width - paddle_width:
            paddle_x += 1
        
        # Move ball
        new_ball_x = ball_x + ball_dx
        new_ball_y = ball_y + ball_dy
        
        # Wall collisions
        if new_ball_x <= 0 or new_ball_x >= width - 1:
            ball_dx = -ball_dx
            new_ball_x = ball_x + ball_dx
        if new_ball_y <= 0:
            ball_dy = -ball_dy
            new_ball_y = ball_y + ball_dy
        
        # Paddle collision
        if new_ball_y >= height - 3 and new_ball_y < height - 1:
            if paddle_x <= new_ball_x < paddle_x + paddle_width:
                ball_dy = -ball_dy
                new_ball_y = ball_y + ball_dy
        
        # Brick collisions
        hit_brick = False
        for brick in bricks[:]:  # Copy list to iterate safely
            if (brick[1] == new_ball_y and 
                brick[0] <= new_ball_x < brick[0] + 2):
                bricks.remove(brick)
                ball_dy = -ball_dy
                score += 10
                hit_brick = True
                break
        
        if hit_brick:
            new_ball_y = ball_y + ball_dy
        else:
            ball_x = new_ball_x
            ball_y = new_ball_y
        
        # Check if ball fell below paddle
        if ball_y >= height - 1:
            lives -= 1
            if lives <= 0:
                print("Game Over! You ran out of lives.")
                print(f"Final Score: {score}")
                return
            # Reset ball position
            ball_x = width // 2
            ball_y = height - 4
        
        # Check win condition
        if len(bricks) == 0:
            print("Congratulations! You broke all the bricks!")
            print(f"Final Score: {score}")
            return
        
        time.sleep(0.3)  # Slow down the game
    
    print(f"Game Over! Time's up! Final Score: {score}")

if __name__ == "__main__":
    simple_breakout()