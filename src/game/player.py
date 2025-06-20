import pygame
import os

class Player:
    def __init__(self, x, y, rows=2, cols=2, width=255, height=255):
        self.x = x
        self.y = y
        self.speed = 4
        self.flipped = False
        self.width = width
        self.height = height
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
        sprite_sheet = pygame.image.load(sprite_path).convert_alpha()
        frame_width = sprite_sheet.get_width() // cols
        frame_height = sprite_sheet.get_height() // rows
        frames = []
        for row in range(rows):
            for col in range(cols):
                frame = sprite_sheet.subsurface(
                    (col * frame_width, row * frame_height, frame_width, frame_height)
                )
                frame = pygame.transform.scale(frame, (self.width, self.height))
                # เพิ่มขอบ
                frame = add_outline(frame, color=(0,0,0), thickness=2)
                # หรือจะเบลอ
                frame = blur_surface(frame, scale_factor=0.9)
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

def add_outline(surface, color=(0,0,0), thickness=5):
    mask = pygame.mask.from_surface(surface)
    outline_surface = pygame.Surface(
        (surface.get_width() + thickness*2, surface.get_height() + thickness*2), pygame.SRCALPHA
    )
    for dx in range(-thickness, thickness+1):
        for dy in range(-thickness, thickness+1):
            if dx*dx + dy*dy <= thickness*thickness:
                outline_surface.blit(mask.to_surface(setcolor=color, unsetcolor=(0,0,0,0)), (dx+thickness, dy+thickness))
    outline_surface.blit(surface, (thickness, thickness))
    return outline_surface

def blur_surface(surface, scale_factor=0.7):
    w, h = surface.get_size()
    small = pygame.transform.smoothscale(surface, (int(w * scale_factor), int(h * scale_factor)))
    blurred = pygame.transform.smoothscale(small, (w, h))
    return blurred