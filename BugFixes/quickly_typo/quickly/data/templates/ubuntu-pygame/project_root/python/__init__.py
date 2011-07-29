#! /usr/bin/env python
import pygame, random

#import classes from the python_name library
from python_name.base_sprite import BaseSprite
from python_name.guy import Guy
from python_name.enemy import Enemy
from python_name.homingmissle import HomingMissle
from python_name.game import Game
from python_name import hiscores
import python_name.python_nameconfig

#set up translations
import gettext
from gettext import gettext as _
gettext.textdomain('project_name')

#initialize pygame and ther libraries
pygame.font.init()
pygame.mixer.init()
random.seed()

sw = python_name.python_nameconfig.screen_width
sh = python_name.python_nameconfig.screen_height

#setup the display
screen = pygame.display.set_mode((sw, sh))
background = pygame.image.load(python_name.python_nameconfig.background_image)
pygame.mouse.set_visible(False)

#set up some objects and models
clock = pygame.time.Clock() 
font = pygame.font.Font(None, 24)
game = Game()
game.level = 0

#create the player's guy and some enemies
bullets = pygame.sprite.RenderUpdates()
guys = pygame.sprite.RenderUpdates()
enemies = pygame.sprite.RenderUpdates()
g = Guy(bullets)
guys.add(g)

def update_hiscore_screen():
    """Update the hiscore screen."""
    hiscores_size = python_name.python_nameconfig.hiscores_size
    hiscores.screen = hiscores.hiscores_screen(hiscores_size)
    screen_center = screen.get_rect().center
    hiscores.pos = hiscores.screen.get_rect(center=screen_center)

def next_level():
    """next_level - go to the next game level
    after completing the previous level

    """

    game.level += 1
    enemies.empty()

    #TODO: set up enemies here
    #You can add more enemies or use different enemies
    #depening on the level
    for i in xrange(0,1):
        enemies.add(Enemy())
    enemies.add(HomingMissle(g,python_name.python_nameconfig.homing_missle_image))

def reset_level():
    """reset_level - reset the current level after the player's 
    guy has died, and is done exploding

    """

    #The guy is done exploding, so decrement the level and 
    #and reset the guy
    game.lives -= 1
    g.explodestage = 0 #he's done exploding
    guys.add(g) #make him live again
    g.visible = True
    g.init_position()

def controller_tick():
    """controller_tick - collect user input and update data

    """
    
    #handle starting the game or quiting the game if the game
    #is over or has not started
    if game.lives < 1:
        if game.playing:
            game.playing = False
            hiscores.save_score(game.score, game.level)
            update_hiscore_screen()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
                if event.key == 13:
                    game.reset()
                    next_level()
                    return 1
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen() 
                    return 1

    #if the guy has been killed and the explosion is over
    #reset the level
    if(not g.alive() and not g.exploding):
        reset_level()
 
    #if all the enemies are kill and there are more lives,
    #go to the next level
    if len(enemies) == 0 and not game.lives < 1:
        next_level()

    #respond to user input if the game is not over
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        #key down events, typically initiate actions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 0
   
            #pause or unpause
            if event.key == pygame.K_p:
                game.paused = not game.paused
   
            #control the guy
            if not game.paused: 
                if event.key == pygame.K_f:
                    g.start_rotation_right()
                if event.key == pygame.K_s:
                    g.start_rotation_left()
                if event.key == pygame.K_l:
                    g.accelerate()
                if event.key == pygame.K_j:
                    g.shoot()
                if event.key == pygame.K_SPACE:
                    g.hyperspace()
     
        #key up events, typically stop actions
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen() 
            if event.key == pygame.K_f:
                g.stop_rotating_right()
            if event.key == pygame.K_s:
                g.stop_rotating_left()
            if event.key == pygame.K_l:
                g.stop_acceleration()    

def update_sprites():
    """update_sprites - call update() for all sprites"""
    guys.update()
    bullets.update()
    enemies.update() 

def view_tick():
    """view_tick - visually update the screen"""

    #draw the background
    screen.blit(background, [0,0])
    
    #draw the player's guy and bullets
    if g.visible:
        screen.blit(g.image, g.rect)
    bullets.draw(screen)

    #draw enemies
    enemies.draw(screen)
  
    #update the scoreboard
    scoretxt = font.render("score: " + str(game.score), 1, (100, 100, 100))
    scorepos = pygame.Rect(35,15,scoretxt.get_rect().height,scoretxt.get_rect().width)
    leveltxt = font.render("level: " + str(game.level), 1, (100, 100, 100))
    levelpos = pygame.Rect(35,35,leveltxt.get_rect().height,leveltxt.get_rect().width)
    livestxt = font.render("lives: " + str(game.lives), 1, (100, 100, 100))
    livespos = pygame.Rect(35,55,livestxt.get_rect().height,livestxt.get_rect().width)

    screen.blit(scoretxt, scorepos)
    screen.blit(leveltxt, levelpos)
    screen.blit(livestxt, livespos)
    if not game.playing:
        screen.blit(hiscores.screen, hiscores.pos)


    #now show the new drawing
    pygame.display.flip()
 
def check_collisions():
    """check_collisions - check for sprite collisions and update
    as necessary.

    """

    #if the player's guy is not alive, don't let it collide
    #this occurs if he is exploding
    #otherwise, if he collides with enemies, explode them both
    if g.alive():
        e = pygame.sprite.spritecollideany(g, enemies)
        if e != None:
            if e.alive():
                g.explode()
                e.explode()
  
    #check if any enemies got hit by any bullets
    hits_dict = pygame.sprite.groupcollide(bullets, enemies, False, False)
    if len(hits_dict) != 0:
        for b in hits_dict:
            for e in hits_dict[b]:
                if e.alive():
                    e.explode()
                    game.increase_score(e.points)
                    b.explode()

def main():
    """main - function to start the main loop. Program ends
    when main() returns.

    """

    update_hiscore_screen()
    while 1:
        #set the clock to tick 15 times per second
        clock.tick(15)

        #check for user input, quit if necessary
        if controller_tick() == 0:
            return

        #let the game run for a frame
        if not game.paused:
            update_sprites()
            view_tick()
            check_collisions()

