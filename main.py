import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
#from constants import * (* means all)
from logger import log_state

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #pygame.display.set_mode(size=(100, 100), flags= pygame.OPENGL | pygame.RESIZABLE, depth=8, display=0, vsync=0) -> Surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
