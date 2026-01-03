#!/usr/bin/env python3
"""
Simple Space Invaders game
A text-based version of the classic arcade game
"""

import random
import time
import sys
import os

def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def space_invaders():
    """Main Space Invaders game function"""
    print("Welcome to Space Invaders!")
    print("Use A/D to move, SPACE to shoot, Q to quit")
    input("Press Enter to start...")
    
    # Game dimensions
    width = 30
    height = 15
    
    # Initial positions
    player_x = width // 2
    player_y = height - 1
    bullets = []
    invaders = []
    score = 0
    
    # Initialize invaders
    for i in range(3):
        for j in range(8):
            invaders.append([j*3 + 2, i + 2])
    
    # Game loop
    while True:
        # Clear screen
        clear_screen()
        
        # Draw game board
        board = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Place player
        board[player_y][player_x] = '^'
        
        # Place bullets
        for bullet in bullets:
            if 0 <= bullet[1] < height:
                board[bullet[1]][bullet[0]] = '|'
        
        # Place invaders
        for invader in invaders:
            if 0 <= invader[1] < height and 0 <= invader[0] < width:
                board[invader[1]][invader[0]] = 'M'
        
        # Draw board
        print("+" + "-" * width + "+")
        for row in board:
            print("|" + ''.join(row) + "|")
        print("+" + "-" * width + "+")
        print(f"Score: {score}")
        print("Use A/D to move, SPACE to shoot, Q to quit")
        
        # Move bullets
        new_bullets = []
        for bullet in bullets:
            new_bullet = [bullet[0], bullet[1] - 1]
            if new_bullet[1] >= 0:  # Bullet still on screen
                new_bullets.append(new_bullet)
        bullets = new_bullets
        
        # Move invaders randomly
        if random.random() < 0.3:  # 30% chance to move
            for invader in invaders:
                if random.random() < 0.5:  # 50% chance to move horizontally
                    direction = random.choice([-1, 1])
                    new_x = invader[0] + direction
                    if 0 <= new_x < width:
                        invader[0] = new_x
                else:  # 50% chance to move down
                    invader[1] += 1
        
        # Check collisions
        bullets_to_remove = []
        invaders_to_remove = []
        
        for i, bullet in enumerate(bullets):
            for j, invader in enumerate(invaders):
                if bullet[0] == invader[0] and bullet[1] == invader[1]:
                    if i not in bullets_to_remove and j not in invaders_to_remove:
                        bullets_to_remove.append(i)
                        invaders_to_remove.append(j)
                        score += 10
        
        # Remove hit invaders and bullets (in reverse order to maintain indices)
        for i in sorted(bullets_to_remove, reverse=True):
            if i < len(bullets):
                del bullets[i]
        for j in sorted(invaders_to_remove, reverse=True):
            if j < len(invaders):
                del invaders[j]
                # Add a new invader at the top
                invaders.append([random.randint(0, width-1), 1])
        
        # Check if invaders reached the bottom
        for invader in invaders:
            if invader[1] >= player_y:
                print("Game Over! The invaders reached you!")
                print(f"Final Score: {score}")
                return
        
        # Check for user input (simplified - in real implementation would use keyboard input)
        print("\nPress Enter to continue, 'q' to quit: ", end='', flush=True)
        try:
            import select
            if select.select([sys.stdin], [], [], 0.5)[0]:
                key = sys.stdin.read(1).lower()
            else:
                key = ''
        except:
            # Fallback for systems without select
            import time
            time.sleep(0.5)
            key = ''
        
        if key == 'q':
            print("Thanks for playing!")
            print(f"Final Score: {score}")
            return
        elif key == 'a' and player_x > 0:
            player_x -= 1
        elif key == 'd' and player_x < width - 1:
            player_x += 1
        elif key == ' ':
            # Shoot bullet
            bullets.append([player_x, player_y - 1])
        
        # If all invaders are destroyed, add more
        if len(invaders) == 0:
            for i in range(3):
                for j in range(8):
                    invaders.append([j*3 + 2, i + 2])

def simple_space_invaders():
    """A simplified version that works without advanced input handling"""
    print("Welcome to Simple Space Invaders!")
    print("This is a simplified version of the game.")
    print("You'll control a spaceship at the bottom of the screen.")
    print("Avoid the falling invaders and shoot them to earn points!")
    
    input("Press Enter to start...")
    
    score = 0
    lives = 3
    player_pos = 10
    invaders = [[random.randint(1, 19), 1] for _ in range(5)]
    bullets = []
    
    for turn in range(50):  # Game ends after 50 turns
        clear_screen()
        print(f"Score: {score} | Lives: {lives}")
        print("+" + "-" * 20 + "+")
        
        # Create the game grid
        grid = [['.' for _ in range(20)] for _ in range(10)]
        
        # Place player
        grid[9][player_pos] = '^'
        
        # Place invaders
        for invader in invaders:
            if 0 <= invader[1] < 10 and 0 <= invader[0] < 20:
                grid[invader[1]][invader[0]] = 'M'
        
        # Place bullets
        for bullet in bullets:
            if 0 <= bullet[1] < 10 and 0 <= bullet[0] < 20:
                grid[bullet[1]][bullet[0]] = '|'
        
        # Draw grid
        for row in grid:
            print("|" + ''.join(row) + "|")
        
        print("+" + "-" * 20 + "+")
        print("Controls: A/D to move left/right, S to shoot, Q to quit")
        
        # Get user input
        action = input("Action (A/D/S/Q): ").lower()
        
        if action == 'q':
            print(f"Game Over! Final Score: {score}")
            return
        elif action == 'a' and player_pos > 0:
            player_pos -= 1
        elif action == 'd' and player_pos < 19:
            player_pos += 1
        elif action == 's':
            bullets.append([player_pos, 8])  # Add bullet above player
        
        # Move invaders down
        for invader in invaders:
            invader[1] += 1
        
        # Move bullets up
        new_bullets = []
        for bullet in bullets:
            bullet[1] -= 1
            if bullet[1] >= 0:  # Bullet still on screen
                new_bullets.append(bullet)
        bullets = new_bullets
        
        # Check collisions
        hit_invaders = []
        hit_bullets = []
        
        for i, bullet in enumerate(bullets):
            for j, invader in enumerate(invaders):
                if bullet[0] == invader[0] and bullet[1] == invader[1]:
                    if j not in hit_invaders and i not in hit_bullets:
                        hit_invaders.append(j)
                        hit_bullets.append(i)
                        score += 10
        
        # Remove hit invaders and bullets
        for i in sorted(hit_invaders, reverse=True):
            if i < len(invaders):
                del invaders[i]
        for i in sorted(hit_bullets, reverse=True):
            if i < len(bullets):
                del bullets[i]
        
        # Check if invaders reached the bottom
        for invader in invaders:
            if invader[1] >= 9:  # Reached player's row
                if invader[0] == player_pos:  # Hit player
                    lives -= 1
                    if lives <= 0:
                        print("Game Over! You've been hit too many times!")
                        print(f"Final Score: {score}")
                        return
                invaders.remove(invader)  # Remove the invader that reached bottom
                invaders.append([random.randint(1, 19), 1])  # Add new invader
        
        # Add new invaders periodically
        if turn % 10 == 0:
            invaders.append([random.randint(1, 19), 0])
        
        time.sleep(0.3)  # Slow down the game
    
    print(f"Game Over! You survived all waves! Final Score: {score}")

if __name__ == "__main__":
    simple_space_invaders()