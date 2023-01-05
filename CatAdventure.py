import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Cat's Adventure")

# Set the background color
bg_color = (0, 0, 0)

# Load the background image
bg_image = pygame.image.load("bg.png")

# Load the cat image
cat_image = pygame.image.load("cat.png")

# Create the cat rectangle
cat_rect = pygame.Rect(5, 500, 5, 5)

# Set the cat's movement speed
cat_speed = 5

# Load the enemy image
enemy_image = pygame.image.load("enemy.png")

# Create a list to store the enemy rectangles
enemies = []

# Set the enemy spawn rate
enemy_spawn_rate = 0.01

# Set the game font
font = pygame.font.Font(None, 36)

# Set the game over flag
game_over = False

# Create a game clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Get the keys that are currently pressed
    keys = pygame.key.get_pressed()

    # Update the cat's position based on the keys pressed
    if keys[pygame.K_LEFT]:
        cat_rect.x -= cat_speed
    if keys[pygame.K_RIGHT]:
        cat_rect.x += cat_speed
    if keys[pygame.K_UP]:
        cat_rect.y -= cat_speed
    if keys[pygame.K_DOWN]:
        cat_rect.y += cat_speed

    # Keep the cat within the screen bounds
    if cat_rect.left < 0:
        cat_rect.left = 0
    if cat_rect.right > window_size[0]:
        cat_rect.right = window_size[0]
    if cat_rect.top < 0:
        cat_rect.top = 0
    if cat_rect.bottom > window_size[1]:
        cat_rect.bottom = window_size[1]

    # Spawn enemies randomly
    if random.random() < enemy_spawn_rate:
        # Choose a random position for the enemy
        enemy_x = random.randint(0, window_size[0] - 50)
        enemy_y = random.randint(0, window_size[1] - 50)

        # Create the enemy rectangle
        enemy_rect = pygame.Rect(enemy_x, enemy_y, 5, 5)

        # Add the enemy rectangle to the list
        enemies.append(enemy_rect)

    # Update the enemy positions
    for enemy in enemies:
        enemy.y += 1

        # Remove enemies that have gone off the screen
        if enemy.bottom > window_size[1]:
            enemies.remove(enemy)

    # Draw the background image
    screen.blit(bg_image, (0, 0))

    # Draw the cat image
    # Downsize the cat image
    scaled_cat_image = pygame.transform.scale(cat_image, (50, 50))

    # Draw the scaled cat image
    screen.blit(scaled_cat_image, cat_rect)


    # Draw the enemies
    for enemy in enemies:
        screen.blit(enemy_image, enemy)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()
