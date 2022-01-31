#enemy class
import pygame
import os
import copy
import random


class Baddies(pygame.sprite.Sprite):

    def __init__(self, screen, maze, target_distance, tile_size, speed_extra, temp_arduino):
        game_folder = os.path.dirname(__file__)     # initialise variables
        sprite_folder = os.path.join(game_folder, 'sprites')
        self.sprite = pygame.image.load(os.path.join(sprite_folder, 'small_jonko.png')).convert()
        pygame.display.init()
        pygame.sprite.Sprite.__init__(self)
        self.sprite.set_colorkey((0, 0, 0))     # fix sprite settings
        self.screen = screen
        self.tile_size = tile_size
        self.direction = [0, 0]
        self.speed = (speed_extra + 10) / 200
        self.rect = self.sprite.get_rect()
        self.rect.center = (400, 400)
        self.maze = maze
        self.start_tile = [0, 0]
        while self.maze.final_2d_list[self.start_tile[0]][self.start_tile[1]] == '|':   #assign random start tile
            self.start_tile[0] = random.randint(1, len(self.maze.final_2d_list) - 1)
            self.start_tile[1] = random.randint(1, len(self.maze.final_2d_list[0]) - 1)
        self.pos = [self.start_tile[0] * self.tile_size, self.start_tile[1] * self.tile_size]
        self.temp_shark_pos = (99, 99)  # initialise variables
        self.temp_direction = [[]]
        self.tiles_moved = 0
        self.target_distance = target_distance
        self.route = []
        self.alive = True
        self.arduino = temp_arduino

    def update(self, shark_pos, dt):
        if self.alive:  # if not smoked
            if self.maze.manhat_dist(self.maze.get_tile(self.pos, self.tile_size),  #if distance is smaller than target distance
                                     self.maze.get_tile(shark_pos, self.tile_size)) <= self.target_distance:
                self.temp_shark_pos = copy.deepcopy(shark_pos)
                self.route.clear()  # clear route
                self.route = copy.deepcopy(self.greedy_search(self.temp_shark_pos))
                self.route.pop(0)   # set route and remove first tile since it's the start tile
            else:
                if self.maze.collision_detection_straight(self.pos, self.direction, self.tile_size):
                    self.direction[0] = 0   # if distance is bigger than target distance move until crash
                    self.direction[1] = 0
                    temp_tile = self.maze.get_tile(self.pos, self.tile_size)
                    self.pos[0] = temp_tile[0] * self.tile_size # reset position after stopping
                    self.pos[1] = temp_tile[1] * self.tile_size

            if self.route:  # if there is a route
                if self.maze.center_detection(self.pos):    # check if joint is in center of tile
                    tile = self.maze.get_tile(self.pos, self.tile_size)
                    self.direction[0] = self.route[0][0] - tile[0]  # set new direction depending on next tile in route
                    self.direction[1] = self.route[0][1] - tile[1]
                    self.temp_direction = self.direction
                    self.route.pop(0)   # pop tile from route
                else:
                    self.direction = self.temp_direction    # follow temporary direction

            self.pos[0] += self.direction[0] * self.speed * dt  # update position
            self.pos[1] += self.direction[1] * self.speed * dt
            self.collision(shark_pos)   # check for collision with shark

        else:
            self.pos = [-20, -20]   # if smoked remove from grid

    def draw(self):
            self.screen.blit(self.sprite, (self.pos[0], self.pos[1]))   # draw joint

    def greedy_search(self, shark_pos):
        current_tile = self.maze.get_tile(self.pos, self.tile_size)     # get current and 'target' tile
        target_tile = self.maze.get_tile(shark_pos, self.tile_size)
        queue = [current_tile]  # initialise que, visited possible neighbours and possible neighbours sorted
        visited = []
        options = {}
        sorted_options = []

        while len(queue) > 0:   # while there's a queue
            current_node = queue.pop(0) # remove current from queue
            if self.maze.manhat_dist(current_node, target_tile) < self.target_distance:     # if distance > target distance
                if current_node not in visited:     # if not visited yet
                    visited.append(current_node)    # add to visited
                    neighbours = self.maze.get_neighbours(current_node)
                    options.clear()     # clear old lists
                    sorted_options.clear()
                    for next_node in neighbours:    # go through neighbours
                        if next_node not in visited:
                            score = self.maze.manhat_dist(next_node, target_tile)
                            options[next_node] = score  # set score in library
                    sorted_options = sorted(options.items(), key=lambda kv: (kv[1], kv[0]), reverse=False)
                    for a in range(len(sorted_options)):    # insert sorted library into queue
                        queue.insert(0, sorted_options[a][0])
            else:
                if visited:     # return route
                    return visited
                else:
                    return [[420, 420]] # return variable to prevent errors

    def collision(self, shark_pos):
        if (self.pos[0] - self.tile_size <= shark_pos[0] <= self.pos[0] + self.tile_size) and \
                (self.pos[1] - self.tile_size <= shark_pos[1] <= self.pos[1] + self.tile_size):
            self.alive = False  # check collision based on tile size
