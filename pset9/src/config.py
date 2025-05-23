from dataclasses import dataclass


@dataclass
class GameConfig:
    # Game settings
    width: int = 800
    height: int = 640
    fps: int = 60

    # Star settings
    star_radius: int = 5
    initial_star_count: int = 20

    # Player settings
    player_width: int = 50
    player_height: int = 40
    player_speed: int = 5
    player_max_lives: int = 5

    # Font path
    font_path: str = "/Users/hyun/dev_ws/pygame/assets/Exo2-BoldItalic.ttf"

    # Sound paths
    bgm_path: str = "/Users/hyun/dev_ws/pygame/assets/bgm.mp3"
    hit_sound_path: str = "/Users/hyun/dev_ws/pygame/assets/hit.wav"
    game_over_sound_path: str = "/Users/hyun/dev_ws/pygame/assets/game_over.wav"

    # Image paths
    player_image_path: str = "/Users/hyun/dev_ws/pygame/assets/player.png"
    background_image_path: str = "/Users/hyun/dev_ws/pygame/assets/background.png"


CONFIG = GameConfig()