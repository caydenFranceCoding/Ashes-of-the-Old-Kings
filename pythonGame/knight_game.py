import pygame
import sys

# Initialize Pygame
pygame.init()

# Check for initialization errors
if pygame.get_error():
    print(f"Pygame initialization error: {pygame.get_error()}")
    pygame.quit()
    sys.exit()

# Set window dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Knight's Adventure")

# Load the sprite sheet and convert alpha
try:
    spritesheet = pygame.image.load("character_sprite.png").convert_alpha()
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

# Define sprite dimensions
sprite_width = 16
sprite_height = 16

# Get the first idle sprite
knight_idle_frame = spritesheet.subsurface(pygame.Rect(0, 0, sprite_width, sprite_height))

# Scale the sprite to make it more visible
knight_scale = 3
knight_idle_scaled = pygame.transform.scale(knight_idle_frame, (sprite_width * knight_scale, sprite_height * knight_scale))
knight_rect = knight_idle_scaled.get_rect()
knight_rect.center = (screen_width // 2, screen_height // 2)

# Knight's movement speed
knight_speed = 5

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                knight_rect.x -= knight_speed
            elif event.key == pygame.K_RIGHT:
                knight_rect.x += knight_speed

    # Fill the background
    screen.fill((0, 128, 0))  # Green background

    # Draw the knight
    screen.blit(knight_idle_scaled, knight_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()