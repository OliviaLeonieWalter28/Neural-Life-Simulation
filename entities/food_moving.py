import pygame
from entities.food import Food
from direction import Direction
import random


class Food_moving(Food):
    screen_size = (0,0)
    def __init__(self, x, y, screen_size):
        self.screen_size = screen_size
        super().__init__(x, y, 3, "food_moving.png", screen_size)

    def move(self):
        direction = random.choice(list(Direction))
        dx, dy = direction.value
        new_x = self.x + dx * 3
        new_y = self.y + dy * 3

        sprite_width = self.rect.width * 2
        sprite_height = self.rect.height * 2

        if 0 <= new_x <= self.screen_size[0] - sprite_width:
            self.x = new_x

        if 0 <= new_y <= self.screen_size[1] - sprite_height:
            self.y = new_y
