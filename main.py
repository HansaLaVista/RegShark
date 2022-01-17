import pygame
from helpers.Constants import Constants
from helpers.keyboardHandler import KeyboardHandler


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Game:

    def __init__(self):
        pygame.init()
        self.size = (Constants.Window_width, Constants.Window_height)
        self.screen = pygame.display.set_mode(self.size)
        self.keyboard_handler = KeyboardHandler()
        self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], 64)
        self.time = pygame.time.get_ticks()
        self.game = reggae_shark()

    def game_loop(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time
        self.time = current_time
        self.handle_events()
        self.update_game(delta_time)
        self.draw_components()

    def update_game(self, dt):

    def draw_components(self):

    def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.handle_key_down(event)
                if event.type == pygame.KEYUP:
                    self.handle_key_up(event)
                if event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_motion(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_pressed(event)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_released(event)


    def handle_key_down(self, event):
            self.keyboard_handler.key_pressed(event.key)


    def handle_key_up(self, event):
            self.keyboard_handler.key_released(event.key)


    def handle_mouse_motion(self, event):
            pass


    def handle_mouse_pressed(self, event):
           # self.game_view.on_mouse_clicked(pygame.mouse.get_pos())


    def handle_mouse_released(self, event):
            pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    while True:
        game.game_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
