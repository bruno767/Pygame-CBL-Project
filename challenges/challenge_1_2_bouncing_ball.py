"""
Challenge 1.2: Bouncing Ball Physics ⚽

Math Concept: Reflection, velocity vectors
Physics Concept: Elastic collision
Programming Concepts: Conditionals (if/else), boundaries

Goal: Make a ball bounce off screen edges with realistic physics

Learning Outcomes:
- Conditional logic (if ball hits edge, reverse direction)
- Understanding boundaries
- Introduction to vectors (velocity as direction + speed)
"""

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BALL_RADIUS = 25
BALL_COLOR = (255, 100, 100)  # RGB: Red
BACKGROUND_COLOR = (20, 20, 30) 
BALL_2_RADIUS = 100
BALL_2_COLOR = (128, 0, 128)  # RGB: purple

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Challenge 1.2: Bouncing Ball Physics!")

# Ball 1  properties
ball_x = WINDOW_WIDTH // 2  # Start in the middle
ball_y = WINDOW_HEIGHT // 2


# Ball 2 properties
ball_2_x = WINDOW_WIDTH  # Start in top right
ball_2_y = 0

# Velocity vector: (speed_x, speed_y)
# This represents both direction AND speed
speed_x = 5
speed_y = -4  # Negative means moving up

speed_2_x = speed_x * 2
speed_2_y = speed_x * -1 

# Physics properties
bounce_damping = 0.98  # Energy loss on bounce (0.98 = 2% energy lost)
gravity = 0.2  # Gravity pulling down

print("⚽ Physics simulation started!")
print("💡 The ball will bounce with some energy loss (damping)")
print("🌍 Gravity is pulling the ball down")

# Game loop
clock = pygame.time.Clock()
running = True


# testing code 

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Bonus: Click to reset ball position
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ball_x, ball_y = pygame.mouse.get_pos()
            print(f"🖱️ Ball reset to: ({ball_x}, {ball_y})")
    
    # UPDATE: Apply physics
    
    # 1. Apply gravity (always pulling down)
    speed_y = speed_y + gravity
    speed_2_y = speed_2_y + gravity
    
    # 2. Update position based on velocity
    ball_x = ball_x + speed_x
    ball_y = ball_y + speed_y

    ball_2_x = ball_2_x + speed_2_x
    ball_2_y = ball_2_y + speed_2_y
    
    # 3. Check boundaries and bounce (with damping)
    # Right edge
    if ball_x + BALL_RADIUS > WINDOW_WIDTH:
        ball_x = WINDOW_WIDTH - BALL_RADIUS  # Keep ball on screen
        speed_x = -speed_x * bounce_damping  # Reverse and lose energy
        print(f"💥 Bounced ball 1 off right wall! Speed: {speed_x:.2f}")
    
    # Left edge
    elif ball_x - BALL_RADIUS < 0:
        ball_x = BALL_RADIUS
        speed_x = -speed_x * bounce_damping
        print(f"💥 Bounced ball 1 off left wall! Speed: {speed_x:.2f}")

    # right edge ball 2 
    if ball_x + BALL_2_RADIUS > WINDOW_WIDTH:  
        ball_2_x = WINDOW_WIDTH - BALL_2_RADIUS  # Keep ball on screen
        speed_2_x = -speed_2_x * bounce_damping  # Reverse and lose energy
        print(f"💥 Bounced ball 2  off right wall! Speed: {speed_2_x:.2f}")
    
    # Left edge
    elif ball_2_x - BALL_2_RADIUS < 0:
        ball_2_x = BALL_2_RADIUS
        speed_2_x = -speed_2_x * bounce_damping
        print(f"💥 Bounced ball 2 off left wall! Speed: {speed_2_x:.2f}")
    
    # Bottom edge
    if ball_y + BALL_RADIUS > WINDOW_HEIGHT:
        ball_y = WINDOW_HEIGHT - BALL_RADIUS
        speed_y = -speed_y * bounce_damping
        print(f"💥 Bounced off floor! Speed: {speed_y:.2f}")
    
    # Top edge
    elif ball_y - BALL_RADIUS < 0:
        ball_y = BALL_RADIUS
        speed_y = -speed_y * bounce_damping
        print(f"💥 Bounced off ceiling! Speed: {speed_y:.2f}")

    #  y vector direction change of ball 2 
    # Bottom edge
    if ball_2_y + BALL_2_RADIUS > WINDOW_HEIGHT:
        ball_2_y = WINDOW_HEIGHT - BALL_2_RADIUS
        speed_2_y = -speed_2_y * bounce_damping
        print(f"💥 Bounced ball 2 off floor! Speed: {speed_2_y:.2f}")
    
    # Top edge
    elif ball_2_y - BALL_2_RADIUS < 0:
        ball_2_y = BALL_2_RADIUS
        speed_2_y = -speed_2_y * bounce_damping
        print(f"💥 Bounced ball 2  off ceiling! Speed: {speed_2_y:.2f}")
    
    # DRAW: Clear and draw
    screen.fill(BACKGROUND_COLOR)
    
    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), BALL_RADIUS)
    pygame.draw.circle(screen, BALL_2_COLOR, (int(ball_2_x), int(ball_2_y)), BALL_2_RADIUS)
    
    # Draw velocity vector (optional visualization)
    # This shows the direction and magnitude of velocity
    end_x = int(ball_x + speed_x * 5)
    end_y = int(ball_y + speed_y * 5)
    pygame.draw.line(screen, (255, 255, 0), 
                     (int(ball_x), int(ball_y)), 
                     (end_x, end_y), 2)
    
    # Display info
    font = pygame.font.Font(None, 24)
    speed_text = font.render(f"Speed: ({speed_x:.1f}, {speed_y:.1f})", True, (255, 255, 255))
    screen.blit(speed_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

"""
🎓 Reflection Questions:
1. What happens if you set bounce_damping to 1.0? What about 0.5?
2. Why does the ball eventually stop bouncing?
3. How does gravity affect the ball's motion?
4. What's the difference between speed_x and ball_x?

🔬 Experiment Ideas:
- Change gravity to see different effects
- Make the ball bounce perfectly (damping = 1.0)
- Add multiple balls with different properties
- Create walls at angles (advanced!)
"""

