import pygame


class ReggaeShark:

    def __init__(self, screen):
        self.screen = screen
        self.pos = [400, 400]
        self.direction = [0, 0]
        self.speed = 1/8

    def update(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed

    def draw(self):
        pygame.draw.ellipse(self.screen, [255, 255, 255], [[self.pos[0], self.pos[1]], [20, 20]])

    def direction_change(self, new_direction):
        self.direction = new_direction
