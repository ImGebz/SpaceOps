#Created by Gabe Seale 3/21
#assets and audio-ib Jace


import pygame
import os
pygame.font.init()
pygame.mixer.init()

#GUI settings
pygame.display.set_caption("SpaceOps") #change gui window display name
WIDTH, HEIGHT = 900, 500 #width and height variables for surface(tuple)
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #create new window WIN with set dimensions

WHITE = (255,255,255) #variable contains the color white in rgb as a tuple
BLACK = (0,200,200) #color of middle barrier
NEON= (57,255,20) #bullet color shipb


BARRIER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT) #dimensions and position of middle barrier
                    #(left position, top position, width, height)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Images','NewBackground5.jpg')), (WIDTH, HEIGHT)) #background image

FPS = 60 #frames per second variable
Velocity = 6 #velocity value to control movement speed
BULLET_VEL = 15 #speed of projectiles
Max_Bullets = 4 #max bullets that can be on the screen at once for each ship


CollisionSound = pygame.mixer.Sound('Assets/Sounds/explosion.wav')
LaserSound = pygame.mixer.Sound('Assets/Sounds/laser.wav')

Ship_Width, Ship_Height = 90,70 #global width and height for ship obj


shipA_hit = pygame.USEREVENT + 1 #Define two new pygame events
shipB_hit = pygame.USEREVENT + 2 #each defines collision event for each ship

#font style for health and lives
HealthFont = pygame.font.SysFont('aldhabi', 40)
WinnerFont = pygame.font.SysFont('bahnschrift', 100)

#load ship 1 from file
Ship_A_IMG = pygame.image.load(
    os.path.join('Assets', 'Images', 'NewShipA.png'))
Ship_A = pygame.transform.rotate(pygame.transform.scale(Ship_A_IMG, (Ship_Width,Ship_Height)), 90) #pass scaled ship image as arg for rotation function
#load ship 2 from files
Ship_B_IMG = pygame.image.load(
    os.path.join('Assets', 'Images','NewShip2.png'))
Ship_B = pygame.transform.rotate(pygame.transform.scale(Ship_B_IMG, (Ship_Width,Ship_Height)), 90)

WASD_keysIMG = pygame.image.load(
      os.path.join('Assets', 'Images','WASDKeys.png'))
WASDkeys = pygame.transform.scale(WASD_keysIMG, (95,70))

Arrow_keysIMG = pygame.image.load(
      os.path.join('Assets', 'Images','ArrowKeysIMG.png'))
ARROWkeys = pygame.transform.scale(Arrow_keysIMG, (95,70))


#Function to draw into window
def draw_window(pos_ShipA, pos_ShipB, ShipA_bullets, ShipB_bullets,health_A, health_B): 
   
    WIN.blit(BACKGROUND, (0,0)) #draw bakcground image
    pygame.draw.rect(WIN, BLACK, BARRIER) #use draw module for barrier instead of blit(draw rectangle with defined border)
    
    
    shipA_caption = HealthFont.render("Lives: " + str(health_A),1,WHITE) #spaceship health text
    shipB_caption = HealthFont.render("Lives: " + str(health_B),1,WHITE)
    WIN.blit(WASDkeys, (50,400))
    WIN.blit(ARROWkeys,(750, 400))
    WIN.blit(shipB_caption, (WIDTH - shipB_caption.get_width() -10, 10)) #position health text
    WIN.blit(shipA_caption, (10, 10))
    WIN.blit(Ship_A, (pos_ShipA.x,pos_ShipA.y)) #"Blit" function takes a surface arg and pastes to screen
    WIN.blit(Ship_B, (pos_ShipB.x,pos_ShipB.y))#Pass object and specify position
   
    
    for bullet in ShipA_bullets: #iterate bullet list
          pygame.draw.rect(WIN, NEON, bullet) #draw colored rect for bullet
    for bullet in ShipB_bullets:
          pygame.draw.rect(WIN, NEON, bullet)
    
    pygame.display.update() #must update display after filling

#SpaceShip movement
def shipA_movement(keys_pressed, pos_ShipA):
    #Function moves spaceship and uses "and" to check for edge case
    if keys_pressed[pygame.K_a] and pos_ShipA.x -Velocity > 0: #LEFT
            pos_ShipA.x -= Velocity
    if keys_pressed[pygame.K_d] and pos_ShipA.x + Velocity  + pos_ShipA.width < BARRIER.x:#Right
            pos_ShipA.x += Velocity
    if keys_pressed[pygame.K_w] and pos_ShipA.y - Velocity > 0: #UP
            pos_ShipA.y -= Velocity
    if keys_pressed[pygame.K_s] and pos_ShipA.y + Velocity + pos_ShipA.height < HEIGHT : #DOWN
            pos_ShipA.y += Velocity

