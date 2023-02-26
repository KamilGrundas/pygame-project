import sys
import pygame
from settings import Settings



class Dungeons():

    def __init__(self):

        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height))


        pygame.display.set_caption("Dungeons")


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    ai = Dungeons()
    ai.run_game()

