import pygame
import os
import time
from algosy.compiler import comp

pygame.init()
# -- Constants -- #
WIDTH, HEIGHT = 1280, 720  # Resolution
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Window
# WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("anonymous_2008")  # Project Name
FPS = 60  # Max FPS
font = pygame.font.Font(os.path.join('Fonts', 'Hack-Regular.ttf'), 15)  # Font for password input
small_font = pygame.font.Font(os.path.join('Fonts', 'Hack-Regular.ttf'), 8)  # Font for attempts left counter
BG = pygame.image.load(os.path.join('Textures', 'bg_game.png'))  # Gameplay background (Kali Linux Desktop)
BG = pygame.transform.smoothscale(BG, (WIDTH, HEIGHT))
KEY_SFX = pygame.mixer.Sound(os.path.join('SFX', 'keys_pressed.mp3'))  # Sound of pressed keys
BAZA = pygame.mixer.Sound(os.path.join('SFX', 'baza.mp3'))  # Based
MUSIC = pygame.mixer.Sound(os.path.join('SFX', 'music_for_hacking.mp3'))  # Intense Cool Music to hack/study to
BAD_END = pygame.mixer.Sound(os.path.join('SFX', 'bad_end.mp3'))  # Bad ending (used all attempts)
SOCIAL_CREDIT = pygame.mixer.Sound(os.path.join('SFX', 'chingchong.mp3'))  # Good Ending
REMEN = pygame.mixer.Sound(os.path.join('SFX', 'remen.mp3'))  # Very Bad ending
# Dictionary used in opening animation as sleep time0
SLEEP_FOR_OP = {1: 0.11, 2: 0.11, 3: 0.11, 4: 0.11, 5: 0.2, 6: 0.4, 7: 0.12, 8: 0.09, 9: 0.09, 10: 0.18, 11: 0.11,
                12: 0.11, 13: 0.11, 14: 0.25, 15: 0.11, 16: 0.3, 17: 0.09, 18: 0.09, 19: 0.12, 20: 0.08, 21: 0.08,
                22: 0.1, 23: 0.11, 24: 0.7, 25: 0.11, 26: 0.11, 27: 0.11, 28: 0.11, 29: 0.11, 30: 0.1, 31: 0.1, 32: 0.1,
                33: 0.1, 34: 0.1, 35: 0.1, 36: 0.1, 37: 0.1, 38: 0.1, 39: 0.1, 40: 0.1, 41: 0.1, 42: 0.1, 43: 0.1,
                44: 0.1, 45: 0.1, 46: 0.1, 47: 0.1, 48: 0.1, 49: 0.1, 50: 0.05, 51: 0.05, 52: 0.05, 53: 0.05, 54: 0.05,
                55: 0.05, 56: 0.05, 57: 0.05, 58: 0.05, 59: 0.05, 60: 0.05, 61: 0.05, 62: 0.05, 63: 0.05, 64: 0.05,
                65: 0.05, 66: 0.05, 67: 0.05, 68: 0.05, 69: 0.11}


# Basically waiting user inputting return key
def draw_destiny():
    WIN.blit(BG, (0, 0))
    pygame.display.update()


# Generating random password with difficulty set
def get_password(seed, dif):
    # DataBase with all the passwords sorted by difficulty
    if dif == 1:
        password_pick = {0: 'abc', 1: '111', 2: 'qw'}
    elif dif == 2:
        password_pick = {0: 'password', 1: '1984', 2: 'qwerty'}
    elif dif == 3:
        password_pick = {0: 'yjemyp3y3xz8syev', 1: '6ck5s4xqf3nks6qa', 2: '95shzpmjfk2vdtg8', 3: 'mfyujrvqdtj3w8sh'}
    else:
        password_pick = {0: 'password'}
    return password_pick[seed % len(password_pick)]


# Generates random teacher's login
def get_login(seed):
    names = {0: 'tatyana', 1: 'elena', 2: 'angela', 3: 'alena', 4: 'irina', 5: 'svetlana', 6: 'maria', 7: 'ksenia',
             8: 'zinaida', 9: 'antonina'}
    year = 1950 + seed % 15
    mail = {0: '@mail.ru', 1: '@gmail.com', 2: '@yahoo.com', 3: '@yandex.ru'}
    return names[seed % len(names)] + str(year) + mail[seed % len(mail)]


# Checking if password is correct
def fact_check(text, password):
    return password == text


# Player failed in hacking
def draw_lose():
    lose_image = pygame.image.load(os.path.join('Textures', 'remen.png'))
    lose_image = pygame.transform.smoothscale(lose_image, (WIDTH, HEIGHT))
    WIN.blit(lose_image, (0,0))
    pygame.display.update()


# Player succeed in hacking
def draw_hacked(i):
    time.sleep(1)
    op_address = 'game_over' + str(i) + '.jpg'
    op_image = pygame.image.load(os.path.join('Textures', op_address))
    op_image = pygame.transform.smoothscale(op_image, (WIDTH, HEIGHT))
    WIN.blit(op_image, (0, 0))
    pygame.display.update()


