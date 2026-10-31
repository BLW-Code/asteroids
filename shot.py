import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        color = "red"
        pygame.draw.circle(screen, color, self.position, self.radius)

    def update(self, dt:float) -> None:
        self.position += self.velocity * dt
