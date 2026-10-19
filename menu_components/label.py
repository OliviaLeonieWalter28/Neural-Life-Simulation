import pygame

class Label:

  def __init__(self,x,y,width,height,font_size=20,text=""):
    self.rect = pygame.Rect(x,y,width,height)
    self.text = text
    self.font = pygame.font.Font(None, font_size) 
    self.text_colour = (0,0,0)

  def draw(self, surface):
    text_surface = self.font.render(self.text, True, self.text_colour)
    surface.blit(text_surface, self.rect)
    