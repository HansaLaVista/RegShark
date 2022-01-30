import pygame
import os

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
        self.pos = [50,Constants.Window_height-50]#Constants.Window_width -50, Constants.Window_height - 50]
        self.direction = [0, 0]
        self.speed = 1 / 8
        self.rect = self.sprite.get_rect()
        self.rect.center = (400, 400)
        self.maze = maze
        self.tile_size = tile_size
        self.greedy_found = False
        self.shark_pos = ()
        self.target_distance = target_distance

    def update(self, shark_pos):
        if not self.greedy_found:
            print(self.greedy_search(shark_pos))
            self.greedy_found = True
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
            print(queue)
            current_node = queue.pop(0)
            print(self.maze.manhat_dist(current_node, target_tile))
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
                    sorted_options = sorted(options.items(), key = lambda kv: (kv[1],kv[0]), reverse=False)
                    print(options)
                    print(sorted_options)
                    for a in range(len(sorted_options)):
                        queue.insert(0,sorted_options[a][0])
            else:
                return visited
        pass