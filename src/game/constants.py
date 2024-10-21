WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)

WIDTH = 1500
HEIGHT = 800
FPS = 60
max_players = 3

# PHYSICAL CONSTANTS
g = 9.81  # Gravity (m/s^2)
R = 1   # Half the length of the bar in (m)
m_bar = 10.0  # Weight of the bar itself (kg)
damping = 0.01    # Damping factor
h = 1.2 # Vertical distance from the center of mass to the pivot point (m)
bar_length = R * 2  # Full length of the bar (m)

    ## Moment of inertia (including the bar's weight)
I_bar = (1/3) * m_bar * R**2 + m_bar * h**2
#I_weights = (wL + wR) * (R**2 + h**2)
I_weights = 0
I_total = I_bar + I_weights


# GEOMETRY
px_m = 150  # Pixels per meter
player_y_offset = 0.1*HEIGHT

bar_center_start = (HEIGHT // 2 - 1.5 * px_m) - player_y_offset  # Center of the bar at the start (pixels)
pivot_point = bar_center_start + h*px_m  # Pivot point of the bar (pixels) 
bar_length_px = bar_length * px_m  # Full length of the bar (pixels)
bar_thickness = 0.1 * px_m  # Thickness of the bar (for drawing) DEPRECATED
default_weight_size = bar_length/6 * px_m # Width of weight sprite (px)
weights_y_start = bar_center_start

    ## To draw Mr. Meeseeks
body_width = 1.7 * px_m
body_x_offset = 30
body_y = 0.62 * HEIGHT - player_y_offset
arms_y = 0.311 * HEIGHT - player_y_offset

    ## Safe margins
safe_margin_x = 0.8*body_width # Margin from the top and bottom of the screen (px)


# INITIAL CONDITIONS
theta = 0.0  # Initial angle (horizontal, 0 radians)
omega = 0.0  # Initial angular velocity
alpha = 0.0  # Initial angular acceleration
    ## Force applied by player TODO -> change this to depend on sensor signal (in loop below)
r_force = 0.5  # Distance from the pivot point to the force application point (m)