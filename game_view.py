from pygame import draw


class GameView:

    def __init__(self, game, screen, font):
        self.game = game
        self.screen = screen
        screen_size = self.screen.get_size()
        self.offset = [100, 150]

    def draw_game(self):
        self.draw_maze()


    def draw_maze(self):
        pass