# Good Ending
def good_ending():
    win_image = pygame.image.load(os.path.join('Textures', 'goodending.jpg'))
    win_image = pygame.transform.smoothscale(win_image, (WIDTH, HEIGHT))
    WIN.blit(win_image, (0, 0))
    pygame.display.update()


# Actual gameplay starts from here
def draw_gameplay(text, login, code, life):
    WIN.blit(BG, (0, 0))
    # Render the current input and login.
    login_surface = font.render(login, True, (0, 0, 0))
    txt_surface = font.render(text, True, (0, 0, 0))
    if life < 3:
        attempts_left = "That didn't work. Try again! Attempts left: " + str(life)
        life_surface = small_font.render(attempts_left, True, (255, 0, 0))
        WIN.blit(life_surface, (775, 333))
    out_code = list(code.split('\n'))  # Splitting code into several lines
    # Blit the input and login.
    WIN.blit(login_surface, (780, 246))
    WIN.blit(txt_surface, (780, 307))
    for i in range(len(out_code)):
        # Drawing lines of code one by one
        code_surface = font.render(out_code[i], True, (0, 0, 0))
        if i != 0 and i != len(out_code) - 1:
            WIN.blit(code_surface, (530, 520 + i*23))  # SQL Injection Decorations
        else:
            WIN.blit(code_surface, (510, 520 + i*23))  # Actual code
    pygame.display.update()


# Logo Appears at the start with changing alpha(?).
def draw_logo(alpha):
    logo = pygame.image.load(os.path.join('Textures', 'logo_new.png')).convert()
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


# Picking the Difficulty:
def draw_picker(i):
    menu_address = 'diff_pick_' + str(i) + '.png'
    menu_image = pygame.image.load(os.path.join('Textures', menu_address))
    menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
    WIN.blit(menu_image, (0, 0))
    pygame.display.update()


# Picking the Gamemod:
def draw_gamemod_picker(i):
    menu_address = 'gamemode_pick_' + str(i) + '.png'
    menu_image = pygame.image.load(os.path.join('Textures', menu_address))
    menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
    WIN.blit(menu_image, (0, 0))
    pygame.display.update()


# Animation for game start
def draw_opening(i):
    op_address = 'op' + str(i) + '.png'
    op_image = pygame.image.load(os.path.join('Textures', op_address))
    op_image = pygame.transform.smoothscale(op_image, (WIDTH, HEIGHT))
    WIN.blit(op_image, (0, 0))
    if i == 7:
        pygame.mixer.Sound.play(KEY_SFX)
        pygame.mixer.music.stop()
    pygame.display.update()


