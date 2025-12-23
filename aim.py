import pygame, time
from random import randint
from target import Target
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

target_list = []
for i in range(5):
    target = Target(randint(Target.RADIUS, WIDTH - Target.RADIUS), 20 + randint(Target.RADIUS, HEIGHT - Target.RADIUS), screen)
    target_list.append(target)

cursor_pos = pygame.mouse.get_pos()
game_info = GameInfo(screen)

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
            for trg in target_list[:]:
                if trg.handle_collision(cursor_pos):
                    target_list.remove(trg)
                    BREAK.play(loops=0)
                    Target.COUNT += 1

    if len(target_list) != 5:      
        target_list.append(Target(randint(Target.RADIUS, WIDTH - Target.RADIUS), 20 + randint(Target.RADIUS, HEIGHT - Target.RADIUS), screen))

    for trg in target_list:
        trg.show_target()
        trg.blink()

    aim_rect.center = cursor_pos
    screen.blit(AIM, aim_rect)

    END = time.time()
    game_info.show_infobar(END-START, Target.COUNT)

    pygame.display.flip()
    

pygame.quit()