import pygame
#from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import * #(* means all)
from logger import log_state
from player import Player

def main():
    #initialize
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #pygame.display.set_mode(size=(100, 100), flags= pygame.OPENGL | pygame.RESIZABLE, depth=8, display=0, vsync=0) -> Surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Explaining this to myself
    #pygame has a class and/or method called Clock()
    #We're defining a clock object to be one of those things. Which means it's a class, I'm pretty sure
    clock = pygame.time.Clock()
    dt = 0.0


    #game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)

        pygame.display.flip()
        
        #limiting the game refresh rate to 60 fps
        #For myself; the clock object class has a method called tick, which takes in a float as an optional parameter to limit the framerate
        #I read the documentation, but honestly only vaguely understand how it works. It forces a delay before the next refresh
        dt = clock.tick(60.0) / 1000
        #print(f"the delta time it {dt}")
        

if __name__ == "__main__":
    main()
