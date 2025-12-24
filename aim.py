import pygame, time
from target import Bottle
from infobar import GameInfo

pygame.init()

HEIGHT = 600
WIDTH = 800
FPS = 60
BG_COLOR = (15, 15, 20)
BG_IMAGE = pygame.image.load("assets/bg.png")
BG_IMAGE = pygame.transform.scale(BG_IMAGE, (WIDTH + 10, HEIGHT + 50))
AIM = pygame.image.load("assets/aim.png")
AIM = pygame.transform.scale(AIM, (35, 35))
START = time.time()
END = 0
SHOOT = pygame.mixer.Sound("assets/shoot.mp3")
BREAK = pygame.mixer.Sound("assets/break.mp3")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")
clock = pygame.time.Clock()

bg_rect = BG_IMAGE.get_rect()
aim_rect = AIM.get_rect()
pygame.mouse.set_visible(False)

bottles_list = []
for _ in range(2):
    bottles_list.append(Bottle(screen))

cursor_pos = pygame.mouse.get_pos()
game_info = GameInfo(screen)
def main():
    run = True
    while run:
        clock.tick(FPS)
        bg_rect.center = (WIDTH // 2, (HEIGHT - 50) // 2)
        screen.blit(BG_IMAGE, bg_rect)

        cursor_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                SHOOT.play(loops=0)
                for b in bottles_list:
                    if not b.is_broken and b.handle_collision(cursor_pos):
                        b.is_broken = True
                        Bottle.COUNT += 1
                        BREAK.play(loops=0)
                        bottles_list.append(Bottle(screen))

        for b in bottles_list[:]:
            b.draw()
            b.update()
            if b.y > (HEIGHT + 25):
                bottles_list.remove(b)
                if len(bottles_list) < 4:
                    bottles_list.append(Bottle(screen))

        aim_rect.center = cursor_pos
        screen.blit(AIM, aim_rect)

        END = time.time()
        game_info.show_infobar(END-START, Bottle.COUNT)

        pygame.display.flip()
    
if __name__ == "__main__":
    main()
    pygame.quit()