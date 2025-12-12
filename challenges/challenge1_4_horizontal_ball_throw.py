

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 600

# Colors
BACKGROUND_COLOR = (25, 30, 40)
BALL_COLOR = (255, 100, 100)
GROUND_COLOR = (80, 60, 40)
TEXT_COLOR = (220, 220, 220)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Horizontal Launch Simulation")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

# Physics CTEs
GRAVITY = 9.8  # m/s²
SCALE = 50     # 1 meter = 50 pixels
GRAVITY_PIXELS = GRAVITY * SCALE


class Ball:
    def __init__(self):
        # Starting values
        self.x = 100
        self.y = 100
        self.radius = 15

        # Velocities
        self.vx = 150
        self.vy = 0

        # State
        self.on_ground = False
        self.time = 0

        # Trajectory points
        self.trajectory = []

    def update(self, delta_t):
        
        
        # If stopped on the ground
        if self.on_ground:
            return
        
        # Time progression
        self.time += delta_t
        
        # Physics
        self.vy += GRAVITY_PIXELS * delta_t
        self.x += self.vx * delta_t
        self.y += self.vy * delta_t

        # Tajectory
        self.trajectory.append((self.x, self.y))
        if len(self.trajectory) > 80:
            self.trajectory.pop(0)

        # On ground
        ground_y = HEIGHT - 50 - self.radius
        if self.y >= ground_y:
            self.y = ground_y
            self.on_ground = True
            self.vx = 0
            self.vy = 0

    def draw(self, screen):
        
        
        # Draw fading trajectory
        if len(self.trajectory) > 1:
            for i in range(len(self.trajectory) - 1):
                alpha = int(255 * (i / len(self.trajectory)))
                trail_color = (255, 100, 100, alpha)

                surface = pygame.Surface(
                    (self.radius * 2, self.radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(surface, trail_color,
                                   (self.radius, self.radius),
                                   max(2, int(self.radius * 0.2)))

                px, py = self.trajectory[i]
                screen.blit(surface, (px - self.radius, py - self.radius))

        # Ball
        pygame.draw.circle(screen, BALL_COLOR,
                           (int(self.x), int(self.y)),
                           self.radius)

        # Outline
        pygame.draw.circle(screen, (255, 255, 255),
                           (int(self.x), int(self.y)),
                           self.radius, 2)


def draw_ground(screen):
    
    pygame.draw.rect(screen, GROUND_COLOR, (0, HEIGHT - 50, WIDTH, 50))


def draw_grid(screen):
    
    # Vertical lines
    for x in range(0, WIDTH, 50):
        pygame.draw.line(screen, (50, 55, 65), (x, 0),
                         (x, HEIGHT - 50), 1)
    # Horizontal lines
    for y in range(0, HEIGHT - 50, 50):
        pygame.draw.line(screen, (50, 55, 65), (0, y),
                         (WIDTH, y), 1)


def draw_info(screen, ball):
    
    pygame.draw.rect(screen, (0, 0, 0, 200), (10, 10, 300, 130))

    # Current values
    if not ball.on_ground:
        height = max(0, (HEIGHT - 50 - ball.y) / SCALE)
        dist = max(0, (ball.x - 100) / SCALE)
        vx_ms = ball.vx / SCALE
        vy_ms = ball.vy / SCALE
    else:
        height = 0
        dist = (ball.x - 100) / SCALE
        vx_ms = 0
        vy_ms = 0

    info = [
        f"Time: {ball.time:.2f} s",
        f"Distance: {dist:.2f} m",
        f"Height: {height:.2f} m",
        f"Vx: {vx_ms:.2f} m/s",
        f"Vy: {vy_ms:.2f} m/s",
        "Status: On ground" if ball.on_ground else "Status: In flight"
    ]

    for i, line in enumerate(info):
        text = font.render(line, True, TEXT_COLOR)
        screen.blit(text, (20, 20 + i * 22))


def main():
    ball = Ball()

    

    running = True
    while running:

        delta_t = clock.tick(60) / 1000.0

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Physics update
        ball.update(delta_t)

        # Rendering
        screen.fill(BACKGROUND_COLOR)
        draw_grid(screen)
        draw_ground(screen)
        ball.draw(screen)
        draw_info(screen, ball)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
