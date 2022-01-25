import pygame
import os
from helpers.Constants import Constants
from Map import Maze


class ReggaeShark:

    def __init__(self, screen, maze_map, screen_size, tile_size, maze):
        game_folder = os.path.dirname(__file__)
        sprite_folder = os.path.join(game_folder, 'sprites')
        self.sprite = pygame.image.load(os.path.join(sprite_folder, 'reggae_shark.png')).convert()
        self.rect = self.sprite.get_rect()
        self.rect.center = (400, 400)
        self.sprite.set_colorkey((255, 255, 255))
        self.screen = screen
        self.screen_size = screen_size
        self.pos = [(self.screen_size[0]/2)-.5*tile_size, self.screen_size[1]-2*tile_size]
        self.direction = [0, 0]
        self.new_direction = [0, 0]
        self.speed = 1/4
        self.maze = maze
        self.maze_map = maze_map
        self.size = tile_size - 5

    def update(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed
        if not self.maze.collision_detection_direction(self.pos, self.new_direction, self.size + 5):
            self.direction = self.new_direction
            #self.new_direction = [0, 0]
        if self.maze.collision_detection_direction(self.pos, self.direction, self.size+5):
            self.direction = [0, 0]

    def draw(self):
        pygame.draw.ellipse(self.screen, [100, 100, 100], [[self.pos[0]+2.5, self.pos[1]+2.5], [self.size, self.size]])
        self.screen.blit(self.sprite, (self.pos[0], self.pos[1]))

    def direction_change(self, new_direction):
        #if self.maze.center_detection(): #or self.new_direction == [0, 0]:
            self.new_direction = new_direction
