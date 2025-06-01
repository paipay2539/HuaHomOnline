import pygame
import os
from game.level import Level

# Initialize the game
pygame.init()

# Set up the game window
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D Game")

# ปรับขนาดตัวละคร (pixel scaling)
CHAR_WIDTH = 255   # กำหนดความกว้างที่ต้องการ
CHAR_HEIGHT = 255  # กำหนดความสูงที่ต้องการ

# Load character frames
def load_character_frames(rows=2, cols=2):
    sprite_path = os.path.join("src", "assets", "sprites", "huahom_basechar.png")
    sprite_sheet = pygame.image.load(sprite_path).convert()
    sprite_sheet.set_colorkey((255, 255, 255))  # ลบฉากสีขาว

    frame_width = sprite_sheet.get_width() // cols
    frame_height = sprite_sheet.get_height() // rows

    frames = []
    for row in range(rows):
        for col in range(cols):
            frame = sprite_sheet.subsurface(
                (col * frame_width, row * frame_height, frame_width, frame_height)
            )
            # ย่อขนาดเฟรม
            frame = pygame.transform.scale(frame, (CHAR_WIDTH, CHAR_HEIGHT))
            frames.append(frame)
    return frames

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
    # ตัวอย่าง level_data (แก้ไขตามที่ Level ต้องการ)
    level_data = [
        # เช่น ข้อมูลแผนที่, ตำแหน่งศัตรู ฯลฯ
    ]
    level = Level(level_data)

    frames = load_character_frames()
    frame_idx = 0
    frame_timer = 0
    frame_delay = 200  # ms ต่อเฟรม

    # ตำแหน่งตัวละคร (เริ่มกลางจอ)
    char_x = screen_width // 2
    char_y = screen_height // 2
    char_speed = 4  # ความเร็ว

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state
        level.update()

        # กดปุ่ม WASD เพื่อเดิน
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            char_x -= char_speed
        if keys[pygame.K_d]:
            char_x += char_speed
        if keys[pygame.K_w]:
            char_y -= char_speed
        if keys[pygame.K_s]:
            char_y += char_speed

        # อัปเดตอนิเมชั่น
        frame_timer += clock.get_time()
        if frame_timer >= frame_delay:
            frame_timer = 0
            frame_idx = (frame_idx + 1) % len(frames)

        # Draw everything
        screen.fill((0, 0, 0))  # Clear the screen with black
        screen.fill((255, 255, 255))  # Clear the screen with white
        level.draw(screen)

        # วาดตัวละคร
        char_img = frames[frame_idx]
        char_rect = char_img.get_rect(center=(char_x, char_y))
        screen.blit(char_img, char_rect)

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 frames per second

    pygame.quit()

if __name__ == "__main__":
    main()