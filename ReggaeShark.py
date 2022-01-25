import pygame
import os
from helpers.Constants import Constants


class ReggaeShark:

    def __init__(self, screen):
        game_folder = os.path.dirname(__file__)
        sprite_folder = os.path.join(game_folder, 'sprites')
        self.sprite = pygame.image.load(os.path.join(sprite_folder, 'reggae_shark.png')).convert()
        self.rect = self.sprite.get_rect()
        self.rect.center = (400, 400)
        self.sprite.set_colorkey((0, 0, 0))
        self.screen = screen
        self.pos = [400, 400]
        self.direction = [0, 0]
        self.speed = 1 / 8

    def update(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed

    def draw(self):
        self.screen.blit(self.sprite, (self.pos[0], self.pos[1]))

    def direction_change(self, new_direction):
        self.direction = new_direction
