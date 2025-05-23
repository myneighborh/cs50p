import random

import pygame

from src.config import CONFIG


class Star:
    def __init__(self, speed_range):
        self.speed_range = speed_range
        self.reset()

    def reset(self):
        side = random.choice(['top', 'bottom', 'left', 'right'])
        speed = random.randint(*self.speed_range)
        if side == 'top':
            self.x, self.y = random.randint(0, CONFIG.width), -CONFIG.star_radius * 2
            self.speed_x, self.speed_y = random.choice([-1, 0, 1]) * speed, speed
        elif side == 'bottom':
            self.x, self.y = random.randint(0, CONFIG.width), CONFIG.height + CONFIG.star_radius * 2
            self.speed_x, self.speed_y = random.choice([-1, 0, 1]) * speed, -speed
        elif side == 'left':
            self.x, self.y = -CONFIG.star_radius * 2, random.randint(0, CONFIG.height)
            self.speed_x, self.speed_y = speed, random.choice([-1, 0, 1]) * speed
        else:
            self.x, self.y = CONFIG.width + CONFIG.star_radius * 2, random.randint(0, CONFIG.height)
            self.speed_x, self.speed_y = -speed, random.choice([-1, 0, 1]) * speed

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # Reset the star
        if not -CONFIG.star_radius * 2 <= self.x <= CONFIG.width + CONFIG.star_radius * 2 or not -CONFIG.star_radius * 2 <= self.y <= CONFIG.height + CONFIG.star_radius * 2:
            self.reset()

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), CONFIG.star_radius)

    def collides_with(self, player_rect):
        return player_rect.collidepoint(int(self.x), int(self.y))