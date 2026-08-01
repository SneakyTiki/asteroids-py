import pygame
import sys #some python library
from constants import * #(* means all)
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #initialize
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #pygame.display.set_mode(size=(100, 100), flags= pygame.OPENGL | pygame.RESIZABLE, depth=8, display=0, vsync=0) -> Surface
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroid_field = AsteroidField()
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
        
        #used to be player.update(dt), switched to group
        updatable.update(dt)

        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit")
                print(f"Game over!")
                sys.exit()

            for shot in shots:
                if shot.collides_with(object):
                    log_event("asteroid_shot")
                    object.kill()
                    shot.kill()

        #used to be player.draw(screen), switched to group
        for object in drawable:
            object.draw(screen)

        #refresh screen
        pygame.display.flip()
        
        #limiting the game refresh rate to 60 fps
        #For myself; the clock object class has a method called tick, which takes in a float as an optional parameter to limit the framerate
        #I read the documentation, but honestly only vaguely understand how it works. It forces a delay before the next refresh
        dt = clock.tick(60.0) / 1000
        #print(f"the delta time is {dt}")
        

if __name__ == "__main__":
    main()
