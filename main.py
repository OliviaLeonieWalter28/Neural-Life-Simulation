import pygame
import random
from entities.creature import Creature
from entities.food import Food
from entities.food_static import Food_static
from entities.food_moving import Food_moving
from menu_components.menu import Menu

pygame.init()

# Globals
BACKGROUND_COLOR = (0, 0, 0)  # BLACK
SCREEN_SIZE = (800,600)
FONT = pygame.font.Font(None,32)
DEBUG_STEERING = False

screen = pygame.display.set_mode((SCREEN_SIZE[0] + 200, SCREEN_SIZE[1]))
clock = pygame.time.Clock()
running = True
menu = Menu()

# Entities
creature = Creature(SCREEN_SIZE) 
food = []

def check_collision():
    creature_collision_area = creature.return_collision_area()
    food_pos = 0
    for f in food:
        f_collision_area = f.return_collision_area()
        
        for x in range (f_collision_area[0], f_collision_area[2], 1):
            if x >= creature_collision_area[0] and x <= creature_collision_area[2]:
                 for y in range (f_collision_area[1], f_collision_area[3], 1):
                    if y >= creature_collision_area[1] and y <= creature_collision_area[3]:  
                        creature.eat(f.food_value)
                        food.pop(food_pos)
                        return
        food_pos += 1
   # print("no collsion")

def spawn_food():
    if len(food) < 5:
        x = random.randint(0, SCREEN_SIZE[0]-64)
        y = random.randint(0, SCREEN_SIZE[1]-64)

        food_type = random.choice([Food_moving, Food_static])
        food.append(food_type(x=x, y=y, screen_size=SCREEN_SIZE))



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        debug_value = menu.handle_menu_events(event)
        if debug_value is not None:
            DEBUG_STEERING = debug_value

    # fill the screen with a color to wipe away anything from last frame

    screen.fill(BACKGROUND_COLOR)

    # RENDER YOUR GAME HERE

    # ACTIONS 

    check_collision()
    spawn_food()

    creature.calculate_bodyfuel_usage()
    creature.vision(food)
    creature.think(DEBUG_STEERING)

    # DRAW

    for f in food:
        if type(f) == Food_moving:
            f.move()
        f.draw(screen)

    creature.draw(screen)
    menu.draw_menu(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
