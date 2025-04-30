import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "WHITE", self.position, self.radius, 2)

    def update(self, dt):
        # Update the position of the asteroid based on its velocity and dt
        self.position += self.velocity * dt
    
    def split(self):
        random_angle = random.uniform(20, 50)

        self.kill()  # Remove the asteroid from the game
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        # Create two smaller asteroids with a random angle and velocity
        
        # first new asteroid
        new_velocity1 = self.velocity.rotate(random_angle)
        
        new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid1.velocity = new_velocity1 * 1.2

        # second new asteroid
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid2.velocity = new_velocity2 * 1.2