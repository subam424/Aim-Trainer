import pygame

class Target():
    RADIUS = 40
    IMAGE = pygame.image.load("target.png")
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.size = 0
        self.screen = screen
        self.image = pygame.transform.scale(self.IMAGE, (self.RADIUS, self.RADIUS))
    
    def show_target(self):
        self.target_rect = self.image.get_rect()
        self.target_rect.center = (self.x, self.y)
        self.screen.blit(self.image, self.target_rect)