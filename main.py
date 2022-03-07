from tkinter import W
from unittest import runner
import pygame
from game import Game

if __name__ == '__main__':
    # initialisation
    pygame.init()
    game = Game()
    game.run()

pygame.quit()