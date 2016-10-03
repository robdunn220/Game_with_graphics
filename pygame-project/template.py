import pygame
import random

class Hero(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5

    def render(self, screen):
        hero = pygame.image.load('hero.png')
        screen.blit(hero, (self.x, self.y))

class Monster(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5

    def update(self, width, height):
        self.x += self.speed_x
        #self.y += (self.speed_y)/4
        if self.x > width:
            self.x = 0
            rand_num = random.randrange(20, 480)
            self.y = rand_num
        if self.x < 20:
            self.speed_x = 6
        if self.y > height - 50:
            self.speed_y = -2
        if self.y < 20:
            self.speed_y = 6

    def render(self, screen):
        monster = pygame.image.load('monster.png')
        screen.blit(monster, (self.x, self.y))

def main():
    # declare the size of the canvas
    width = 512
    height = 480
    bg = pygame.image.load('background.png')

    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    monster = Monster(0, 180)
    hero = Hero(236, 210)

    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.KEYUP:
                hero.y -= 10
            #elif event.type == pygame.KEYDOWN:
                #hero.y += 10
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################


        # fill background color
        screen.blit(bg, (0, 0))

        hero.render(screen)
        monster.update(width, height)
        monster.render(screen)
        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
