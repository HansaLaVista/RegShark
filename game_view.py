import pygame

import os


class GameView:

    def __init__(self, game, screen, maze_map, tile_size, maze):
        self.map = [""]
        self.map = maze_map
        self.game = game
        self.screen = screen
        # screen_size = self.screen.get_size()
        game_folder = os.path.dirname(__file__)
        sprite_folder = os.path.join(game_folder, 'sprites')
        self.sprite = pygame.image.load(os.path.join(sprite_folder, 'Coral.png')).convert()
        self.rect = self.sprite.get_rect()
        self.sprite.set_colorkey((0, 0, 0))
        self.tile_size = tile_size
        self.offset = [100, 150]
        self.maze = maze
        #self.map = []
        self.map = maze_map

    def draw_game(self):
        self.draw_maze()

    def draw_maze(self):
        pass
        for a in range(len(self.map)):
            for b in range(len(self.map[0])):
                if self.map[a][b] == ".":
                    pygame.draw.rect(self.screen, [255, 255, 255], [a * self.tile_size, b * self.tile_size, self.tile_size, self.tile_size], 1)
                else:
                    self.screen.blit(self.sprite, [a * self.tile_size, b * self.tile_size])
