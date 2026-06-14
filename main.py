import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
#from constants import * (* means all)

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #pygame.display.set_mode(size=(100, 100), flags= pygame.OPENGL | pygame.RESIZABLE, depth=8, display=0, vsync=0) -> Surface
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
