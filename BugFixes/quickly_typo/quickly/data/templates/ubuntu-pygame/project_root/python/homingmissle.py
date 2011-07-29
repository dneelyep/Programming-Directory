"""
homing_missle - contains the HomingMissle class, a sample sublcass
of BaseSprite

"""

import pygame
from python_name.base_sprite import BaseSprite
import math
from python_name import python_nameconfig

# pylint: disable=E1101

class HomingMissle(BaseSprite):
    """
    HomingMissle - A useful sample class that derives from BaseSprite and 
    has some very simple AI.

    """

    def __init__(self, target, img):
        """
        Create a HomingMissle. Useful as an enemy or as a weapon
        for the player.

        arguments:
        target - A sprite that the homing missle atempts to track down
        and shoot

        img - A path to an image to use for the missle

        """
 
        BaseSprite.__init__(self, img)
        self.init_position()
        self.target = target
        self._rotating_left = False
        self._rotating_right = False

        #the missle starts out moving
        self._accelerating = True

        #the missle starts out not knowing if it is
        #pointed at the target
        self.targetted = False
        self.explode_stage = 0
        self.exploding = False
        self.explosion_sound = pygame.mixer.Sound(python_nameconfig.enemy_explode_sound)
        self.points = 1

    def update(self):
        """update - update internal data and position.
        Typically called by the game controller each game
        tick.

        """

        BaseSprite.update(self)
        if self.exploding: 
            #do an explosion image for each tick
            self.explode_stage += 1
            e = self.explode_stage
            if e < 8:
                e = str(e)
                img_name = python_nameconfig.enemy_explode_stage + e  + ".png"
                self.master_image = pygame.image.load(img_name)
                self._update_image()
                return

            else:#explosion is done
                self.visible = False
                self.exploding = False
                self.kill()
                return

        self.targetted = False
        #calculate target angle
        targx = self.target.x - self.x
        targy = self.target.y - self.y
        target_angle = ((math.atan2(targy,targx)) * 180)/ math.pi
        if target_angle < 0:
            target_angle = 360 + target_angle
 
        #translate the orientation to the
        # same system as the target angle
        fire_angle = 360 - self.orientation
        if fire_angle == 360:
            fire_angle = 0
        fire_angle += 270
        if fire_angle >= 360:
            fire_angle -= 360

        #rotate to face the target
        delta = fire_angle - target_angle
        if delta > 5:
            self._rotating_left = True
            self._rotating_right = False
        elif delta < -5:
            self._rotating_left = False
            self._rotating_right = True
        else:
            self._rotating_left = False
            self._rotating_right = False
            self.targetted = True

    def explode(self):
        """explode - called when the homing missle is destroyed in
        game play. Sets a flag to start animating an explosion in the
        update function. Also plays the explosion sound.

        """

        self._accelerating = False
        self.velocity_x = 0
        self.velocity_y = 0
        if not self.exploding:
            self.explosion_sound.play()
            self.exploding = True

