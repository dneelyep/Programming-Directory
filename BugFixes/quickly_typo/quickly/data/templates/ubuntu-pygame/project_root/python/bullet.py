"""
bullet module - Contains the Bullet class, which represents an
accelerating sprite that continues in a strait trajectory for a 
predetermined time period.

"""

import pygame, random
from python_name.base_sprite import BaseSprite
from python_name import python_nameconfig

# pylint: disable=E1101

class Bullet(BaseSprite):
    """
    Bullet - A sprite that represents a bullet that lacks AI. The
    default implementation starts the bullet in a straight line and
    continues for 10 game clicks or until it is removed from game
    play by colliding with a potential target.

    By default the bullet starts out still and quickly accellerates.
    To make a constant speed bullet, set the velocity_x and velocity_y
    as desired and set accelerating to False.
    
    """

    def __init__(self,x,y,orientation, img_name = None):
        """
        Creates a Bullet.

        arguments:
        x - the starting x position
        y - the starting y position
        orientation - the starting orientation for rotating the sprite image
        img_name - optional name for an image file to use for the sprite's
        master image. By default, the sprite will look for an image
        called 'bullet.png'.
 
        """
        img = python_nameconfig.default_bullet
        if img_name != None:
            img = img_name
        BaseSprite.__init__(self, img)
        self.launch_sound = pygame.mixer.Sound(python_nameconfig.guy_shoot_sound)
        self.launch_sound.play()
        self.explosionSound = pygame.mixer.Sound(python_nameconfig.guy_bullet_explode)
        self.orientation = orientation
        self.x = x
        self.y = y
        self._accelerating = True
        self.acceleration_divisor = .75
        self.max_velocity = 100
        self.max_ticks = 10
        self.ticks = 0
        self.exploding = False
        self.explodestage = 0
        self._update_image()
  
    def update(self):
        """update - update internal data and position.
        Typically called by the game controller each game
        tick.

        """

        BaseSprite.update(self)
        self.ticks += 1
        if not self.exploding and self.ticks > self.max_ticks:
            self.kill()

        if self.exploding: 
            self.explodestage += 1
            e = self.explodestage
            if e < 5:
                e = str(e)
                self.masterImage = pygame.image.load(python_nameconfig.bullet_explode_stage + e  + ".png")
                self._update_image()
            else:
                self.kill()
   
    def explode(self):
        """explode - called when the bullet is destroyed in
        game play. Sets the alive flag to False, and sets a flag to
        start animating an explosion in the update function. Also plays
        the bullet explosion sound.

        """

        self._accelerating = False
        self.velocity_x = 0
        self.velocity_y = 0
        self.explosionSound.play()
        self.exploding = True
   
