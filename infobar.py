import pygame
pygame.init()

class GameInfo():
    FONT = pygame.font.SysFont("calibri", 24)
    BLACK = (0, 0, 0)
    GREY = (112, 128, 144)
    WIDTH = 800
    def __init__(self,screen):
        self.screen = screen

    def show_infobar(self, time, hits):
        self.time = time
        self.hits = hits
        speed_val = self.hits / self.time if self.time > 0 else 0

        time_text = self.FONT.render(f"Time: {self.time:.2f}", True, self.BLACK)
        speed_text = self.FONT.render(f"Speed: {speed_val:.2f}", True, self.BLACK)
        hits_text = self.FONT.render(f"Hits: {self.hits}", True, self.BLACK)

        self.screen.blit(time_text, (10, 10)) 
        self.screen.blit(speed_text, (self.WIDTH // 2 - speed_text.get_width() // 2, 10))
        self.screen.blit(hits_text, (self.WIDTH - hits_text.get_width() - 10, 10))