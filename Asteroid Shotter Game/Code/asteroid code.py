import pygame, sys

def laser_update(laser_list, speed = 300):
    for rect in laser_list:
        rect.y -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect) # this will remove the laser when it reaches the end

    
    




#game init 
pygame.init() 
WINDOW_WIDTH = 1280 
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) 
clock = pygame.time.Clock()

#ship import
ship_surface = pygame.image.load("../Graphics/ship.png").convert_alpha()                                                     
ship_rect = ship_surface.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)) 

# background image
background_image = pygame.image.load("../Graphics/background.png").convert_alpha()
background_rect = background_image.get_rect(center = (640,360))

# the text fond
font = pygame.font.Font("../Graphics/subatomic.ttf", 50) 
text_surface = font.render("Score: ", True, ("white"))
text_rect = text_surface.get_rect(midbottom = (WINDOW_WIDTH/2,WINDOW_HEIGHT - 80))

# the laser
Laser_surface = pygame.image.load("../Graphics/laser.png").convert_alpha()       
laser_list = []
#laser_rect = Laser_surface.get_rect(midbottom = ship_rect.midtop) 




while True: 
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # 0.5 of delay
            print("shooting")
            laser_rect = Laser_surface.get_rect(midbottom = ship_rect.midtop)
            laser_list.append(laser_rect)
            print(laser_list)
        


    # the framerate limit
    dt = clock.tick(120) / 1000
    
    
    #mouse input
    ship_rect.center = pygame.mouse.get_pos() 
    
    # update
    laser_update(laser_list)

    pygame.time.get_ticks()

    #drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_image,background_rect)
    display_surface.blit(ship_surface, ship_rect)
    display_surface.blit(text_surface,text_rect)
    
    
    #for loop that draws the laser surface where the rects are
    for rect in laser_list:
        display_surface.blit(Laser_surface,rect)


    # the frame update
    pygame.display.update() 