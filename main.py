import pygame, sys
from settings import *
#from debug import debug
from level import Level

class Game: 
    def __init__(self):

        #general setup
        pygame.init()                                               #starting pygame
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))       #creating display surface
        pygame.display.set_caption('vp land')
        self.clock = pygame.time.Clock()                            #creating clock

        self.level = Level()                                        #creating instance of Level class

    def run(self):
        while True:
            for event in pygame.event.get():                        #event loop
                if event.type == pygame.QUIT:                       #checking if closing the game
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('black')                               #screen color
            #debug('hi vincent(-:')                                 #displays text on screen
            self.level.run()                                        #running run from level in loop
            pygame.display.update()                                 #updating screen
            self.clock.tick(FPS)                                    #controlling frame rate


if __name__ == '__main__':                                          #if this is main file
    game = Game()                                                   #creating instance of game class
    game.run()                                                      #call method run



