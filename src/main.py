import pygame
import os
from game.level import Level
from game.player import Player

pygame.init()
pygame.mixer.init()
bgm_path = os.path.join("src", "assets", "sounds", "BGM_login_1.mp3")
pygame.mixer.music.load(bgm_path)
pygame.mixer.music.set_volume(0.1)  # ลดเสียงลงครึ่งหนึ่ง
pygame.mixer.music.play(-1)  # -1 = วนลูป

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D Game")

CHAR_WIDTH = 255
CHAR_HEIGHT = 255

def load_assets():
    pass

def main():
    load_assets()
    clock = pygame.time.Clock()
    level_data = []
    level = Level(level_data)
    player = Player(screen_width // 2, screen_height // 2, rows=2, cols=2)  # กำหนด rows, cols ได้

    running = True
    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        level.update()
        player.handle_input()
        player.update(dt)

        screen.fill((0, 0, 0))
        level.draw(screen)
        player.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()