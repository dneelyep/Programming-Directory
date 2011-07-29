
"""
game module. Contains the Game class.

"""

import pygame
from python_name import python_nameconfig

class Game():
    """
    Game - manages game data and functions, such as lives, score,
    level and paused or unpaused.

    """
    def __init__(self):
        """
        Creates a new Game object. To start or restart the game
        use Game.reset()

        """
        self.lives = 0
        self.score = 0
        self.multiplier = 1
        self.free_guys_from_points = 1
        self.free_guy_at = 10
        self.free_guy_sound = pygame.mixer.Sound(python_nameconfig.free_guy_sound)
        self.paused = False
        self.playing = False

    def add_free_guy(self):
        """add_free_guy - increments the game's lives by 1 and plays a sound.
        Can by called due to the player scoring enough points, or called
        directly, for example due to a power.

        """

        self.lives += 1
        self.free_guy_sound.play()

    def increase_score(self, points):
        """increase_score - increase the score by the points specified. 
        Will increment points and aware free guys as needed

        arguments: points
        
        """

        self.score += points * self.multiplier
        if (self.free_guys_from_points * self.free_guy_at) < self.score:
            self.add_free_guy()
            self.free_guys_from_points += 1

    def reset(self):
        """reset - reset or start the game"""
        self.playing = True
        self.level = 0
        self.lives = 5
        self.score = 0
        self.multiplier = 1
        self.paused = False
