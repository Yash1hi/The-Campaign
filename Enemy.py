import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/Protestor.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,80))
        self.rect = self.image.get_rect(midbottom = (1100,400))
        self.velocity = -3

    def update(self):
        if self.rect.x < 0:
            self.velocity = 3
        self.rect.x += self.velocity
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100: 
            self.kill()
