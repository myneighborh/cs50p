import pygame

from src.config import CONFIG


class SoundManager:
    def __init__(self):
        self.hit_sound = pygame.mixer.Sound(CONFIG.hit_sound_path)
        self.hit_sound.set_volume(0.7)
        self.game_over_sound = pygame.mixer.Sound(CONFIG.game_over_sound_path)
        self.game_over_sound.set_volume(0.7)

    def play_hit(self):
        self.hit_sound.play()

    def play_game_over(self):
        self.game_over_sound.play()

    def stop_game_over(self):
        self.game_over_sound.stop()

    def play_bgm(self):
        pygame.mixer.music.load(CONFIG.bgm_path)
        pygame.mixer.music.set_volume(1.2)
        pygame.mixer.music.play(-1)

    def stop_bgm(self):
        pygame.mixer.music.stop()