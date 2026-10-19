from direction import Direction
from entities.food import Food
import os
import pygame
import random

class Creature:

    SPRITE_ALIVE = "creature.png"
    SPRITE_DEAD = "creature_dead.png"
    SPRITE_ASLEEP = "creature_sleeping.png"
    sprite_path = os.path.join("assets", SPRITE_ALIVE)
    screen_size = (0,0)
    
    hunger_multiplier = 0.01
    fatigue_multiplier = 0.03

   
    hunger = 0
    fatigue = 0
    is_alive = True
    is_asleep = False

    vision_food = []


    def __init__(self, screen_size):
        self.sprite = pygame.image.load(self.sprite_path)
        self.rect = self.sprite.get_rect()
        self.x = 0
        self.y = 0
        self.screen_size = screen_size

    def sleep(self):
        if self.is_asleep == False:
            self.is_asleep = True
            self.sprite_path = os.path.join("assets", self.SPRITE_ASLEEP)
            self.sprite = pygame.image.load(self.sprite_path)
        if self.fatigue > 5:
            self.fatigue -= 0.2
        else:
            self.fatigue = 0
        r = random.randint(0, int(self.fatigue) * 6)
        print(r)
        if r == 1 or self.fatigue == 0:
            self.is_asleep = False
            self.sprite_path = os.path.join("assets", self.SPRITE_ALIVE)
            self.sprite = pygame.image.load(self.sprite_path)

    def vision(self, food):
        self.vision_food.clear()
        vision_rectangle = [self.x + 200, self.x - 200, self.y + 200, self.y - 200]
        for f in food:
            if f.x <= vision_rectangle[0] and f.x >= vision_rectangle[1]:
                if f.y <= vision_rectangle[2] and f.y >= vision_rectangle[3]:
                    self.vision_food.append(f)
                    print(len(self.vision_food))

        
    def think(self, is_debug):
        if self.is_alive == False:
            return
        if self.is_asleep == True:
            self.sleep()
            return
        if is_debug:
            self.debug_move()
        else:
            self.move(*self.choose_direction())

    def choose_direction(self):
        direction = random.choice(list(Direction))
        return direction.value

    def calculate_bodyfuel_usage(self):
        self.hunger += self.hunger_multiplier
        self.fatigue += self.fatigue_multiplier
        print(f"hunger: {self.hunger}")
        print(f"energy: {self.fatigue}")
        if self.fatigue >= 50:
            self.sleep()
        if self.hunger >= 10: 
            self.sprite_path = os.path.join("assets", self.SPRITE_DEAD)
            self.sprite = pygame.image.load(self.sprite_path)
            self.is_alive = False
        
    def debug_move(self):
        keys = pygame.key.get_pressed()

        sprite_width = self.rect.width * 2
        sprite_height = self.rect.height * 2  

        if keys[pygame.K_w]:
            new_y = self.y + -1 * 5
            if 0 <= new_y <= self.screen_size[0] - sprite_height:
                self.y = new_y
        if keys[pygame.K_s]:
            new_y = self.y + 1 * 5
            if 0 <= new_y <= self.screen_size[0] - sprite_height:
                        self.y = new_y
        if keys[pygame.K_a]:
            new_x = self.x + -1 * 5
            if 0 <= new_x <= self.screen_size[0] - sprite_width:
                self.x = new_x
        if keys[pygame.K_d]:
            new_x = self.x + 1 * 5
            if 0 <= new_x <= self.screen_size[0] - sprite_width:
                self.x = new_x
    
    def move(self, dx, dy):
        new_x = self.x + dx * 5
        new_y = self.y + dy * 5

        sprite_width = self.rect.width * 2
        sprite_height = self.rect.height * 2

        if 0 <= new_x <= self.screen_size[0] - sprite_width:
            self.x = new_x

        if 0 <= new_y <= self.screen_size[0] - sprite_height:
            self.y = new_y

    def eat(self, food_points):
        if self.hunger != 0:
            if food_points > self.hunger:
                self.hunger = 0
            else: 
                self.hunger -= food_points

    def procreate(self, matingPartner):
        
        
        matingPartner.procreate(self)
        

    # FUTURE - this will be more desired than the current collision check
    def collision(object_type):
        if type(object_type) == Food:
            pass

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

