# Написати код анімації квадрата, який переміщається від лівої межі до правої, 
# дотикається до неї, але не зникає за нею. Після цього повертається назад – 
# від правої межі до лівої, дотикається до неї, і знову рухається вправо. 
# Цикли руху квадрата повторюються до завершення програми. 


import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game")
#clock = pygame.time.Clock()

x=230
y=190
width=40
height=60
#base movement step and starting direction
mx = 10
direct = "left"

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    # movement increment

    def movement(x, y, width, height, direct):
        
        #define direction
        if x > 500-width-15:
            direct = "left"

        elif x < 0+15:
            direct = "right"

        if direct == "right":
            x += mx

        elif direct == "left":
            x -= mx

        #draw rectangle
        pygame.draw.rect(screen, (81,87,59), [x, y, width, height])

        return x, direct

    #without trace
    screen.fill((228,234,230))          
    
    #unpacking tuple from function and assigning it to function
    x, direct = movement(x, y, height, width, direct)
    pygame.display.update()
    clock.tick(60)