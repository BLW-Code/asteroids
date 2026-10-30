import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #assign classes to groups
    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT /2))

    # clock for fps
    fps_clock = pygame.time.Clock()
    dt = 0.0



    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update player state
        updatable.update(dt)

        #render screen
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        #update delta time
        dt = fps_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
