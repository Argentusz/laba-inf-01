import pygame
import os
import time
from algosy.compiler import comp

pygame.init()
# -- Constants -- #
WIDTH, HEIGHT = 1280, 720  # Resolution
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Window
pygame.display.set_caption("anonymous_2008")  # Project Name
FPS = 60  # Max FPS
font = pygame.font.Font(None, 25)  # Font for password input
BG = pygame.image.load(os.path.join('Textures', 'bg_game.png'))  # Gameplay background (Kali Linux Desktop)
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
KEY_SFX = pygame.mixer.Sound(os.path.join('SFX', 'keys_pressed.mp3'))  # Sound of pressed keys
MUSIC = pygame.mixer.Sound(os.path.join('SFX', 'music_for_hacking.mp3'))
# Dictionary used in opening animation as sleep time
SLEEP_FOR_OP = {1: 0.11, 2: 0.11, 3: 0.11, 4: 0.11, 5: 0.2, 6: 0.4, 7: 0.12, 8: 0.09, 9: 0.09, 10: 0.18, 11: 0.11,
                12: 0.11, 13: 0.11, 14: 0.25, 15: 0.11, 16: 0.3, 17: 0.09, 18: 0.09, 19: 0.12, 20: 0.08, 21: 0.08,
                22: 0.1, 23: 0.11, 24: 0.7, 25: 0.11, 26: 0.11, 27: 0.11, 28: 0.11, 29: 0.11, 30: 0.1, 31: 0.1, 32: 0.1,
                33: 0.1, 34: 0.1, 35: 0.1, 36: 0.1, 37: 0.1, 38: 0.1, 39: 0.1, 40: 0.1, 41: 0.1, 42: 0.1, 43: 0.1,
                44: 0.1, 45: 0.1, 46: 0.1, 47: 0.1, 48: 0.1, 49: 0.1, 50: 0.05, 51: 0.05, 52: 0.05, 53: 0.05, 54: 0.05,
                55: 0.05, 56: 0.05, 57: 0.05, 58: 0.05, 59: 0.05, 60: 0.05, 61: 0.05, 62: 0.05, 63: 0.05, 64: 0.05,
                65: 0.05, 66: 0.05, 67: 0.05, 68: 0.05, 69: 0.11}


# Generating random password with difficulty
def get_password(seed, dif):
    if dif == 0:
        password_pick = {0: 'abc', 1: '111', 2: 'qw'}
    elif dif == 1:
        password_pick = {0: 'password', 1: '1984', 2: 'qwerty'}
    elif dif == 2:
        password_pick = {0: 'yjemyp3y3xz8syev', 1: '6ck5s4xqf3nks6qa', 2: '95shzpmjfk2vdtg8', 3: 'mfyujrvqdtj3w8sh'}
    else:
        password_pick = {0: 'password'}
    return password_pick[seed % len(password_pick)]


# Checking if password is correct
def fact_check(text, password):
    return password == text


# Player failed in hacking
def draw_lose():
    WIN.fill((255, 0, 0))
    pygame.display.update()


# Player succeed in hacking
def draw_hacked():
    WIN.fill((0, 255, 0))
    pygame.display.update()


# Actual gameplay starts from here
def draw_gameplay(text):
    WIN.blit(BG, (0, 0))
    # Render the current text.
    txt_surface = font.render(text, True, (0, 0, 0))
    # Blit the text.
    WIN.blit(txt_surface, (780, 308))
    pygame.display.update()


# Logo Appears at the start with changing alpha(?).
def draw_logo(alpha):
    logo = pygame.image.load(os.path.join('Textures', 'logo.png')).convert_alpha()
    logo = pygame.transform.scale(logo, (WIDTH, HEIGHT))
    logo.set_alpha(alpha)
    WIN.blit(logo, (0, 0))
    pygame.display.update()


# Main Menu appearing after logo
def draw_main_menu(i):
    menu_address = 'mainmenu' + str(i) + '.png'
    menu_image = pygame.image.load(os.path.join('Textures', menu_address))
    menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
    WIN.blit(menu_image, (0, 0))
    pygame.display.update()


