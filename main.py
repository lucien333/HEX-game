import pygame,sys
from game_screen import * 
from Buttons import Buttons
from Mouse import Mouse

#general settings 
pygame.init() 
clock = pygame.time.Clock() 

#class mouse 
class Mouse(pygame.sprite.Sprite): 
    def __init__(self,picture_path):  
        super().__init__() 
        self.image = pygame.image.load(picture_path) 
        self.rect = self.image.get_rect() 

    def color_change(self): 
        pygame.sprite.spritecollide(mouse,buttons_group,True) 
    
    def update(self): 
        self.rect.center = pygame.mouse.get_pos() 
        
#mouse
mouse = Mouse("images/crosshair.png")
mouse_group = pygame.sprite.Group()
mouse_group.add(mouse)


#buttons
buttons_group = pygame.sprite.Group() 
for i in range(11):
    for g in range(11):
        grey_button = Buttons("images/bouton.gif",246+30*i+15*g,240+25*g) 

     
        buttons_group.add(grey_button) 


#game loop
while True: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse.color_change()
            
   
    pygame.display.flip() 
    screen.blit(background,(0,0)) 
    screen.blit(game_board,(200,200)
    buttons_group.draw(screen) 
    mouse_group.draw(screen)
    mouse_group.update()
    clock.tick(60) 
    
