import pygame
import numpy as np
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# PHYSICAL CONSTANTS
g = 9.81  # Gravity (m/s^2)
R = 1   # Half the length of the bar in (m)
wL = 2.0  # Left weight (kg)
wR = 5.0  # Right weight (kg)
m_bar = 10.0  # Weight of the bar itself (kg)
damping = 0.01    # Damping factor
h = 1 # Vertical distance from the center of mass to the pivot point (m)
bar_length = R * 2  # Full length of the bar (m)

    ## Moment of inertia (including the bar's weight)
I_bar = (1/3) * m_bar * R**2 + m_bar * h**2
I_weights = (wL + wR) * (R**2 + h**2)
I_total = I_bar + I_weights


# GEOMETRY
px_m = 200  # Pixels per meter
pivot_point = (400, 300)  # Pivot point of the bar (pixels)
bar_center_start = (pivot_point[0] - R * px_m, pivot_point[1] + h * px_m)  # Center of the bar at the start (pixels)
bar_length_px = bar_length * px_m  # Full length of the bar (pixels)
bar_thickness = 0.05 * px_m  # Thickness of the bar (for drawing)


# INITIAL CONDITIONS
theta = 0.0  # Initial angle (horizontal, 0 radians)
omega = 0.0  # Initial angular velocity
alpha = 0.0  # Initial angular acceleration
    ## Force applied by player TODO -> change this to depend on sensor signal (in loop below)
r_force = 0.5  # Distance from the pivot point to the force application point (m)





def rotate_around_point(window, surf, theta, pivot):
    last_coords = np.array(surf.get_rect().center)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    r_pivot = last_coords - pivot
    rotated_rpivot = rotation_matrix @ (r_pivot)
    new_coords = pivot + rotated_rpivot
    return new_coords, pygame.transform.rotate(surf, np.degrees(theta))

def run_game():
    # Initialize Pygame
    pygame.init()

    # Window size and setup
    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Weightlifer Simulation")


    # Bar surface
    bar_surface = pygame.Surface((bar_length, bar_thickness), pygame.SRCALPHA)
    bar_surface.fill(WHITE)
    window_center = np.array([width // 2, height // 2])
    window.blit(bar_surface, window_center)

    # Simulation loop control
    running = True
    clock = pygame.time.Clock()

    # Main game loop
    last_time = time.time()

    while running:
        # Handle events (like quitting)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the state of all keys
        keys = pygame.key.get_pressed()

        applied_force = 0
        # Apply force based on key presses (A/D keys)
        if keys[pygame.K_a]:
            # Apply force in counterclockwise direction (negative torque)
            applied_force = 100
        if keys[pygame.K_d]:
            # Apply force in clockwise direction (positive torque)
            applied_force = -100

        # Calculate net torque due to gravity (only weights contribute to torque)
        tau_net = (wL - wR) * g * R
    
        # Add the torque from the perpendicular force
        tau_perpendicular = applied_force * r_force
        tau_total = tau_net + tau_perpendicular
        
        # Update angular acceleration
        alpha = tau_total / I_total
        
        dt = time.time() - last_time # Time step
        last_time = time.time()
        # Update angular velocity
        omega += alpha * dt
        
        # Update angle
        theta += omega * dt

        # Clear the screen
        window.fill(BLACK)

        # Rotate the bar and draw it
        rotated_rect, rotated_bar = rotate_around_point(window, bar_surface, theta, pivot_point)
        
        # Get the rectangle of the rotated bar and set its center to the pivot point
        window.blit(rotated_bar, rotated_rect)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()