import pygame
import math

def run_game():
    # Initialize pygame
    pygame.init()

    # Define constants
    WIDTH, HEIGHT = 800, 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BAR_WIDTH, BAR_HEIGHT = 200, 20  # Dimensions of the bar
    STEEL_DENSITY = 7850  # kg/m^3 (Density of steel)
    G = 9.81  # Gravitational constant
    DAMPING = 0.99  # Damping factor to simulate friction

    # Define the physics
    bar_mass = STEEL_DENSITY * BAR_WIDTH * BAR_HEIGHT * 1e-6  # mass in kg (assuming 1m length scale)
    moment_of_inertia = (1 / 12) * bar_mass * (BAR_WIDTH ** 2)  # Moment of inertia of a rectangle

    # Angular acceleration and velocity
    angular_velocity = 0
    angular_acceleration = 0
    gravity_acceleration = G / 1000  # Adjust gravity effect for visual scale

    # Axis of rotation (can be anywhere on the screen)
    AXIS_X = WIDTH // 2
    AXIS_Y = HEIGHT // 3

    # Setup display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rotating Bar with External Axis")

    # Clock to control frame rate
    clock = pygame.time.Clock()

    def draw_rotating_bar(surface, angle, width, height, axis_x, axis_y):
        """Draw the rectangular bar with a given rotation angle, maintaining its dimensions, rotating around the external axis."""
        bar = pygame.Surface((width, height), pygame.SRCALPHA)  # Allow transparency
        bar.fill(BLACK)
        
        # Rotate the bar around its center
        rotated_bar = pygame.transform.rotate(bar, angle)
        
        # Get the new rectangle position (but do not center it on screen, instead use axis as rotation point)
        rect = rotated_bar.get_rect(center=(axis_x, axis_y))
        
        # Blit the rotated bar to the surface
        surface.blit(rotated_bar, rect)

    # Main game loop
    running = True
    angle = 0  # Starting angle of rotation (0 means horizontal)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Input handling
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            # Increase angular acceleration
            angular_acceleration += 0.01
        elif keys[pygame.K_a]:
            # Decrease angular acceleration
            angular_acceleration -= 0.01
        else:
            # Apply gravitational torque when no input is given
            gravity_torque = -gravity_acceleration * math.sin(math.radians(angle))
            angular_acceleration = gravity_torque / moment_of_inertia

        # Update the angular velocity and angle
        angular_velocity += angular_acceleration
        angular_velocity *= DAMPING  # Apply damping to simulate friction/air resistance
        angle += angular_velocity

        # Keep the angle within the range of -180 to 180 degrees for easier control
        if angle > 180:
            angle -= 360
        elif angle < -180:
            angle += 360

        # Screen update
        screen.fill(WHITE)
        
        # Draw the axis point for reference
        pygame.draw.circle(screen, BLACK, (AXIS_X, AXIS_Y), 5)
        
        # Draw the rotating bar around the external axis
        draw_rotating_bar(screen, angle, BAR_WIDTH, BAR_HEIGHT, AXIS_X, AXIS_Y)
        
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

    # Quit pygame
    pygame.quit()