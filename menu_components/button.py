import pygame


class Button:

  def __init__(self,x,y,width,height, font_size=20,text=""):
    self.rect = pygame.Rect(x,y,width,height)
    self.text = text
    self.font = pygame.font.Font(None, font_size)
    self.is_clicked = False
    self.background_color = (228, 58, 58)
    self.active = False


  def event_on_button_clicked(self,event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and self.active:
          if self.is_clicked == True:
            self.is_clicked = False
            self.background_color = (228, 58, 58)
          else:
            self.is_clicked = True
            self.background_color = (34, 155, 60)
          return self.is_clicked

  def draw(self, surface):
    pygame.draw.rect(
            surface,
            self.background_color,
            self.rect,
            border_radius=5)
    
    # Text
    text_surface = self.font.render(self.text, True, (254,254,254))
    text_rect = text_surface.get_rect(
                midleft=(self.rect.x + 8, self.rect.centery)
            )
    surface.blit(text_surface, text_rect)