# Animation for game start
def draw_opening(i):
    op_address = 'op' + str(i) + '.png'
    op_image = pygame.image.load(os.path.join('Textures', op_address))
    op_image = pygame.transform.scale(op_image, (WIDTH, HEIGHT))
    WIN.blit(op_image, (0, 0))
    if i == 7 or i == 16 or i == 28:  # Keys pressed sound
        pygame.mixer.Sound.play(KEY_SFX)
        pygame.mixer.music.stop()
    pygame.display.update()


# Program Entry point
def main():
    password = ''  # If nothing will go wrong this will be changed
    seed = int(time.time())  # Seed For random numbers
    print(seed)
    life = 3  # Attempts user have to hack
    clock = pygame.time.Clock()  # Used for limiting FPS
    run = True  # Game is running while this is set to True
    mode = 0
    # Mode we are in:
    # 0 - Drawing logo
    # 1 - Drawing Main Menu
    # 2 - Opening Animation
    # 3 - Gameplay
    # 4 - Web Hacked
    # 5 - Failed in Hacking
    i = 1  # Opening Screenshot s Number
    j = 1  # Main Menu Selected Option
    text = ''  # User input
    alpha = 0  # Alpha for logo(?)
    while run:
        clock.tick(FPS)  # FPS Limitation
        for event in pygame.event.get():  # Checking for keys pressed / game closed
            if event.type == pygame.QUIT:  # Game is closed
                run = False
            if event.type == pygame.KEYDOWN:  # Key is pressed
                # -- Main Menu -- #
                if mode == 1:
                    if event.key == pygame.K_UP:  # Upper Option
                        j -= 1
                    elif event.key == pygame.K_DOWN:  # Lower Option
                        j += 1
                    elif event.key == pygame.K_RETURN:
                        if j % 3 == 1:  # Start the game
                            mode = 2
                            dif = 1  # The difficulty should be picked by user. 2b fixed
                            password = get_password(seed, dif)  # Generate password with this diff
                            code = comp(password)  # Get password coded
                        if j % 3 == 0:  # Quit
                            run = False
                # -- Gameplay -- #
                if mode == 3:
                    if event.key == pygame.K_RETURN:  # Checking password when Enter is pressed
                        if fact_check(text, password):
                            mode = 4  # Go to success screen
                        else:
                            life -= 1  # -1 Attempt
                        if not life:
                            mode = 5  # If no more lives go to fail screen
                        text = ''  # Deleting previous input
                    elif event.key == pygame.K_BACKSPACE:  # Deleting last symbol of input when backspace is pressed
                        text = text[:-1]
                    else:
                        text += event.unicode  # Appending pressed symbol
                if mode == 4 or mode == 5:  # In developing :)
                    if event.key == pygame.K_q:
                        run = False
        # -- Drawing Logo -- #
        if mode == 0:
            alpha += 1  # Gradually changing transparency of logo (Doesn't work ??)
            draw_logo(alpha)
            if alpha == 50:
                mode = 1  # Go to Main Menu
        # -- Main Menu -- #
        elif mode == 1:
            draw_main_menu(j % 3 or 3)  # Highlight option №j
        # -- Opening Animation -- #
        elif mode == 2:
            draw_opening(i)  # Blit screenshot №i
            time.sleep(SLEEP_FOR_OP[i])  # Pause between screenshots
            i += 1
            if i > 69:
                pygame.mixer.Sound.play(MUSIC)  # Turning on the Music
                mode = 3  # Go to Gameplay
        # -- Gameplay -- #
        if mode == 3:
            draw_gameplay(text)  # Kali linux bg with user input on 'password' field
        # -- Success Screen -- #
        if mode == 4:
            draw_hacked()
        # -- Failure Screen -- #
        if mode == 5:
            draw_lose()
    pygame.quit()


# -- Launching -- #
if __name__ == '__main__':
    main()
