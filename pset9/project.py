import sys

import pygame

# Import game configuration settings.
from src.config import CONFIG
# Import sound manager to handle game audio.
from src.sound import SoundManager
# Import Star class to represent falling stars.
from src.star import Star
# Import Player class to control the player character.
from src.player import Player


def main():
    # Initialize game state and objects.
    state = init()
    # Set the game state to initial values.
    reset_game(state)

    while True:
        # Process keyboard and quit events.
        handle_events(state)
        if state["running"]:
            # Update game logic (player, stars, collisions).
            update(state)
            # Render all objects to the screen.
            draw(state)
        else:
            if not state["game_over"]:
                # Show the title screen.
                draw_title(state)
            else:
                # Show game over screen.
                draw_game_over(state)

        # Refresh the display to show drawn content.
        pygame.display.flip()
        # Control frame rate.
        state["clock"].tick(CONFIG.fps if state["running"] else 15)


def init():
    # Start all imported pygame modules.
    pygame.init()
    # Initialize the mixer module for sound.
    pygame.mixer.init()
    
    # Set the game window size.
    screen = pygame.display.set_mode((CONFIG.width, CONFIG.height))
    # Set the game window title.
    pygame.display.set_caption("A Billion Stars Falling From the Sky")
    
    # Create a clock object to manage frame rate.
    clock = pygame.time.Clock()

    # Load the default font.
    font = pygame.font.Font(CONFIG.font_path, 36)
    # Load a larger font.
    large_font = pygame.font.Font(CONFIG.font_path, 48)

    # Load the player image.
    player_image = pygame.image.load(CONFIG.player_image_path).convert_alpha()
    # Resize player image.
    player_image = pygame.transform.scale(player_image, (CONFIG.player_width, CONFIG.player_height))
    # Create a Player.
    player = Player(player_image)

    # Load the background image for the title and game over screen.
    background_image = pygame.image.load(CONFIG.background_image_path)
    # Resize for screen.
    background_image = pygame.transform.scale(background_image, (CONFIG.width, CONFIG.height))

    # Create a SoundManager.
    sound = SoundManager()

    # Return all game state information as a dictionary.
    return {
        "screen": screen,
        "clock": clock,
        "font": font,
        "large_font": large_font,
        "player": player,
        "player_image": player_image,
        "background_image": background_image,
        "sound": sound,
        "stars": [],
        "difficulty_level": 1,
        "speed_range": (1, 2),
        "time_score": 0,
        "running": False,
        "game_over": False,
        "lives": CONFIG.player_max_lives,
        "best_time": 0,
        "music_started": False
    }


def reset_game(state):
    state["difficulty_level"] = 1
    state["speed_range"] = (1, 2)
    state["stars"] = [Star(state["speed_range"]) for _ in range(CONFIG.initial_star_count)]
    state["time_score"] = 0
    state["running"] = False
    state["game_over"] = False
    state["lives"] = CONFIG.player_max_lives
    state["best_time"] = 0


def draw_score(state):
    # Render time.
    time_text = state["font"].render(f"Time: {state["time_score"] // CONFIG.fps}s", True, (255, 255, 0))
    # Render lives.
    lives_text = state["font"].render(f"Lives: {state["lives"]}", True, (255, 100, 100))
    # Draw time on screen.
    state["screen"].blit(time_text, (10, 10))
    # Draw lives below time.
    state["screen"].blit(lives_text, (10, 50))


def increase_difficulty(state):
    # Every 20 seconds
    if state["time_score"] > 0 and state["time_score"] % (20 * CONFIG.fps) == 0:
        # Increment difficulty level.
        state["difficulty_level"] += 1
        # Calculate new star speed range.
        new_range = (1, 2 + state["difficulty_level"])
        # Add a new star.
        state["stars"].append(Star(new_range))
        # Update all stars with new speed.
        for star in state["stars"]:
            star.speed_range = new_range


def handle_events(state):
    for event in pygame.event.get():
        # Exit the program if the 'ESC' key is pressed.
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key_pressed = event.unicode.lower()
            # Start the game if the 'S' key is pressed.
            if key_pressed == "s" and not state["running"] and not state["game_over"]:
                state["running"] = True
                state["game_over"] = False
                if not state["music_started"]:
                    state["sound"].play_bgm()
                    state["music_started"] = True
            # Restart the game if the 'R' key is pressed.
            elif state["game_over"] and key_pressed == "r":
                reset_game(state)
                state["running"] = True
                state["sound"].stop_game_over()
                state["sound"].play_bgm()
                state["music_started"] = True


def update(state):
    # Increase time score.
    state["time_score"] += 1
    # Update player position.
    state["player"].update(pygame.key.get_pressed())
    # Update all stars.
    for star in state["stars"]:
        star.update()
        # If a star hits the player
        if star.collides_with(state["player"].rect):
            state["sound"].play_hit()
            state["lives"] -= 1
            star.reset()
            if state["lives"] <= 0:
                state["sound"].stop_bgm()
                state["sound"].play_game_over()
                state["running"] = False
                state["game_over"] = True
                state["best_time"] = max(state["best_time"], state["time_score"])
    # Adjust game difficulty.
    increase_difficulty(state)


def draw(state):
    state["screen"].fill((0, 0, 20))
    for star in state["stars"]:
        star.draw(state["screen"])
    state["player"].draw(state["screen"])
    draw_score(state)


def draw_title(state):
    screen = state["screen"]
    screen.blit(state["background_image"], (0, 0))
    title = state["large_font"].render("A Billion Stars", True, (255, 255, 0))
    title2 = state["large_font"].render("Falling From The Sky", True, (255, 255, 0))
    start = state["font"].render("Press S to start", True, (255, 255, 255))
    screen.blit(title, (CONFIG.width // 2 - title.get_width() // 2, CONFIG.height // 2 - 120))
    screen.blit(title2, (CONFIG.width // 2 - title2.get_width() // 2, CONFIG.height // 2 - 50))
    screen.blit(start, (CONFIG.width // 2 - start.get_width() // 2, CONFIG.height // 2 + 100))


def draw_game_over(state):
    screen = state["screen"]
    screen.blit(state["background_image"], (0, 0))
    game_over = state["large_font"].render("Game Over!", True, (255, 50, 50))
    restart = state["font"].render("Press R to Restart", True, (255, 255, 255))
    best = state["font"].render(f"Best Time: {state["best_time"] // CONFIG.fps}s", True, (255, 255, 0))
    screen.blit(game_over, (CONFIG.width // 2 - game_over.get_width() // 2, CONFIG.height // 2 - 120))
    screen.blit(best, (CONFIG.width // 2 - best.get_width() // 2, CONFIG.height // 2 - 50))
    screen.blit(restart, (CONFIG.width // 2 - restart.get_width() // 2, CONFIG.height // 2 + 100))


if __name__ == "__main__":
    main()
