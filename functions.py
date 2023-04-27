#Created by Gabe Seale 
#assets and audio-ib Jace
#Adapted from TechWithTims' "Space Invaders" single player game
#https://youtu.be/Q-__8Xw9KTM


#Contains all functions and methods

#import variables from variable file
from variables import *

#Function to draw into window
def draw_window(pos_ShipA, pos_ShipB, ShipA_bullets, ShipB_bullets,health_A, health_B): 
   
    WIN.blit(BACKGROUND, (0,0)) #draw bakcground image
    pygame.draw.rect(WIN, BLACK, BARRIER) #use draw module for barrier instead of blit(draw rectangle with defined border)
    
    
    shipA_caption = HealthFont.render("Lives: " + str(health_A),1,WHITE) #define spaceship A health text variable
    shipB_caption = HealthFont.render("Lives: " + str(health_B),1,WHITE) #define spaceship B health text var
    #"Blit" function takes a surface arg and pastes to window
    WIN.blit(WASDkeys, (50,400)) #draw WASD key IMG onto bottom left of window
    WIN.blit(ARROWkeys,(750, 400)) #draw Arrow key IMG onto bottom right of window
    WIN.blit(shipB_caption, (WIDTH - shipB_caption.get_width() -10, 10)) #draw shipB health text to window
    WIN.blit(shipA_caption, (10, 10)) #Draw ShipA health caption to window
    WIN.blit(Ship_A, (pos_ShipA.x,pos_ShipA.y)) #Draw shipA object to window at given posistion
    WIN.blit(Ship_B, (pos_ShipB.x,pos_ShipB.y))#Draw shipB objet to window at given position
   
    
    for bullet in ShipA_bullets: #iterate bullet list for ShipA
          pygame.draw.rect(WIN, NEON, bullet) #draw colored rect for  each bullet
    for bullet in ShipB_bullets: #iterate bullet list for ShipB
          pygame.draw.rect(WIN, NEON, bullet)
    
    pygame.display.update() #must update display window to render "blit" drawing

#Handle SpaceShip movement
def shipA_movement(keys_pressed, pos_ShipA):
    #Function moves spaceship and uses "and" to check for edge case
    if keys_pressed[pygame.K_a] and pos_ShipA.x -Velocity > 0: #LEFT with "a" key
            pos_ShipA.x -= Velocity
    if keys_pressed[pygame.K_d] and pos_ShipA.x + Velocity  + pos_ShipA.width < BARRIER.x:#RIGHT with "d" key
            pos_ShipA.x += Velocity
    if keys_pressed[pygame.K_w] and pos_ShipA.y - Velocity > 0: #UP with "w" key
            pos_ShipA.y -= Velocity
    if keys_pressed[pygame.K_s] and pos_ShipA.y + Velocity + pos_ShipA.height < HEIGHT : #DOWN with "s" key
            pos_ShipA.y += Velocity

def shipB_movement(keys_pressed, pos_ShipB):
    if keys_pressed[pygame.K_LEFT] and pos_ShipB.x -Velocity > BARRIER.x + BARRIER.width: #LEFT with "left arrow" key
            pos_ShipB.x -= Velocity
    if keys_pressed[pygame.K_RIGHT] and pos_ShipB.x + Velocity  + pos_ShipB.width < WIDTH: #Right with "right arrow" key
            pos_ShipB.x += Velocity
    if keys_pressed[pygame.K_UP] and pos_ShipB.y - Velocity > 0 : #UP with "up arrow" key
            pos_ShipB.y -= Velocity
    if keys_pressed[pygame.K_DOWN] and pos_ShipB.y + Velocity + pos_ShipB.height < HEIGHT: #DOWN with "down arrow" ley
            pos_ShipB.y += Velocity

#Handle bullet movement and collision
def handle_bullets(ShipA_bullets, ShipB_bullets, pos_ShipA, pos_ShipB):
      #ShipA bullets
      for bullet in ShipA_bullets: #iterate list of bullets
            bullet.x += BULLET_VEL # x position is adjusted by bullet velocity value
            #check collision
            if pos_ShipB.colliderect(bullet): #both obj must  be rects 
                  pygame.event.post(pygame.event.Event(shipB_hit)) #call user defined event "Hit" for collision
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
