import pygame, math
pygame.init()

class Target():
    MAX_RADIUS = 50
    MIN_RADIUS = 30
    RADIUS = 40
    IMAGE = pygame.image.load("target.png")
    COUNT = 0
    SPEED = 1
    SHRINK = True
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.size = 0
        self.screen = screen
        self.image = pygame.transform.scale(self.IMAGE, (self.RADIUS, self.RADIUS))
        self.target_rect = self.image.get_rect()
        self.target_rect.center = (self.x, self.y)
    
    def show_target(self):
        self.screen.blit(self.image, self.target_rect)

    def handle_collision(self, mouse_pos):
        distance = math.sqrt((self.x - mouse_pos[0])**2 + (self.y - mouse_pos[1])**2)
        return distance < self.RADIUS / 2
    
    def blink(self):
        if self.SHRINK:
            self.RADIUS -= self.SPEED
            if self.RADIUS <= self.MIN_RADIUS:
                self.SHRINK = False
        else:
            self.RADIUS += self.SPEED
            if self.RADIUS >= self.MAX_RADIUS:
                self.SHRINK = True
        size = int(self.RADIUS)
        self.image = pygame.transform.scale(self.IMAGE, (size, size))
        self.target_rect = self.image.get_rect()
        self.target_rect.center = (self.x, self.y)
