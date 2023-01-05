import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (400, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Doodle Jump")

# Set the background color
bg_color = (0, 0, 0)

# Load the cat image
cat_image = pygame.image.load("cat.png")

# Create the player rectangle
player_rect = pygame.Rect(50, 50, 50, 50)

# Set the player's movement speed
player_speed = 5

# Set the player's jump height
jump_height = 20

# Set the gravity
gravity = 0.5

# Set the ground level
ground_level = 500

# Set the game font
font = pygame.font.Font(None, 36)

# Create a game clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys that are currently pressed
    keys = pygame.key.get_pressed()

    # Update the player's position based on the keys pressed
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= jump_height
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Apply gravity
    player_rect.y += gravity

    # Keep the player within the screen bounds
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > window_size[0]:
        player_rect.right = window_size[0]
    if player_rect.bottom > ground_level:
        player_rect.bottom = ground_level

    # Draw the background
    screen.fill(bg_color)

    # Draw the player
    screen.blit(cat_image, player_rect)

    # Draw the ground
    pygame.draw.rect(screen, (255, 255, 255), (0, ground_level, 400, 100))

    # Draw the score
    score_text = font.render("Score: {}".format(player_rect.y), 1, (255, 255, 255))

    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()
