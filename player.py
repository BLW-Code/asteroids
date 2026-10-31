from circleshape import CircleShape
from shot import Shot
from  constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x:int, y:int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.shoot_timer = 0
        self.rotation = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen:pygame.Surface):
        color = "white"
        points = self.triangle()
        pygame.draw.polygon(screen, color, points, LINE_WIDTH)

    def rotate(self, dt:float):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt:float):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        tip = self.triangle()[0]
        shot = Shot(tip.x, tip.y)
        shot.velocity = pygame.Vector2(0, 1)
        rotated_vector = shot.velocity.rotate(self.rotation)
        rotated_vector_with_speed = rotated_vector * PLAYER_SHOT_SPEED
        shot.velocity += rotated_vector_with_speed



    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        #horizontal movement
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        #vertical movement
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)

        #shoot
        self.shoot_timer -= dt
        if keys[pygame.K_SPACE]:
            self.shoot()

    def collides_with(self, other: "CircleShape"):
        for vector in self.triangle():
            other_edge_vector = other.position.move_towards(vector, other.radius)
            if vector.distance_to(other_edge_vector) <= 0:
                return True

        return False
