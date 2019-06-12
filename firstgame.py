import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600
car_width = 45
car_height = 92
bg_color = (50,50,50)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('To The Limit')
clock = pygame.time.Clock()

car_img = pygame.image.load('carimg.png')
road_img = pygame.image.load('road.png')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " +str(count), True, yellow)
    gameDisplay.blit(text, (0,0))
    
def car(x,y):
    gameDisplay.blit(car_img,(x,y))
def road(x,y):
    gameDisplay.blit(road,(x,y))
def text_objects(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()
def msg_display(text):
    policeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects(text, policeText)
    TextRect.center = (400,300)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
def crashed():
    msg_display('BOOM!')
   
  

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_move = 0
    y_move = 0
    thing_startx = random.randrange(0, 1000)
    thing_starty = 600
    thing_speed = 7
    thing_width = 50
    thing_height = 50
    thingCount = 1
    dodged = 0
        
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -5
                elif event.key == pygame.K_RIGHT:
                    x_move = +5
                elif event.key == pygame.K_UP:
                    y_move = -5
                elif event.key == pygame.K_DOWN:
                    y_move = +5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0
        x += x_move
        y += y_move

        gameDisplay.fill(road_img)
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        if x > display_width - car_width or x < 0:
            crashed()
        if y > display_height - car_height or y < 0:
            crashed()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.2
        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crashed()
            
        pygame.display.update()
        clock.tick(60)
        
#game_intro()        
game_loop()    
pygame.quit()
quit()
