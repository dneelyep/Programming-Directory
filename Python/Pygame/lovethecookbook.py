#I love the Pygame Cookbook - messed with a bit
import pygame, random
pygame.init() 
screen = pygame.display.set_mode([800,100])
screen.fill([255,255,255])
mainloop, x,y, color, fontsize, delta, fps =  True, 25 , 0, (32,32,32), 35, 1, 30
clock = pygame.time.Clock() # create clock object
while mainloop:
    tick_time = clock.tick(fps) # milliseconds since last frame
    pygame.display.set_caption("press Esc to quit. FPS: %.2f" % (clock.get_fps()))
    fontsize = random.randint(35, 75)
    myFont = pygame.font.SysFont("None", fontsize)
    color = (random.randint(0,30), random.randint(0,255), random.randint(0,255))
    screen.fill((255,255,255))
    screen.blit(myFont.render("I love the pygame cookbook", 0, (color)), (x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
    pygame.display.update()
