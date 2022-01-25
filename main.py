import sys

import pygame
from ReggaeShark import ReggaeShark
from Map import Map
from Map import Maze

#import pygame_gui
from baddies import Baddies
from game_view import GameView
#import serial


from helpers.Constants import Constants
from helpers.keyboardHandler import KeyboardHandler


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("reggae.mp3")
        pygame.mouse.set_visible(False)
        self.background = pygame.image.load("Background.jpg")
        #self.arduino = serial.Serial('COM3', 115200)
        #pygame.mixer.music.play()
        self.size = (Constants.window_width, Constants.window_height)
        self.screen = pygame.display.set_mode(self.size)
        self.maze = Maze()
        # self.maze_map = [""]
        self.maze_map = self.maze.generate_matrix()
        self.keyboard_handler = KeyboardHandler()
        self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], 64)
        self.time = pygame.time.get_ticks()
        self.game = ReggaeShark(self.screen, self.maze_map, self.size, Constants.tile_size, self.maze)
        self.baddies = Baddies(self.screen, self.maze, Constants.tile_size)
        self.game_view = GameView(self.game, self.screen, self.maze_map, Constants.tile_size, self.maze)
        self.Map = Map
        self.game = ReggaeShark(self.screen, self.maze_map, self.size, Constants.tile_size, self.maze)
        self.game_view = GameView(self.game, self.screen, self.font, self.maze_map, Constants.tile_size)
        self.arduino_data = ""
        #self.manager = pygame_gui.UIManager()

    def game_loop(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time
        self.time = current_time
        self.handle_events()
        self.update_game(delta_time)
        self.draw_components()
        self.arduino_data = self.arduino.readline().decode('ascii').strip()

    def update_game(self, dt):
        self.game.update(dt)
        self.baddies.update(self.game.pos)
        pass

    def draw_components(self):
        self.screen.blit(self.background, (0, 0))
        self.game_view.draw_game()
        self.game.draw()
        self.baddies.draw()
        pygame.display.flip()

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
        # Moving up
        if self.arduino_data == "U":
            self.game.direction_change([0, -1])
        # Moving down
        if self.arduino_data == "D":
            self.game.direction_change([0, 1])
        # Moving left
        if self.arduino_data == "L":
            self.game.direction_change([-1, 0])
        # Moving right
        if self.arduino_data == "R":
            self.game.direction_change([1, 0])

    def handle_key_down(self, event):
        self.keyboard_handler.key_pressed(event.key)



    def handle_key_up(self, event):
        self.keyboard_handler.key_released(event.key)

    def handle_mouse_motion(self, event):
        pass

    def handle_mouse_pressed(self, event):
        # self.game_view.on_mouse_clicked(pygame.mouse.get_pos())
        # self.game_view.on_mouse_clicked(pygame.mouse.get_pos())
        pass

    def handle_mouse_released(self, event):
        pass


# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    game = Game()
    while True:
        game.game_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
