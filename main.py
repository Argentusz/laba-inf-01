import pygame
import os
import time

# Constants
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("anonymous_2008")
WHITE = 255, 255, 255
FPS = 120
SLEEP_FOR_OP = {1: 0.11, 2: 0.11, 3: 0.11, 4: 0.11, 5: 0.2, 6: 0.4, 7: 0.12, 8: 0.09, 9: 0.09, 10: 0.18, 11: 0.11,
                12: 0.11, 13: 0.11, 14: 0.25, 15: 0.11, 16: 0.3, 17: 0.09, 18: 0.09, 19: 0.12, 20: 0.08, 21: 0.08,
                22: 0.1, 23: 0.11, 24: 0.7, 25: 0.11}


def draw_logo(alpha):
    logo = pygame.image.load(os.path.join('Textures', 'logo.png')).convert_alpha()
    logo = pygame.transform.scale(logo, (WIDTH, HEIGHT))
    logo.set_alpha(50)
    WIN.blit(logo, (0, 0))
    pygame.display.update()


def draw_main_menu(i):
    menu_address = 'mainmenu' + str(i) + '.png'
    menu_image = pygame.image.load(os.path.join('Textures', menu_address))
    menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
    WIN.blit(menu_image, (0, 0))
    pygame.display.update()


def draw_opening(i):
    op_address = 'op' + str(i) + '.png'
    op_image = pygame.image.load(os.path.join('Textures', op_address))
    op_image = pygame.transform.scale(op_image, (WIDTH, HEIGHT))
    WIN.blit(op_image, (0, 0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    mode = 0
    i = j = 1
    alpha = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    j -= 1
                elif event.key == pygame.K_DOWN:
                    j += 1
                elif event.key == pygame.K_RETURN:
                    if j % 3 == 1:
                        mode = 2
                elif event.key == pygame.K_q:
                    if mode == 3:
                        run = False
        if mode == 0:
            alpha += 1
            draw_logo(min(alpha, 255))
            if alpha == 50:
                mode = 1
        elif mode == 1:
            draw_main_menu(j % 3 or 3)
        elif mode == 2:
            draw_opening(i)
            time.sleep(SLEEP_FOR_OP[i])
            i += 1
            if i > 25:
                mode = 3
    pygame.quit()


if __name__ == '__main__':
    main()
