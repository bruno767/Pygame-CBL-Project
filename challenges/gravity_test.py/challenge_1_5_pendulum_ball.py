import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pendulum Ball - Challenge 1.5")

# Colors
BACKGROUND = (25, 30, 40)
ARM_COLOR = (200, 200, 200)
BALL_COLOR = (255, 120, 120)

# Pendulum settings
origin = (WIDTH // 2, 100)  # fixed point on top
length = 300                # pendulum rod length
angle = math.pi / 4         # start angle (45°)
angular_velocity = 0
angular_acceleration = 0
gravity = 0.0009            # smaller = slower, smoother motion

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Pendulum physics ---
    # Formula: angular_acc = -(g / L) * sin(theta)
    angular_acceleration = -(gravity / length) * math.sin(angle)

    angular_velocity += angular_acceleration
    angle += angular_velocity

    # Slight damping (optional – keeps motion realistic)
    angular_velocity *= 0.999

    # Position of the ball
    ball_x = origin[0] + length * math.sin(angle)
    ball_y = origin[1] + length * math.cos(angle)

    # --- Drawing ---
    window.fill(BACKGROUND)

    # Draw the arm (line)
    pygame.draw.line(window, ARM_COLOR, origin, (ball_x, ball_y), 3)

    # Draw ball
    pygame.draw.circle(window, BALL_COLOR, (int(ball_x), int(ball_y)), 30)

    pygame.display.flip()
    clock.tick(60)
