import pygame
import sys

def main():
    pygame.init()
    
    # Constants
    WIDTH, HEIGHT = 800, 600
    PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90
    BALL_SIZE = 15
    PADDLE_SPEED = 7
    BALL_SPEED_X = 5
    BALL_SPEED_Y = 5
    
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    # Set up the display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("GitHub Game Player - Pong Game")
    clock = pygame.time.Clock()
    
    # Game objects
    left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    
    # Ball velocity
    ball_dx = BALL_SPEED_X
    ball_dy = BALL_SPEED_Y
    
    # Scores
    left_score = 0
    right_score = 0
    
    # Font
    font = pygame.font.Font(None, 74)
    
    print("GitHub Game Player - Pong Game")
    print("Loading...")
    print("Pong game started!")
    print("Controls: W/S for left paddle, Up/Down arrows for right paddle")
    print("First to 5 points wins!")
    
    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED
        
        # Ball movement
        ball.x += ball_dx
        ball.y += ball_dy
        
        # Ball collision with top and bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy = -ball_dy
        
        # Ball collision with paddles
        if ball.colliderect(left_paddle) and ball_dx < 0:
            ball_dx = -ball_dx
            # Add some angle based on where the ball hits the paddle
            relative_y = (left_paddle.centery - ball.centery) / (PADDLE_HEIGHT / 2)
            ball_dy = -relative_y * BALL_SPEED_Y
        
        if ball.colliderect(right_paddle) and ball_dx > 0:
            ball_dx = -ball_dx
            # Add some angle based on where the ball hits the paddle
            relative_y = (right_paddle.centery - ball.centery) / (PADDLE_HEIGHT / 2)
            ball_dy = -relative_y * BALL_SPEED_Y
        
        # Scoring
        if ball.left <= 0:
            right_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_dx = BALL_SPEED_X
            print(f"Right player scores! Score: {left_score}-{right_score}")
        
        if ball.right >= WIDTH:
            left_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_dx = -BALL_SPEED_X
            print(f"Left player scores! Score: {left_score}-{right_score}")
        
        # Check for winner
        if left_score >= 5 or right_score >= 5:
            winner = "Left" if left_score >= 5 else "Right"
            print(f"\n{winner} player wins the game! Final score: {left_score}-{right_score}")
            running = False
        
        # Drawing
        screen.fill(BLACK)
        
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
        
        # Draw scores
        left_text = font.render(str(left_score), True, WHITE)
        right_text = font.render(str(right_score), True, WHITE)
        screen.blit(left_text, (WIDTH // 4, 50))
        screen.blit(right_text, (3 * WIDTH // 4, 50))
        
        # Update display
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
    
    pygame.quit()
    print(f"Game ended! Final score: {left_score}-{right_score}")

if __name__ == "__main__":
    main()