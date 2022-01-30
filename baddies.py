import pygame
import os
import copy

from helpers.Constants import Constants


class Baddies(pygame.sprite.Sprite):

    def __init__(self, screen, maze, target_distance, tile_size):
        game_folder = os.path.dirname(__file__)
        sprite_folder = os.path.join(game_folder, 'sprites')
        self.sprite = pygame.image.load(os.path.join(sprite_folder, 'small_jonko.png')).convert()
        pygame.display.init()
        pygame.sprite.Sprite.__init__(self)
        self.sprite.set_colorkey((0, 0, 0))
        self.screen = screen
        self.pos = [50, Constants.Window_height-50]
        self.direction = [0, 0]
        self.speed = 1 / 8
        self.rect = self.sprite.get_rect()
        self.rect.center = (400, 400)
        self.maze = maze
        self.tile_size = tile_size
        self.search_started = False
        self.temp_shark_pos = (99, 99)
        self.temp_direction = [[]]
        self.tiles_moved = 0
        self.target_distance = target_distance
        self.route = []

    def update(self, shark_pos):
        if self.maze.manhat_dist(self.maze.get_tile(self.pos, self.tile_size),self.maze.get_tile(shark_pos, self.tile_size)) <= 20:#self.tiles_moved >= 1 or not self.search_started:
            print("start")
            self.search_started = True
            self.tiles_moved = 0
            self.temp_shark_pos = copy.deepcopy(shark_pos)
            self.route.clear()
            self.route = copy.deepcopy(self.greedy_search(self.temp_shark_pos))
            self.route.pop(0)
            #print(self.route)
        else:
            #self.search_started = False
            #if self.maze.collision_detection_straight(self.pos, self.direction, self.tile_size):
            tile = self.maze.get_tile(self.pos, self.tile_size)*self.tile_size
            print("shit")
            #self.pos = [tile[0]*(self.tile_size+0.01), tile[1]*(self.tile_size+0.01)]
            if self.maze.collision_detection_straight(self.pos, self.direction, self.tile_size):#self.search_started:
                self.direction[0] = 0
                self.direction[1] = 0
                temp_tile = self.maze.get_tile(self.pos, self.tile_size)
                self.pos[0] = temp_tile[0]*self.tile_size
                self.pos[1] = temp_tile[1]*self.tile_size
                self.search_started = False
        if self.route: # != [420, 420]: # len(self.route) > 0:
            print("check")
            if self.maze.center_detection(self.pos): #and \
                    #self.maze.get_tile(self.pos, self.tile_size) == self.route[0]:
                print(self.route)
                self.tiles_moved += 1
                tile = self.maze.get_tile(self.pos, self.tile_size)
                self.direction[0] = self.route[0][0] - tile[0]
                self.direction[1] = self.route[0][1] - tile[1]
                self.temp_direction = self.direction
                print(self.direction)
                self.route.pop(0)
            else:
                self.direction = self.temp_direction

        #print(self.maze.manhat_dist(self.maze.get_tile(self.pos, self.tile_size),self.maze.get_tile(shark_pos, self.tile_size)))
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed

    def draw(self):
        self.screen.blit(self.sprite, (self.pos[0], self.pos[1]))

    def greedy_search(self, shark_pos):
        current_tile = self.maze.get_tile(self.pos, self.tile_size)
        target_tile = self.maze.get_tile(shark_pos, self.tile_size)
        queue = [current_tile]
        visited = []
        options = {}
        sorted_options = []

        while len(queue) > 0:
            current_node = queue.pop(0)
            if self.maze.manhat_dist(current_node, target_tile) < 20:
                if current_node not in visited:
                    visited.append(current_node)
                    neighbours = self.maze.get_neighbours(current_node)
                    options.clear()
                    sorted_options.clear()
                    for next_node in neighbours:
                        if next_node not in visited:
                            score = self.maze.manhat_dist(next_node, target_tile)
                            options[next_node] = score
                    sorted_options = sorted(options.items(), key=lambda kv: (kv[1], kv[0]), reverse=False)
                    for a in range(len(sorted_options)):
                        queue.insert(0, sorted_options[a][0])
            else:
                if visited:
                    return visited
                else:
                    return [[420, 420]]
