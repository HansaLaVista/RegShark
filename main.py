import sys
import pygame
#import serial

from ReggaeShark import RastaShark
from Maze import Maze
from baddies import Baddies
from game_view import GameView
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
        pygame.mixer.music.play()
        self.size = (Constants.Window_width, Constants.Window_height)
        self.screen = pygame.display.set_mode(self.size)
        self.maze = Maze()
        self.maze_map = [""]
        self.maze_map = self.maze.generate_matrix()
        self.keyboard_handler = KeyboardHandler()
        self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], 64)
        self.time = pygame.time.get_ticks()
        self.number_of_joints = 4
        self.baddies = []
        for x in range(self.number_of_joints):
            self.baddies.append(Baddies(self.screen, self.maze, Constants.Target_distance[x], Constants.Tile_size,
                                        Constants.J_speed[x]))
        self.shark = RastaShark(self.screen, self.maze_map, self.size, Constants.Tile_size, self.maze)
        self.game_view = GameView(self.shark, self.screen, self.maze_map, Constants.Tile_size, self.maze)
        # self.arduino = serial.Serial('COM3', 9600)


    def game_loop(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time
        self.time = current_time
        self.handle_events()
        self.update_game(delta_time)
        self.draw_components()
        # self.controller_update()


    def update_game(self, dt):
        jonko_pos = []
        for x in range(len(self.baddies)):
            self.baddies[x].update(self.shark.pos, dt)
            jonko_pos.append(self.baddies[x].pos)
        self.shark.update(dt, jonko_pos)


    # def controller_update(self):
    #     arduino_data = self.arduino.read().decode('ascii')
    #     if arduino_data == 'U':
    #         self.shark.direction_change([0, -1])
    #     if arduino_data == 'D':
    #         self.shark.direction_change([0, 1])
    #     if arduino_data == 'L':
    #         self.shark.direction_change([-1, 0])
    #     if arduino_data == 'R':
    #         self.shark.direction_change([1, 0])

    def draw_components(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time
        self.screen.blit(self.background, (0, 0))
        self.game_view.draw_maze()
        self.shark.draw(delta_time)
        for x in range(len(self.baddies)):
            self.baddies[x].draw()
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

    def handle_key_down(self, event):
        #self.keyboard_handler.key_pressed(event.key)
        if event.key == pygame.K_w:
            self.shark.direction_change([0, -1])
        if event.key == pygame.K_s:
            self.shark.direction_change([0, 1])
        if event.key == pygame.K_a:
            self.shark.direction_change([-1, 0])
        if event.key == pygame.K_d:
            self.shark.direction_change([1, 0])

    def handle_key_up(self, event):
        pass# self.keyboard_handler.key_released(event.key)

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

    shark = Game()
    while True:
        shark.game_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
