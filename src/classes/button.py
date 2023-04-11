import pygame


import classes.lastscavenger as lastscavenger


class Button():
    def __init__(self, 
                 ls: lastscavenger.LastScavenger,
                 title: str, 
                 title_color: tuple,
                 color: tuple, 
                 hover_color: tuple,
                 width: int, 
                 height: int,
                 x: int,
                 y: int):
        self.title = title
        self.title_color = title_color
        
        self.color = color
        self.hover_color = hover_color
        
        self.width = width
        if ls.gameFrameWidth < width:
            self.width = ls.gameFrameWidth
        self.height = height
        if ls.gameFrameHeight < height:
            self.height = ls.gameFrameHeight

        self.x = x
        if x < 0 or x > ls.gameFrameWidth:
            self.x = 0
        self.y = y
        if y < 0 or y > ls.gameFrameHeight:
            self.y = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, displaySurf: pygame.Surface, font: pygame.font.Font):
        pygame.draw.rect(displaySurf, self.color, self.rect)
        
        button_surface = font.render(self.title, True, self.title_color)
        button_rect_center = button_surface.get_rect(center=self.rect.center)
        displaySurf.blit(button_surface, button_rect_center)

    def draw_hover(self, displaySurf: pygame.Surface):
        pygame.draw.rect(displaySurf, self.hover_color, self.rect)