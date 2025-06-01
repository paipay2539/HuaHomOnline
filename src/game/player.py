import pygame
import os

CHAR_WIDTH = 255
CHAR_HEIGHT = 255

class Player:
    def __init__(self, x, y, rows=2, cols=2):
        self.x = x
        self.y = y
        self.speed = 4
        self.flipped = False
        self.frames = self.load_frames(rows, cols)
        self.frame_idx = 0
        self.frame_timer = 0
        self.frame_delay = 100  # ms ต่อเฟรม

        # โหลดเสียงเดิน
        self.walk_sound = pygame.mixer.Sound(
            os.path.join("src", "assets", "sounds", "honma_run.wav")
        )
        self.walk_channel = None

    def load_frames(self, rows, cols):
        sprite_path = os.path.join("src", "assets", "sprites", "huahom_basechar_tranl.png")
        sprite_sheet = pygame.image.load(sprite_path).convert()
        sprite_sheet.set_colorkey((255, 255, 255))
        frame_width = sprite_sheet.get_width() // cols
        frame_height = sprite_sheet.get_height() // rows
        frames = []
        for row in range(rows):
            for col in range(cols):
                frame = sprite_sheet.subsurface(
                    (col * frame_width, row * frame_height, frame_width, frame_height)
                )
                frame = pygame.transform.scale(frame, (CHAR_WIDTH, CHAR_HEIGHT))   
                frames.append(frame)
        return frames

    def handle_input(self):
        keys = pygame.key.get_pressed()
        moving = False
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.flipped = False
            moving = True
        if keys[pygame.K_d]:
            self.x += self.speed
            self.flipped = True
            moving = True
        if keys[pygame.K_w]:
            self.y -= self.speed
            moving = True
        if keys[pygame.K_s]:
            self.y += self.speed
            moving = True

        # เล่นเสียงเดินวนลูปเมื่อเดิน
        if moving:
            if self.walk_channel is None or not self.walk_channel.get_busy():
                self.walk_channel = self.walk_sound.play(loops=-1)
        else:
            if self.walk_channel is not None and self.walk_channel.get_busy():
                self.walk_channel.stop()

    def update(self, dt):
        self.frame_timer += dt
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.frame_idx = (self.frame_idx + 1) % len(self.frames)

    def draw(self, surface):
        img = self.frames[self.frame_idx]
        if self.flipped:
            img = pygame.transform.flip(img, True, False)
        rect = img.get_rect(center=(self.x, self.y))
        surface.blit(img, rect)