#enemy class
import pygame
import os
import copy
import random


class Baddies(pygame.sprite.Sprite):

    def __init__(self, screen, maze, target_distance, tile_size, speed_extra, temp_arduino):
        game_folder = os.path.dirname(__file__)
        sprite_folder = os.path.join(game_folder, 'sprites')
        self.sprite = pygame.image.load(os.path.join(sprite_folder, 'small_jonko.png')).convert()
        pygame.display.init()
        pygame.sprite.Sprite.__init__(self)
        self.sprite.set_colorkey((0, 0, 0))
        self.screen = screen
        self.tile_size = tile_size
        self.direction = [0, 0]
        self.speed = (speed_extra + 10) / 200
        self.rect = self.sprite.get_rect()
        self.rect.center = (400, 400)
        self.maze = maze
        self.start_tile = [0, 0]
        while self.maze.final_2d_list[self.start_tile[0]][self.start_tile[1]] == '|':
            self.start_tile[0] = random.randint(1, len(self.maze.final_2d_list) - 1)
            self.start_tile[1] = random.randint(1, len(self.maze.final_2d_list[0]) - 1)
        self.pos = [self.start_tile[0] * self.tile_size, self.start_tile[1] * self.tile_size]
        self.search_started = False
        self.temp_shark_pos = (99, 99)
        self.temp_direction = [[]]
        self.tiles_moved = 0
        self.target_distance = target_distance
        self.route = []
        self.alive = True
        self.arduino = temp_arduino

    def update(self, shark_pos, dt):
        if self.alive:
            if self.maze.manhat_dist(self.maze.get_tile(self.pos, self.tile_size),
                                     self.maze.get_tile(shark_pos, self.tile_size)) <= self.target_distance:
                self.search_started = True
                self.tiles_moved = 0
                self.temp_shark_pos = copy.deepcopy(shark_pos)
                self.route.clear()
                self.route = copy.deepcopy(self.greedy_search(self.temp_shark_pos))
                self.route.pop(0)
            else:
                if self.maze.collision_detection_straight(self.pos, self.direction, self.tile_size):
                    self.direction[0] = 0
                    self.direction[1] = 0
                    temp_tile = self.maze.get_tile(self.pos, self.tile_size)
                    self.pos[0] = temp_tile[0] * self.tile_size
                    self.pos[1] = temp_tile[1] * self.tile_size
                    self.search_started = False

            if self.route:
                if self.maze.center_detection(self.pos):
                    self.tiles_moved += 1
                    tile = self.maze.get_tile(self.pos, self.tile_size)
                    self.direction[0] = self.route[0][0] - tile[0]
                    self.direction[1] = self.route[0][1] - tile[1]
                    self.temp_direction = self.direction
                    self.route.pop(0)
                else:
                    self.direction = self.temp_direction

            self.pos[0] += self.direction[0] * self.speed * dt
            self.pos[1] += self.direction[1] * self.speed * dt
            self.collision(shark_pos)

        else:
            self.pos = [-20, -20]

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
            if self.maze.manhat_dist(current_node, target_tile) < self.target_distance:
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

    def collision(self, shark_pos):
        if (self.pos[0] - self.tile_size <= shark_pos[0] <= self.pos[0] + self.tile_size) and \
                (self.pos[1] - self.tile_size <= shark_pos[1] <= self.pos[1] + self.tile_size):
            self.alive = False
