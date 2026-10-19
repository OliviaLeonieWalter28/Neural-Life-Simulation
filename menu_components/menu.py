import pygame
from .input_box import InputBox
from .button import Button
from .label import Label


MENU_COLOUR = (73,84,70) # GREY

class Menu:

  def __init__(self):
     pygame.init()
     self.input_box = InputBox(900, 0, 200, 45, max_length=30)
     self.button = Button(840,550,120,30,text="Debug Steering")
     self.label = Label(800,0,200,500,text="Generations")
     self.font = pygame.font.Font(None,32)

  def handle_menu_events(self, event):
     self.input_box.event_on_interact(event)
     value = self.button.event_on_button_clicked(event)
     return value


  def draw_menu(self, screen):
   
      pygame.draw.rect(screen,MENU_COLOUR,(800,0,200,600))
      
      self.input_box.draw(screen)
      self.button.draw(screen)
      self.label.draw(screen)


  