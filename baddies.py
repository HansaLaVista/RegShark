import pygame
import os

from helpers.Constants import Constants


class Baddies(pygame.sprite.Sprite):

    def __init__(self, screen, maze, tile_size):
        game_folder = os.path.dirname(__file__)
        sprite_folder = os.path.join(game_folder, 'sprites')
        self.sprite = pygame.image.load(os.path.join(sprite_folder, 'small_jonko.png')).convert()
        pygame.display.init()
        pygame.sprite.Sprite.__init__(self)
        self.sprite.set_colorkey((0, 0, 0))
        self.screen = screen
        self.maze = maze
        self.tile_size = tile_size
        self.pos = [Constants.window_width / 2, Constants.window_height - 50]
        self.direction = [0, 0]
        self.speed = 1 / 8
        self.rect = self.sprite.get_rect()
        self.rect.center = (400, 400)

    def update(self, shark_pos):
        shark_tile = self.maze.get_tile(shark_pos, self.tile_size)
        # queue = self.greedy_search(shark_tile)
        # self.direction = queue[0]-self.maze.get_tile(self.pos, self.tile_size)
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed

    def draw(self):
        self.screen.blit(self.sprite, (self.pos[0], self.pos[1]))

    def greedy_search(self, shark_pos):
        target_tile = self.maze.get_tile(shark_pos, self.tile_size)
        current_tile = self.maze.get_tile(self.pos, self.tile_size)
        gstack = [current_tile]
        visited = []
        scores = [999]
        counter = 0
        temp_lowest = 999
        temp_tile = [99,99]

        while len(gstack) > 0:
            current_tile = gstack.pop(0)
            if current_tile != target_tile:
                if current_tile != visited or current_tile == visited:
                    visited.append(current_tile)
                    neighbours = self.maze.get_neighbours(current_tile)
                    for next_tile in neighbours:
                        if next_tile not in visited:
                            score = self.maze.manhat_distance(next_tile, target_tile)
                            scores.insert(0,score)
                            for b in range(len(scores)):
                                if score < scores[b]:
                                    temp_lowest = score
                                    temp_tile = next_tile
                    gstack.insert(0, temp_tile)
            else:
                break
        return visited
