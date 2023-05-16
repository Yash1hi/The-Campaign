import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))


class Headshot(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
  
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200,300))
        if position == "left":
            self.rect = self.image.get_rect(bottomleft = (400,0))
        if position == "right":
            self.rect = self.image.get_rect(bottomright = (400,800))
            
    
    def player_input(self):
        pass

    def update(self):
        pass