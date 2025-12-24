import pygame
pygame.init()

class GameInfo():
    FONT = pygame.font.SysFont("Impact", 24)
    BOARD = pygame.image.load("assets/board.png")
    BOARD = pygame.transform.scale(BOARD, (120, 60))
    TEXT_COLOR = (245, 235, 200)
    HITS_COLOR = (255, 215, 0)
    WIDTH = 800

    def __init__(self,screen):
        self.screen = screen
        self.board1 = self.BOARD.get_rect()
        self.board2 = self.BOARD.get_rect()
        self.board3 = self.BOARD.get_rect()

    def show_infobar(self, time, hits):
        self.time = time
        self.hits = hits
        speed_val = self.hits / self.time if self.time > 0 else 0

        time_text = self.FONT.render(f"Time: {self.time:.1f}", True, (self.TEXT_COLOR))
        speed_text = self.FONT.render(f"Speed: {speed_val:.1f}", True, self.TEXT_COLOR)
        hits_text = self.FONT.render(f"Score:  {self.hits}", True, self.HITS_COLOR)

        self.board1.center = (55, 25)
        self.board2.center = (self.WIDTH // 2, 25)
        self.board3.center = (self.WIDTH - 55, 25)

        self.screen.blit(self.BOARD, self.board1)
        self.screen.blit(self.BOARD, self.board2)
        self.screen.blit(self.BOARD, self.board3)

        self.screen.blit(time_text, (10, 10)) 
        self.screen.blit(speed_text, (self.WIDTH // 2 - speed_text.get_width() // 2, 10))
        self.screen.blit(hits_text, (self.WIDTH - hits_text.get_width() - 10, 10))