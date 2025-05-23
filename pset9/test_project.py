import pygame
import pytest

from src.config import CONFIG
from src.star import Star
from src.player import Player


@pytest.fixture
def player():
    pygame.init()
    image = pygame.Surface((CONFIG.player_width, CONFIG.player_height))
    return Player(image)


@pytest.fixture
def star():
    return Star((1, 2))


def test_player_initial_position(player):
    assert player.rect.center == (CONFIG.width // 2, CONFIG.height // 2)


def test_star_initial_within_bounds(star):
    assert isinstance(star.speed_x, int)
    assert isinstance(star.speed_y, int)


def test_star_movement(star):
    old_x, old_y = star.x, star.y
    star.update()
    assert (star.x != old_x or star.y != old_y)


def test_star_collision(player, star):
    star.x, star.y = player.rect.center
    assert star.collides_with(player.rect)
