import pygame
from Map import Maze


class GameView:

    def __init__(self, game, screen, font, maze_map, Tile_size, maze):
        self.game = game
        self.screen = screen
        screen_size = self.screen.get_size()
        self.tile_size = Tile_size
        self.offset = [100, 150]
        self.maze = maze
        self.map = [""]
        self.map = maze_map

    def draw_game(self):
        self.draw_maze()


    def draw_maze(self):
        for a in range(len(self.map)):
            for b in range(len(self.map[0])):
                if self.map[a][b] == ".":
                    pygame.draw.rect(self.screen, [255,255,255], [a*25,b*25,25,25])
                else:
                    pygame.draw.rect(self.screen, [0, 0, 0], [a * 25 +1, b * 25 +1, 25, 25])