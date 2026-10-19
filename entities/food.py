import pygame
import os


class Food:
    screen_size = (0,0)
    food_value = 0

    def __init__(self, x, y, food_value, sprite_name, screen_size):
        self.sprite = pygame.image.load(os.path.join("assets", f"{sprite_name}"))
        self.rect = self.sprite.get_rect()
        self.x = x
        self.y = y
        self.food_value = food_value
        self.screen_size = screen_size

    def return_collision_area(self):
        width = self.x + (self.rect.width * 2)
        height = self.y + (self.rect.height * 2)
        collision_area = [self.x,self.y, width, height]
        return collision_area 
    
    def draw(self, screen):
        scaled_sprite = pygame.transform.scale(
            self.sprite, (self.rect.width * 2, self.rect.height * 2)
        )
        screen.blit(scaled_sprite, (self.x, self.y))
