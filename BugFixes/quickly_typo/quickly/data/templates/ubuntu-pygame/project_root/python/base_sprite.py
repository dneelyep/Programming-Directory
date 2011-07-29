
"""
base_sprite - contains BaseSprite class.

"""

import pygame, random
from python_name import python_nameconfig

# pylint: disable=E1101

class BaseSprite(pygame.sprite.Sprite):
    """
    BaseSprite - handles all common sprite data and functionality
    for sprites in crashteroids.

    """

    def __init__(self, sprite_image):
        """Creates a BaseSprite. Sets the sprite's initial screen
        position, so this should be called by subclasses before they
        make any changes positioning.

        arguments:
        sprite_image - path to image file to use for the sprite.

        """

        #initialize member variables
        self.orientation = 0
        self._rotating_right = False
        self._rotating_left = False
        self.velocity_x = 0
        self.velocity_y = 0
        self._accelerating = False
        self.x = 0
        self.y = 0
        self.max_velocity = 50

        #acceleration_divisor determines how fast a sprite
        #accelerates. The hight the divisor, the slower the
        #acceleration.
        self.acceleration_divisor = 3 #accelerate at 1/3 speed

        #rotation_rate determines how many degrees the sprite will
        #rotate witch each tick while rotating. 
        self.rotation_rate = 15 #makes 360/14 = 24 orientations

        pygame.sprite.Sprite.__init__(self)
  
        #load the image and shave a few pixels from the rect
        #maintain a master image to avoid image corruption due to
        #multiple transformations of an image
        self.master_image = pygame.image.load(sprite_image)
        self.image = self.master_image
        self.rect = self.image.get_rect()

        #make the rect for the sprite slightly smaller than the
        #sprite image to accomedate non-rectangular images
        self.rect.height -= 5
        self.rect.width -= 5

        self._update_image()
        self.init_position()

    def center_on_screen(self):
        """center_on_screen - initializes values for positioning, and provides 
        a default position implemention, places the sprite in the center of
        the screen. This is an internal implementation that centers the 
        sprite. Use the default public implementation for a default
        implementation to be called externally.

        """

        self.orientation = 0
        self._rotating_right = False
        self._rotating_left = False
        self.velocity_x = 0
        self.velocity_y = 0
        self._accelerating = False
        self.x = python_nameconfig.screen_width / 2
        self.y = python_nameconfig.screen_height / 2
        self.max_velocity = 50
  
  
    def start_rotation_right(self):
        """
        start_rotation_right - set sprite to rotate clockwise by
        degrees set in rotation_rate on each call to update().

        """

        self._rotating_right = True

    def start_rotation_left(self):
        """
        start_rotation_left - set sprite to rotate counter-clockwise by
        degrees set in rotation_rate on each call to update().

        """
        self._rotating_left = True
  
    def stop_rotating_right(self):
        """
        stop_rotating_right - set the sprite to stop rotating on each tick

        """

        self._rotating_right = False
  
    def stop_rotating_left(self):
        """
        stop_rotating_right - set the sprite to stop rotating on each tick

        """

        self._rotating_left = False
 
    def accelerate(self):
        """
        accelerate - set the sprite to accelerate up to the max_acceleration
        on each tick

        """
        self._accelerating = True
  
    def stop_acceleration(self):
        """
        accelerate - set the sprite to stop accelateration
        on each tick

        """
        self._accelerating = False
  
    def update(self):
        """update - update internal data and position.
        Typically called by the game controller each game
        tick.

        """

        #update the orientation
        if self._rotating_left:
            self.orientation += self.rotation_rate
        if self.orientation >= 360:
            self.orientation = 0 

        if self._rotating_right:
            self.orientation -= self.rotation_rate
    
        if self.orientation < 0:
            self.orientation = 360 - self.rotation_rate
  
        #change the image if rotating
        if self._rotating_left or self._rotating_right:
            self._update_image()
  
        #adjust the velocity based on orientation
        up = 360/self.rotation_rate
        right = up/4
        down = up/2
        left = right * 3
        
        if self._accelerating:
            num = (up - self.orientation/self.rotation_rate) 
            if num == up:
                num = 0
            if num <= right:
                self.velocity_x += num
                self.velocity_y -= right - num
            elif num <= down:
                self.velocity_x += down - num
                self.velocity_y += num - right
            elif num <= left:
                self.velocity_x -= num - down
                self.velocity_y += left - num
            elif num < up:
                self.velocity_x -= up - num
                self.velocity_y -= num - left
  
        #set the velocity is within bounds
        if self.velocity_x > self.max_velocity:
            self.velocity_x = self.max_velocity
        if self.velocity_y > self.max_velocity:
            self.velocity_y = self.max_velocity
        if self.velocity_x < 0 - self.max_velocity:
            self.velocity_x = 0 - self.max_velocity
        if self.velocity_y < 0 - self.max_velocity:
            self.velocity_y = 0 - self.max_velocity
   
        #adjust the location, raise accelrationDivisor to slow down
        self.x += self.velocity_x/self.acceleration_divisor
        self.y += self.velocity_y/self.acceleration_divisor


        sw = python_nameconfig.screen_width
        sh = python_nameconfig.screen_height
        #wrap the sprite around the screen, maintain "hyper zone"
        if self.x > sw:
            self.x = 0 - self.rect.height
        if self.y > sh:
            self.y = 0 - self.rect.width
   
        if self.x < 0 - self.rect.width:
            self.x = sw
        if self.y < 0 - self.rect.height:
            self.y = sh
  
        self.rect.topleft = [self.x,self.y]
  
    def _update_image(self):
        """_update_image - internal function to manage updating
        a sprite's image. Maintains a master image to avoid image
        corruption after repeated rotations of the same image.        

        """

        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.master_image,self.orientation)
        self.rect = self.image.get_rect()
        #make a buffer so sprites can appear closer together
        self.rect.width -= 5
        self.rect.height -= 5
        self.rect.center = oldCenter
 
    def explode(self):
        """explode - function called when a sprite is destroyed
        in game play. Default implentation calls kill() which 
        simply removes the sprite from play. Subclasses of BaseSprite
        override explode to add explosion animations.

        """

        self.kill()#remove self from any spritegroups by default

    def init_position(self):
        """init_position - Typically called after a sprite is 
        created to place the sprite into game play. This defualt
        implementation places sprite randomly at the edges of the
        screen by calling random_perimeter_placement. 
        Sublclasess override this function to determine
        other start positions. This function can be modified to
        create different default start position logic for all
        sprites in the game.

        """

        self.random_perimeter_placement()

    def random_perimeter_placement(self):
        """init_position - Places sprite randomly at the edges of the
        screen. 

        """

        #leave room in the center for the guy
        sw = python_nameconfig.screen_width
        sh = python_nameconfig.screen_height

        quad = random.randint(0,3)
        if quad == 0:
            #top left
            right_bound = sw/2 - 100
            left_bound = 0
            bottom_bound = sh/2 - 100
            top_bound = 0

        if quad == 1:
            #top right
            right_bound = sw
            left_bound = sw/2 + 100
            bottom_bound = sh/2 - 100
            top_bound = 0
            
        if quad == 2:
            #bottom left
            right_bound = sw/2 - 100
            left_bound = 0
            bottom_bound = sh
            top_bound = sh/2 + 100
            
        if quad == 3:
            #bottom right
            right_bound = sw
            left_bound = sw/2 + 100
            bottom_bound = sh
            top_bound = sh/2 + 100

        self.x = random.randint(left_bound, right_bound)
        self.y = random.randint(top_bound, bottom_bound)