def shipB_movement(keys_pressed, pos_ShipB):
    if keys_pressed[pygame.K_LEFT] and pos_ShipB.x -Velocity > BARRIER.x + BARRIER.width: #LEFT
            pos_ShipB.x -= Velocity
    if keys_pressed[pygame.K_RIGHT] and pos_ShipB.x + Velocity  + pos_ShipB.width < WIDTH: #Right
            pos_ShipB.x += Velocity
    if keys_pressed[pygame.K_UP] and pos_ShipB.y - Velocity > 0 : #UP
            pos_ShipB.y -= Velocity
    if keys_pressed[pygame.K_DOWN] and pos_ShipB.y + Velocity + pos_ShipB.height < HEIGHT: #DOWN
            pos_ShipB.y += Velocity

#bullet movement and collision
def handle_bullets(ShipA_bullets, ShipB_bullets, pos_ShipA, pos_ShipB):
      #ShipA bullets
      for bullet in ShipA_bullets: #iterate list of bullets
            bullet.x += BULLET_VEL # x position is adjusted by bullet velocity value
            #check collision
            if pos_ShipB.colliderect(bullet): #both obj must  be rects 
                  pygame.event.post(pygame.event.Event(shipB_hit)) #call user defined event for collision
                  ShipA_bullets.remove(bullet) #bullet is removed from list
            #handle bullets off screen
            elif bullet.x > WIDTH: #elif so bullet is not removed twice
                  ShipA_bullets.remove(bullet)
                  
      
      #Ship B bullets
      for bullet in ShipB_bullets:
            bullet.x -= BULLET_VEL 
            if pos_ShipA.colliderect(bullet): #both obj must  be rects
                  pygame.event.post(pygame.event.Event(shipA_hit))
                  ShipB_bullets.remove(bullet)
            elif bullet.x < 0:
                  ShipB_bullets.remove(bullet)
#draw winner to screen
def winner(txt):
      draw = WinnerFont.render(txt, 1, WHITE) #render text into variable draw
      #draw at middle of screen
      WIN.blit(draw, (WIDTH/2 - draw.get_width()/2, HEIGHT/2 - draw.get_height()/2)) 
      pygame.display.update()
      pygame.time.delay(5000) #delay and display message, then restart game

                      
    

#Main
def main():
    clock = pygame.time.Clock() #clock variable
   
   #Ship position control
    pos_ShipA = pygame.Rect(100, 300, Ship_Width, Ship_Height) #create rectangle at current posistion
    pos_ShipB = pygame.Rect(700, 300, Ship_Width, Ship_Height)#

    ShipA_bullets = [] #bullet list 
    ShipB_bullets = [] #compares to Max bullets 
   
    health_A = 10 #health var for each ship
    health_B = 10
    
    pygame.mixer.music.load('Assets/Sounds/background.wav')
    pygame.mixer.music.play(1, 10)

    run = True #condition to continue while loop
    while run: #infinite loop to keep game window running
        #Main game loop
        clock.tick(FPS) #constant tick rate of 60 fps9
        
        for event in pygame.event.get(): #loop through list of events that are possible
            if event.type == pygame.QUIT: #check if user quit the game
                run = False
                pygame.quit() #if QUIT condition true, quit the game


            if event.type == pygame.KEYDOWN: #Keydown checks one key
                  if event.key == pygame.K_LCTRL and len(ShipA_bullets) < Max_Bullets: #check if shoot key is pressed and within max bullets
                       bullet = pygame.Rect(pos_ShipA.x + pos_ShipA.width, pos_ShipA.y + pos_ShipA.height//2 -2, 10, 5) #initial pos of bullet
                       ShipA_bullets.append(bullet) #add bullet to list
                       LaserSound.play() 
                  
                  if event.key == pygame.K_RCTRL and len(ShipB_bullets) < Max_Bullets:
                        bullet = pygame.Rect(pos_ShipB.x, pos_ShipB.y + pos_ShipB.height//2 -2, 10, 5)
                        ShipB_bullets.append(bullet)
                        LaserSound.play()
                        
       
            
            if event.type == shipA_hit: #handle losing lives upon event
                  health_A -= 1
                  CollisionSound.play()  
                
            
            if event.type == shipB_hit:  
                  health_B -= 1
                  CollisionSound.play()  
        
        winner_txt = "" 
        if health_A <= 0: #BLUE ship message
            winner_txt = "Blue ship wins!"
        
        if health_B <=0: #Red ship message
              winner_txt = "Red ship wins!"

        if winner_txt != "": #display winner text
              winner(winner_txt)
              break #break so game restarts aftermessage delay
        
        keys_pressed = pygame.key.get_pressed() #get pressed function to return keys that are pressed(multiple)
        shipA_movement(keys_pressed, pos_ShipA) 
        shipB_movement(keys_pressed, pos_ShipB)
        
        handle_bullets(ShipA_bullets, ShipB_bullets, pos_ShipA, pos_ShipB) #function call for bullets
        
        draw_window(pos_ShipA, pos_ShipB, ShipA_bullets, ShipB_bullets,health_A,health_B) #function call
        
    main()#start game again after a restart
    
if __name__ == "__main__":
    main()
    