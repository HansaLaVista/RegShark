import pygame
import os
from helpers.Constants import Constants
from Maze import Maze


class ReggaeShark:

    def __init__(self, screen, maze_map, screen_size, tile_size, maze):
        game_folder = os.path.dirname(__file__)
        sprite_folder = os.path.join(game_folder, 'sprites')
        self.sprites = []
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_1.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_2.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_3.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_4.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_5.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_6.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_7.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_8.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_9.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_10.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_11.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_12.png')))

        self.jonko_sprites = []
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_1.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_2.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_3.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_4.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_5.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_6.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_7.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_8.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_9.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_10.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_11.png')))
        self.sprites.append(pygame.image.load(os.path.join(sprite_folder, 'rs_wj_12.png')))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)
        self.image.set_colorkey((0, 0, 0))
        self.screen = screen
        self.screen_size = screen_size
        self.pos = [(self.screen_size[0]/2)-tile_size, self.screen_size[1]-2*tile_size]
        self.direction = [0, 0]
        self.new_direction = [0, 0]
        self.speed = 1/15
        self.maze = maze
        self.maze_map = maze_map
        self.size = tile_size - 5
        self.tile_size = tile_size



    def update(self, j_pos, dt):

        self.pos[0] += self.direction[0] * self.speed * dt
        self.pos[1] += self.direction[1] * self.speed * dt
        self.center = (self.pos[0]+self.tile_size/2, self.pos[1]+self.tile_size/2)
        if self.new_direction != [0, 0] and not \
                self.maze.collision_detection_direction(self.pos, self.direction, self.new_direction, self.size + 5): #and self.new_direction == self.direction:
            if (self.direction[0] != -self.new_direction[0] or self.direction[1] != -self.new_direction[1]) \
                    and self.new_direction != self.direction:
                self.tile = self.maze.get_tile(self.center, self.tile_size)
                #print(self.tile)
                self.pos[0] = self.tile[0]*self.tile_size
                self.pos[1] = self.tile[1]*self.tile_size
            self.direction = self.new_direction
            self.new_direction = [0, 0]
        if self.maze.collision_detection_straight(self.pos, self.direction, self.size+5):
            self.direction = [0, 0]
            self.tile = self.maze.get_tile(self.center, self.tile_size)
            self.pos[0] = self.tile[0] * self.tile_size
            self.pos[1] = self.tile[1] * self.tile_size

    def draw(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.screen.blit(self.image, (self.pos[0]-20, self.pos[1]-17))

    def direction_change(self, new_direction):
        #if self.maze.center_detection(): #or self.new_direction == [0, 0]:
            self.new_direction = new_direction
