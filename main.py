import pygame
import sys
import time
import asyncio
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #assign classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT /2))
    asteroid_field = AsteroidField()

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

        for asteroid in asteroids:
            if player1.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over")
                sys.exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()


        #render screen
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        #update delta time
        dt = fps_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
