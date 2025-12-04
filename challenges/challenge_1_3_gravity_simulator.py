"""
Challenge 1.3: Gravity Simulator 🌍

Math Concept: Linear functions, acceleration
Physics Concept: Gravity (g = 9.8 m/s²)
Programming Concepts: Variables that change over time, delta time

Goal: Make objects fall with realistic gravity

Learning Outcomes:
- Understanding acceleration (velocity changes over time)
- Time-based movement (delta time)
- Real-world physics in code
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (20, 20, 30)
GROUND_COLOR = (100, 80, 60)
GROUND_HEIGHT = 50

# Physics constants
GRAVITY = 9.8  # m/s² (real Earth gravity)
PIXELS_PER_METER = 50  # Scale: 50 pixels = 1 meter
GRAVITY_PIXELS = GRAVITY * PIXELS_PER_METER / 60  # Convert to pixels per frame (at 60 FPS)

# Bounce damping constant
BOUNCE_DAMPING = 0.2  # Energy lost on bounce (0.7 = keeps 70% of velocity)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Challenge 1.3: Gravity Simulator!")

# Object class - this represents a falling object
class FallingObject:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        
        # Physics properties
        self.velocity_y = 0  # Current vertical velocity (pixels per frame)
        self.mass = radius  # Mass proportional to size
        
        # Track if object has hit ground
        self.on_ground = False
        
        # Track bounce count
        self.bounce_count = 0
    
    def update(self, delta_time):
        """Update object's position based on physics"""
        if not self.on_ground:
            # Apply gravity: velocity increases over time
            # v = v₀ + a*t (physics equation!)
            self.velocity_y = self.velocity_y + GRAVITY_PIXELS * delta_time
            
            # Update position: x = x₀ + v*t
            self.y = self.y + self.velocity_y * delta_time
            
            # Check if hit ground
            ground_y = WINDOW_HEIGHT - GROUND_HEIGHT
            if self.y + self.radius >= ground_y:
                # ADDED BOUNCE PHYSICS
                if abs(self.velocity_y) > 1:
                    # Reverse velocity and apply damping
                    self.velocity_y = -self.velocity_y * BOUNCE_DAMPING
                    self.bounce_count += 1
                    self.y = ground_y - self.radius  # Keep above ground
                    print(f"🔴 Bounce #{self.bounce_count}! Velocity: {self.velocity_y:.2f}")
                else:
                    # Final landing
                    self.y = ground_y - self.radius
                    self.on_ground = True
                    self.velocity_y = 0
                    if self.bounce_count > 0:
                        print(f"🛑 Object landed after {self.bounce_count} bounces")
                    else:
                        print(f"🛬 Object landed! Final velocity: {self.velocity_y:.2f} px/frame")
    
    def draw(self, surface):
        """Draw the object on the screen"""
        pygame.draw.circle(surface, self.color, 
                          (int(self.x), int(self.y)), 
                          self.radius)
        
        # Draw velocity indicator
        if not self.on_ground:
            end_y = int(self.y + self.velocity_y * 2)
            pygame.draw.line(surface, (255, 255, 0),
                           (int(self.x), int(self.y)),
                           (int(self.x), end_y), 2)

# Create some falling objects
objects = [
    FallingObject(150, 50, 20, (255, 100, 100)),   # Red ball
    FallingObject(300, 50, 30, (100, 255, 100)),   # Green ball
    FallingObject(450, 50, 15, (100, 100, 255)),   # Blue ball
    FallingObject(600, 50, 25, (255, 255, 100)),   # Yellow ball
]

print("🌍 Gravity Simulator started!")
print("💡 All objects fall with the same acceleration (g = 9.8 m/s²)")
print("💥 Objects now bounce with damping coefficient:", BOUNCE_DAMPING)
print("🖱️ Click to drop a new object!")

# Game loop
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 24)

while running:
    # Calculate delta time (time since last frame)
    delta_time = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Create new object at mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            import random
            radius = random.randint(15, 30)
            color = (random.randint(100, 255), 
                    random.randint(100, 255), 
                    random.randint(100, 255))
            objects.append(FallingObject(mouse_x, mouse_y, radius, color))
            print(f"➕ New object created at ({mouse_x}, {mouse_y})")
    
    # UPDATE: Update all objects
    for obj in objects:
        obj.update(delta_time)
    
    # DRAW: Clear screen
    screen.fill(BACKGROUND_COLOR)
    
    # Draw ground
    pygame.draw.rect(screen, GROUND_COLOR,
                    (0, WINDOW_HEIGHT - GROUND_HEIGHT, 
                     WINDOW_WIDTH, GROUND_HEIGHT))
    
    # Draw all objects
    for obj in objects:
        obj.draw(screen)
    
    # Draw info
    info_text = font.render(f"Gravity: {GRAVITY} m/s² | Objects: {len(objects)}", 
                           True, (255, 255, 255))
    screen.blit(info_text, (10, 10))
    
    # Updated physics text - ADDED BOUNCE INFO
    physics_text = font.render(f"Objects bounce with {BOUNCE_DAMPING*100:.0f}% energy conservation", 
                              True, (200, 200, 255))
    screen.blit(physics_text, (10, 35))
    
    pygame.display.flip()

pygame.quit()
sys.exit()

"""
🎓 Reflection Questions:
1. Why do all objects fall at the same rate, regardless of mass?
2. What would happen if we made gravity stronger? Weaker?
3. How does delta_time make the simulation frame-rate independent?
4. What's the difference between velocity and acceleration?
5. How does bounce damping affect the number of bounces?

🔬 Experiment Ideas:
- Change GRAVITY to simulate different planets
- Change BOUNCE_DAMPING to see different bounce behaviors
- Make objects bounce more times by increasing the bounce count limit
- Add air resistance (drag force)
- Add horizontal velocity for projectile motion
- Simulate moon gravity (1.6 m/s²) or Jupiter gravity (24.8 m/s²)

📚 Physics Connection:
This demonstrates Galileo's famous experiment - all objects fall 
at the same rate regardless of mass (in a vacuum)!
The bounce damping represents energy loss during collisions.
"""