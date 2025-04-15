import pygame



class gameObject():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load("bilder/placeholder.png")
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

    def set_image(self,):
        self.image = pygame.image.load(self.image)
        self.image = pygame.transform.scale(self.image, (100, 100))
    
    def draw(self, screen):
        screen.blit(self.image, self.rect.center)
