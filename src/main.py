import pygame
import os
from game.level import Level

# Initialize the game
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D Game")

# Load assets
def load_assets():
    # Load sounds
    sounds_dir = os.path.join("src", "assets", "sounds")
    # Load sprites
    sprites_dir = os.path.join("src", "assets", "sprites")
    # Add loading logic here

# Main game loop
def main():
    load_assets()
    clock = pygame.time.Clock()
    level = Level()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state
        level.update()

        # Draw everything
        screen.fill((0, 0, 0))  # Clear the screen with black
        level.draw(screen)

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 frames per second

    pygame.quit()

if __name__ == "__main__":
    main()