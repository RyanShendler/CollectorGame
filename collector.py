import pygame

#Global Variables
screen_width = 1600
screen_height = 900
background = pygame.image.load("images/background.png")

def move(item, x, y):
    item_rect = item.get_rect()
    current_x = item_rect.x
    new_x = current_x + x
    current_y = item_rect.y
    new_y = current_y + y
    width = item_rect.width
    height = item_rect.height
    if (new_x)>0 and (new_x + width)<screen_width and (new_y)>0 and (new_y + height)<screen_height:
        screen.blit(background, (0,0))
        screen.blit(item, (new_x,new_y))
        pygame.display.flip()
        

def main():
    #Startup
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    running = True

    #Images
    image = pygame.image.load("images/stickman.png")

    #Local Variables
    xpos = 50
    ypos = 50

    
    #Initialization
    screen.blit(background, (0,0))
    screen.blit(image, (xpos,ypos))
    pygame.display.flip()

    #main loop
    while running:
        for event in pygame.event.get():
            #check for quit
            if event.type == pygame.QUIT:
                pygame.quit(); 
                running = False

            #movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ypos-=25
                    screen.blit(background, (0,0))
                    screen.blit(image, (xpos,ypos))
                    pygame.display.flip()
                if event.key == pygame.K_a:
                    xpos-=25
                    screen.blit(background, (0,0))
                    screen.blit(image, (xpos,ypos))
                    pygame.display.flip()
                if event.key == pygame.K_s:
                    ypos+=25
                    screen.blit(background, (0,0))
                    screen.blit(image, (xpos,ypos))
                    pygame.display.flip()
                if event.key == pygame.K_d:
                    xpos+=25
                    screen.blit(background, (0,0))
                    screen.blit(image, (xpos,ypos))
                    pygame.display.flip()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
            
                if event.key == pygame.K_a:
                    
                if event.key == pygame.K_s:
                    
                if event.key == pygame.K_d:
                   

if __name__=="__main__":
    main()
