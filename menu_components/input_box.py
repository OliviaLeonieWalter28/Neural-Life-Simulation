
import pygame


class InputBox:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        font_size=28,
        text="",
        max_length=None
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, font_size)

        self.text = text
        self.max_length = max_length
        self.active = False
        self.submitted = False

        self.color_inactive = (120, 120, 120)
        self.color_active = (80, 160, 255)
        self.text_color = (30, 30, 30)
        self.background_color = (245, 245, 245)

        self.border_color = self.color_inactive

    def event_on_interact(self, event):
        self.submitted = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.border_color = (
                self.color_active if self.active
                else self.color_inactive
            )

        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.submitted = True

            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]

            elif event.key == pygame.K_ESCAPE:
                self.active = False
                self.border_color = self.color_inactive

            else:
                if (
                    self.max_length is None
                    or len(self.text) < self.max_length
                ):
                    if event.unicode.isprintable():
                        self.text += event.unicode

    def draw(self, surface):
        # Background
        pygame.draw.rect(
            surface,
            self.background_color,
            self.rect,
            border_radius=5
        )

        # Border
        pygame.draw.rect(
            surface,
            self.border_color,
            self.rect,
            width=2,
            border_radius=5
        )

        text_surface = self.font.render(
            self.text, True, self.text_color
        )

        text_rect = text_surface.get_rect(
            midleft=(self.rect.x + 8, self.rect.centery)
        )

        surface.blit(text_surface, text_rect)

    def get_text(self):
        return self.text

    def clear(self):
        self.text = ""
