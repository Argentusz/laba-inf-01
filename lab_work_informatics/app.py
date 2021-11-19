import pygame
from constants import WINDOW_W, WINDOW_H, SCREEN_W, SCREEN_H, BLOCK_SIZE, VOLUME
from json import loads, dump

from menus import MainMenu, SideMenu
class App():

    def __init__(self):
        self.running = True
        self.window = None
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.w_size = (WINDOW_W, WINDOW_H)
        self.s_size = (SCREEN_W, SCREEN_H) 
        self.collide_ent = []
        self.gravity_ent = []
        self.decor_ent_fore = []
        self.decor_ent_back = []
        self.spikes = []
        self.dialog_windows = []
        
        self.texts = []
        text = open("lab_work_informatics\\texts.json", "r", encoding = "utf-8")
        self.texts = loads(text.read())
        text.close()
        
        self.upgrades = []
        
        self.fullScreen = True
        self.difficulty = 1
        
        self.mainFont = "gui/font.ttf"
        
        text = open("lab_work_informatics\\language.json", "r")
        language = loads(text.read())
        text.close()
        self.language = language["Language"]
        
        self.creditsImage = (pygame.image.load("lab_work_informatics\gui\mainmenu.png"))
        self.creditsOn = False
        
        self.story = False
        self.level = 1
        
        #####
        self.nextWave = False

        self.pause = False
        self.stop = False  
        
        self.enemies = []
        #####
        
        self.dt = 0

    def on_loop(self):
        #игровые вычисления в цикле    
        pass
                        
    def on_render(self):
        #отрисовка объектов
        #self.draw_background()
        self.screen.fill((0, 20, 100))
            
            
                    
        subscreen = self.screen.subsurface(self.look.update())
            
        for caption in self.dialog_windows:
            caption.render(subscreen)
            
        self.player.render_hp(subscreen)
            
        if self.stop:
            textw = self.textend.get_width()
            texth = self.textend.get_height()
            subscreen.blit(self.textend, (WINDOW_W//2 - textw//2, WINDOW_H//2 - texth//2))
                
        if self.mainMenu.working:
            self.mainMenu.render(subscreen)
        if self.menu.working:
            self.menu.render(subscreen)
            
        self.credits(self.screen)
                
        self.window.blit(subscreen, (0, 0))
            
        pygame.display.flip()
            
    def on_cleanup(self):
        #завершение работы программы
        pygame.quit()
            
    def draw_background(self):
        #отрисовка фона
        self.window.blit(self.screen, (0, 0))
            
        
    def on_execute(self):
        #цикл работы приложения
        if self.on_init() == False:
            self.running = False
                
        while (self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.dt = self.clock.tick(self.fps)
        self.on_cleanup()

    def set_full_screen(self):
        #полноэкранный режим
        self.window = pygame.display.set_mode(self.w_size, pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
            
    def set_window_screen(self):
        #оконный режим
        self.window = pygame.display.set_mode(self.w_size)
            
    def on_init(self):
        #инициализация игры
        pygame.init()
        #self.init_gamepad()
        self.set_full_screen()
        pygame.display.set_caption('ANONIMUS2008') #строчка на панели управления
        #pygame.display.set_icon(pygame.image.load("image.png")) #иконка
        self.running = True    
        
        #главное меню
        self.mainMenu = MainMenu(0, 0, "lab_work_informatics\gui\mainmenu.png", self)
        self.mainMenu.activate()    
            
        #меню
        self.menu = SideMenu(0, 0, "lab_work_informatics\gui\mainmenu.png", self)
            
        self.pause = True
        self.game_channel.pause()
        self.menu_music.play(-1)