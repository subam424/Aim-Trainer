import pygame, time, math
from random import randint
from target import Target

pygame.init()

HEIGHT = 600
WIDTH = 800
FPS = 120
GREY = (112, 128, 144)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
AIM = pygame.image.load("aim.png")
AIM = pygame.transform.scale(AIM, (32, 32))
START = time.time()
END = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")
clock = pygame.time.Clock()

aim_rect = AIM.get_rect()
pygame.mouse.set_visible(False)

target_list = []
for i in range(3):
    target = Target(randint(Target.RADIUS, WIDTH - Target.RADIUS), randint(Target.RADIUS, HEIGHT - Target.RADIUS), screen)
    target_list.append(target)

cursor_pos = pygame.mouse.get_pos()

run = True
while run:
    clock.tick(FPS)
    screen.fill(WHITE)
    cursor_pos = pygame.mouse.get_pos()
    pygame.mouse.set_cursor(pygame.cursors.diamond)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for trg in target_list[:]:
                if math.sqrt((trg.x-cursor_pos[0])**2 + (trg.y-cursor_pos[1])**2) < target.RADIUS/2:
                    target_list.remove(trg)
    for trg in target_list:
        trg.show_target()

    aim_rect.center = cursor_pos
    screen.blit(AIM, aim_rect)

    END = time.time()
    pygame.display.flip()
    

pygame.quit()