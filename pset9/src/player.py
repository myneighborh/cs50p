import pygame

from src.config import CONFIG


class Player:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect(center=(CONFIG.width // 2, CONFIG.height // 2))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= CONFIG.player_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += CONFIG.player_speed
        if keys[pygame.K_UP]:
            self.rect.y -= CONFIG.player_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += CONFIG.player_speed
        self.rect.clamp_ip(pygame.Rect(0, 0, CONFIG.width, CONFIG.height))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)