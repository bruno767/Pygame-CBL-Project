"""
Challenge 1.1: Hello, Moving Circle! 🟢

Math Concept: Cartesian coordinates (x, y)
Programming Concepts: Variables, loops, basic graphics

Goal: Make a circle move across the screen

Learning Outcomes:
- Understand coordinate systems
- Learn about variables (position, velocity)
- See loops in action (game loop)
- First "wow!" moment: making something move
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants - these are values that won't change
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CIRCLE_RADIUS = 30
CIRCLE_COLOR = (0, 255, 0)  # RGB: Green
BACKGROUND_COLOR = (20, 20, 30)  # RGB: Dark blue-gray

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Challenge 1.1: Moving Circle!")

# Variables - these can change!
# Position: where the circle is on the screen
circle_x = 100  # x coordinate (horizontal position)
circle_y = 300  # y coordinate (vertical position)

# Velocity: how fast and in what direction the circle moves
velocity_x = 1  # pixels per frame moving right
velocity_y = 20  # pixels per frame moving down

# Game loop - this runs continuously
clock = pygame.time.Clock()
running = True

print("🎮 Game started! Watch the circle move!")
print("💡 Try changing velocity_x and velocity_y values to see what happens!")

while running:
    # Handle events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # UPDATE: Change the circle's position
    # This is the math part! We're adding velocity to position
    circle_x = circle_x + velocity_x  # Move horizontally
    circle_y = circle_y + velocity_y  # Move vertically
    
    # Bounce off edges (simple boundary check)
    if circle_x + CIRCLE_RADIUS > WINDOW_WIDTH or circle_x - CIRCLE_RADIUS < 0:
        velocity_x = -velocity_x  # Reverse horizontal direction
        print(f"💥 Bounced! New position: ({circle_x}, {circle_y})")
    
    if circle_y + CIRCLE_RADIUS > WINDOW_HEIGHT or circle_y - CIRCLE_RADIUS < 0:
        velocity_y = -velocity_y  # Reverse vertical direction
        print(f"💥 Bounced! New position: ({circle_x}, {circle_y})")
    
    # DRAW: Clear the screen and draw everything
    screen.fill(BACKGROUND_COLOR)  # Fill with background color
    
    # Draw the circle at position (circle_x, circle_y)
    pygame.draw.circle(screen, CIRCLE_COLOR, (int(circle_x), int(circle_y)), CIRCLE_RADIUS)
    
    # Update the display
    pygame.display.flip()
    
    # Control the speed of the game (frames per second)
    clock.tick(60)  # 60 FPS

# Clean up
pygame.quit()
sys.exit()

"""
🎓 Reflection Questions:
1. What happens if you change velocity_x to 10? What about -5?
2. What does the coordinate (0, 0) represent on the screen?
3. Why do we use int(circle_x) when drawing the circle?
4. What happens if you remove the boundary checks?

🔬 Experiment Ideas:
- Change CIRCLE_COLOR to a different RGB value
- Make the circle move faster or slower
- Add a second circle with different properties
- Change the window size
"""

