import pygame
import sys
import random

pygame.init()

# Check for initialization errors
if pygame.get_error():
    print(f"Pygame initialization error: {pygame.get_error()}")
    pygame.quit()
    sys.exit()

# Set window dimensions
screen_width = 1620
screen_height = 920
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Knight's Adventure")

# Load assets
try:
    spritesheet = pygame.image.load("knight.png")
    grass_tile = pygame.image.load("tileset-grassland-grass.png").convert()
    tree_image = pygame.image.load("Tree 1.png").convert_alpha()
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

# Define world size (optional)
world_width = 2000
world_height = 2000
tile_size = grass_tile.get_width() # Assuming square tiles

# Define sprite dimensions and load knight animations (as before)
sprite_width = 72
sprite_height = 72
transparent_color = (0, 0, 0)
knight_scale = 3
scaled_width = sprite_width * knight_scale
scaled_height = sprite_height * knight_scale
knight_idle_frame = spritesheet.subsurface(pygame.Rect(0, 0, sprite_width, sprite_height))
knight_idle_frame.set_colorkey(transparent_color)
knight_idle_scaled = pygame.transform.scale(knight_idle_frame, (scaled_width, scaled_height))
walk_frames = []
num_walk_frames = 2
for i in range(num_walk_frames):
    frame = spritesheet.subsurface(pygame.Rect(i * sprite_width, sprite_height, sprite_width, sprite_height))
    frame.set_colorkey(transparent_color)
    walk_frames.append(pygame.transform.scale(frame, (scaled_width, scaled_height)))

# Animation variables (as before)
current_frame = 0
animation_speed = 0.1
animation_timer = .1
is_moving = False
current_sprite = knight_idle_scaled
knight_speed = 0.2

# Knight's world position (float)
knight_world_x = float(world_width // 2 - scaled_width // 2)
knight_world_y = float(world_height // 2 - scaled_height // 2)

# Camera offset (integer)
camera_x = 0
camera_y = 0

# Generate random tree positions within the world
num_trees = 100
trees = []
for _ in range(num_trees):
    tree_x = random.randint(0, world_width - tree_image.get_width())
    tree_y = random.randint(0, world_height - tree_image.get_height())
    trees.append((tree_x, tree_y))

# Game loop
running = True
while running:
    # Event handling (as before)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                is_moving = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                is_moving = False
                current_sprite = knight_idle_scaled
                current_frame = 0

    # Update knight's world position (float)
    if is_moving:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            knight_world_x -= knight_speed
        if keys[pygame.K_RIGHT]:
            knight_world_x += knight_speed
        if keys[pygame.K_UP]:
            knight_world_y -= knight_speed
        if keys[pygame.K_DOWN]:
            knight_world_y += knight_speed

        # Update animation frame (as before)
        animation_timer += 0.5
        if animation_timer >= animation_speed:
            animation_timer = 0
            current_frame = (current_frame + 1) % len(walk_frames)
            current_sprite = walk_frames[current_frame]
    else:
        current_sprite = knight_idle_scaled

    # Calculate camera offset (integer) to keep knight centered
    camera_x = int(screen_width / 2 - (knight_world_x + scaled_width / 2))
    camera_y = int(screen_height / 2 - (knight_world_y + scaled_height / 2))

    # Draw the grass background by tiling
    for y in range(0, screen_height, tile_size):
        for x in range(0, screen_width, tile_size):
            screen_x = x + camera_x % tile_size - (tile_size if camera_x % tile_size > 0 else 0)
            screen_y = y + camera_y % tile_size - (tile_size if camera_y % tile_size > 0 else 0)
            screen.blit(grass_tile, (screen_x, screen_y))

    # Draw the trees relative to the camera
    for tree_x, tree_y in trees:
        screen_tree_x = int(tree_x + camera_x)
        screen_tree_y = int(tree_y + camera_y)
        screen.blit(tree_image, (screen_tree_x, screen_tree_y))

    # Calculate the knight's screen position (integer)
    knight_screen_x = int(knight_world_x + camera_x)
    knight_screen_y = int(knight_world_y + camera_y)

    # Draw the knight
    screen.blit(current_sprite, (knight_screen_x, knight_screen_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()