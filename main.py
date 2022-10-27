import pygame 
from game_screen import * 
from Buttons import Buttons
from Mouse import Mouse

#general settings 
pygame.init() 
clock = pygame.time.Clock() 


        
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
            
   
    pygame.display.flip() 
    screen.blit(background,(0,0)) 
    screen.blit(game_board,(200,200))
    clock.tick(60) 
   
   
    buttons_group.draw(screen) 



    mouse_group.draw(screen)
    mouse_group.update()
    