# Program Entry point
def main():
    # If nothing will go wrong this will be changed
    password = login = code = ''
    start = 0  # Used later to check time player not hacking
    seed = int(time.time())  # Seed For random numbers
    life = 3  # Attempts user have to hack
    clock = pygame.time.Clock()  # Used for limiting FPS
    run = True  # Game is running while this is set to True
    mode = 0  # Mode we are in, where: {
    # 0 - Drawing logo
    # 1 - Drawing Main Menu
    # 2 - Opening Animation
    # 3 - Gameplay
    # 4 - Web Hacked
    # 5 - Failed in Hacking
    # 6 - Choose your Destiny
    # 7 - Good Ending
    # 8 - Picking Difficulty (in main menu)
    # 9 - Picking game mode - settings (in main menu)
    # } (Order is a bit weird but it historically based)
    i = 1  # Opening Screenshot s Number
    j = 1  # Main Menu Selected Option
    dif = 1  # Difficulty. Will be picked by user later
    game_mode = 1  # Game modes: 1 - student, 2 - teacher
    text = ''  # User input
    alpha = 180  # Alpha for logo(?)
    baza_played = False  # Nobody heard this incredible phrase yet.
    hack_end_played = False  # Still no bad end
    while run:
        clock.tick(FPS)  # FPS Limitation
        for event in pygame.event.get():  # Checking for keys pressed / game closed
            if event.type == pygame.QUIT:  # Game is closed
                run = False
            if event.type == pygame.KEYDOWN:  # Key is pressed in:
                # -- Main Menu -- #
                if mode == 1:
                    if event.key == pygame.K_UP:  # Upper Option
                        j -= 1
                    elif event.key == pygame.K_DOWN:  # Lower Option
                        j += 1
                    elif event.key == pygame.K_RETURN:
                        if j % 3 == 1:  # Go to difficulty pick
                            mode = 8
                        if j % 3 == 2:  # Settings
                            mode = 9
                        if j % 3 == 0:  # Quit
                            run = False
                # -- Opening -- #
                elif mode == 2:
                    if event.key == pygame.K_RETURN:
                        mode = 3
                        pygame.mixer.Sound.stop(KEY_SFX)
                        pygame.mixer.Sound.play(MUSIC).set_volume(0.5)  # Turning on the Music
                # -- Diff pick -- #
                elif mode == 8:
                    if event.key == pygame.K_UP:  # Upper Option
                        dif -= 1
                    elif event.key == pygame.K_DOWN:  # Lower Option
                        dif += 1
                    elif event.key == pygame.K_RETURN:
                        if game_mode == 1:  # Student
                            if dif % 4 in (1, 2, 3):  # Go to gameplay
                                dif = dif % 4 or 4
                                mode = 2
                                password = get_password(seed, dif)  # Generate password with this diff
                                code_unchanged = comp(password)  # Get password coded
                                code = code_unchanged
                                print(password)  # For Debugging and Cheating
                                print(code)
                                dividers_num = len(code) // 80  # See how much line transfers we need
                                # Divide code into multiple lines
                                for temp in range(dividers_num):
                                    code = code[:80 * (temp + 1) + temp] + '\n' + code[80 * (temp + 1) + temp:]
                                code = 'SQL.response.password.coded {\n' + code + '\n}'  # Add decorations
                                login = get_login(seed)  # Get random login
                            else:
                                mode = 1
                        if game_mode == 2:  # Teacher
                            pass
                elif mode == 9:
                    if event.key == pygame.K_UP:  # Upper Option
                        game_mode -= 1
                    elif event.key == pygame.K_DOWN:  # Lower Option
                        game_mode += 1
                    elif event.key == pygame.K_RETURN:
                        if dif % 3 in (1, 2):  # Choose the game mode
                            mode = 1
                        else:
                            mode = 1
                # -- Gameplay -- #
                elif mode == 3:
                    if event.key == pygame.K_RETURN:  # Checking password when Enter is pressed
                        if fact_check(text, password):
                            mode = 4  # Go to success screen
                        else:
                            if text != '':
                                life -= 1  # -1 Attempt
                        if not life:
                            mode = 5  # If no more lives go to fail screen
                            pygame.mixer.Sound.stop(MUSIC)
                            pygame.mixer.Sound.play(REMEN)
                        text = ''  # Deleting previous input
                    elif event.key == pygame.K_BACKSPACE:  # Deleting last symbol of input when backspace is pressed
                        text = text[:-1]
                    else:
                        text += event.unicode  # Appending pressed symbol
                if mode == 4 or mode == 5:  # In developing :)
                    if event.key == pygame.K_q:
                        run = False
                if mode == 6:
                    if event.key == pygame.K_RETURN:  # If player start hack
                        mode = 3
        ######################
        # -- Drawing Logo -- #
        if mode == 0:
            draw_logo(alpha)
            if not baza_played:
                pygame.mixer.Sound.play(BAZA)  # Play Incredible Phrase
                pygame.mixer.music.stop()
                baza_played = True
            alpha += 1  # Gradually changing transparency of logo (Doesn't work ??)
            if alpha == 250:
                mode = 1  # Go to Main Menu
        # -- Main Menu -- #
        elif mode == 1:
            draw_main_menu(j % 3 or 3)  # Highlight option №j
        # -- Choosing Difficulty -- #
        elif mode == 8:
            draw_picker(dif % 4 or 4)
        elif mode == 8:
            draw_gamemod_picker(game_mode % 3 or 3)
        # -- Opening Animation -- #
        elif mode == 2:
            draw_opening(i)  # Blit screenshot №i
            time.sleep(SLEEP_FOR_OP[i])  # Pause between screenshots
            i += 1
            if i > 69:
                pygame.mixer.Sound.stop(KEY_SFX)
                pygame.mixer.Sound.play(MUSIC).set_volume(0.5)  # Turning on the Music
                mode = 6  # Go to Choose your Destiny
                start = time.time()  # Start the timer
                print(start)
        # -- Gameplay -- #
        elif mode == 3:
            draw_gameplay(text, login, code, life)  # Kali linux bg with user input on 'password' field
        # -- Success Screen -- #
        elif mode == 4:
            i += 1
            if not hack_end_played:
                pygame.mixer.Sound.play(BAD_END)  # Play FBI OPEN UP!!!
                pygame.mixer.music.stop()
                hack_end_played = True
            draw_hacked(i % 3 or 1)
        # -- Failure Screen -- #
        elif mode == 5:
            i += 1
            draw_lose()
        # -- Choosing Destiny -- #
        elif mode == 6:
            draw_destiny()
            if time.time() > time.time() - start > 5:  # If player won't start hack in 5 minutes he wins
                pygame.mixer.Sound.stop(MUSIC)
                pygame.mixer.Sound.play(SOCIAL_CREDIT)
                mode = 7
        # -- Good Ending -- #
        elif mode == 7:
            good_ending()
    pygame.quit()


# -- Launching -- #
if __name__ == '__main__':
    main()
