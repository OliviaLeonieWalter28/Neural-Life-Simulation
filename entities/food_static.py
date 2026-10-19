import pygame
from entities.food import Food


class Food_static(Food):

    def __init__(self, screen_size, x, y):
        super().__init__(x, y, 1, "food_static.png", screen_size)

