import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.gravity = 0
        self.velocity = 5
        self.max_health = 3
        self.curr_health = 3
  
        self.image = pygame.transform.scale(pygame.image.load('graphics/Charalampost_Right.png').convert_alpha(), (60,140))
        self.rect = self.image.get_rect(midbottom = (200,400))
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 400:
            self.gravity = -17
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect.right <= 800:
            # Move right and change to right image
            self.rect.x += self.velocity
            self.image = pygame.image.load('graphics/Charalampost_Right.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (60,140))
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.left >= 0:
            # Move left and change to right image
            self.rect.x -= self.velocity
            self.image = pygame.image.load('graphics/Charalampost_Left.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (60,140))

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 400:
            self.rect.bottom = 400

    def update(self):
        self.player_input()
        self.apply_gravity()

    def get_curr_health(self):
        return self.curr_health
    
    def get_max_health(self):
        return self.max_health