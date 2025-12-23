import pygame
pygame.init()

class GameInfo():
    FONT = pygame.font.SysFont("Impact", 24)
    BAR_COLOR = (186, 140, 99) 
    TEXT_COLOR = (245, 235, 200)
    HITS_COLOR = (255, 215, 0)
    BORDER_COLOR = (100, 70, 50)
    WIDTH = 800
    def __init__(self,screen):
        self.screen = screen

    def show_infobar(self, time, hits):
        pygame.draw.rect(self.screen, self.BAR_COLOR, (0, 0, 800, 50))
        
        pygame.draw.line(self.screen, self.BORDER_COLOR, (0, 50), (800, 50), 2)

        self.time = time
        self.hits = hits
        speed_val = self.hits / self.time if self.time > 0 else 0

        time_text = self.FONT.render(f"Time: {self.time:.2f}", True, self.TEXT_COLOR)
        speed_text = self.FONT.render(f"Speed: {speed_val:.2f}", True, self.TEXT_COLOR)
        hits_text = self.FONT.render(f"Hits: {self.hits}", True, self.HITS_COLOR)

        self.screen.blit(time_text, (10, 10)) 
        self.screen.blit(speed_text, (self.WIDTH // 2 - speed_text.get_width() // 2, 10))
        self.screen.blit(hits_text, (self.WIDTH - hits_text.get_width() - 10, 10))