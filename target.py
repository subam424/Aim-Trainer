import pygame
from math import sin, cos, sqrt, radians
from random import randint
pygame.init()

class Bottle:
    RADIUS = 70
    WIDTH = 800
    HEIGHT = 600
    BOTTLE = pygame.image.load("assets/bottle.png")
    BROKEN = pygame.image.load("assets/broken_bottle.png")
    COUNT = 0
    def __init__(self, screen):
        self.screen = screen
        self.x = randint(0, self.WIDTH)
        self.y = self.HEIGHT + 20

        self.rotation_angle = 0
        self.rotation_speed = randint(-5, 5)

        self.bottle = pygame.transform.scale(self.BOTTLE, (self.RADIUS, self.RADIUS))
        self.broken = pygame.transform.scale(self.BROKEN, (self.RADIUS, self.RADIUS))
        self.image = self.bottle
        self.rect = self.image.get_rect(center=(self.x, self.y))

        launch_angle = randint(45, 90) if self.x < self.WIDTH // 2 else randint(90, 135) 
        self.angle = radians(launch_angle)

        self.gravity = 0.1
        self.speed = 10
        self.x_speed = self.speed*cos(self.angle)
        self.y_speed = -self.speed*sin(self.angle)
        self.is_broken = False
    
    def update(self):
        self.y_speed += self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rotation_angle += self.rotation_speed

        base_img = self.broken if self.is_broken else self.bottle
        self.image = pygame.transform.rotate(base_img, self.rotation_angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def handle_collision(self, mouse_pos):
        if not self.is_broken:
            distance = sqrt((self.x - mouse_pos[0])**2 + (self.y - mouse_pos[1])**2)
            return distance < self.RADIUS / 2
        return False