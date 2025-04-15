# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1270, 670))
#background = pygame.image.load("bilder/sandTexture.png")
clock = pygame.time.Clock()
running = True
dt = 0
speed = 300

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Spielfigure ubloading
spielerfigur = pygame.image.load("bilder/biene.png")

hubschrauber2 = pygame.image.load("bilder/hubschrauber2.png")
resized_image = pygame.transform.scale(hubschrauber2,(100,100))

tankstelle = pygame.image.load("bilder/tankstelle.png")
resized_image2 = pygame.transform.scale(tankstelle,(100,100))  

home = pygame.image.load("bilder/home.png")
resized_image3 = pygame.transform.scale(home,(100,100))

steine = pygame.image.load("bilder/steine.png")
resized_image4 = pygame.transform.scale(steine,(100,100))


#resized_image5 = pygame.transform.scale(background,(1270,670))


# Spielschleife
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")
    screen.fill("white")
    # Bewegung Verwaltung
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= speed * dt
    if keys[pygame.K_s]:
        player_pos.y += speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= speed * dt
    if keys[pygame.K_d]:
        player_pos.x += speed * dt
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    # Boundary checks
    if player_pos.x < 0:
        player_pos.x = 0
    if player_pos.x > screen.get_width() - spielerfigur.get_width():
        player_pos.x = screen.get_width() - spielerfigur.get_width()
    if player_pos.y < 0:
        player_pos.y = 0
    if player_pos.y > screen.get_height() - spielerfigur.get_height():
        player_pos.y = screen.get_height() - spielerfigur.get_height()

   # pygame.draw.rect(screen, (255,255,255), (30, 20, 100, 200), 10 )
    
    screen.blit(resized_image, (1000, 250))
    screen.blit(resized_image2, (600, 569))   
    screen.blit(resized_image3, (1100, 400))
    screen.blit(resized_image4, (150, 100))
    screen.blit(spielerfigur, (player_pos.x, player_pos.y))
    #screen.blit(resized_image5, (1270, 670))
    #screen.blit(background, (0, 0))


    # flip() the display to put your work on screen
    pygame.display.flip()   
    

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()