#Created by Gabe Seale 
#assets and audio-ib Jace
#Adapted from TechWithTims' "Space Invaders" single player game
#https://youtu.be/Q-__8Xw9KTM

#import functions file
from functions import *

#Main driver program
def main():
    clock = pygame.time.Clock() #clock variable
   
   #Ship position variables
    pos_ShipA = pygame.Rect(100, 300, Ship_Width, Ship_Height) #define variable for mapping the posistion for shipA
    pos_ShipB = pygame.Rect(700, 300, Ship_Width, Ship_Height)#define variable for mapping the posistion for shipB

    ShipA_bullets = [] #bullet list ship A 
    ShipB_bullets = [] #bullet list ship B
   
    health_A = 10 #health var for each ship
    health_B = 10
    
    #load background soundtrack form files
    pygame.mixer.music.load('Assets/Sounds/background.wav')
    pygame.mixer.music.play(1, 10) #play sound throughout execution and loop at given point

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
                        
       
            #ShipAhandle losing lives upon event
            if event.type == shipA_hit: #check for "hit" event
                  health_A -= 1 #if confirmed hit, shipA loses 1 life
                  CollisionSound.play() #collision sound effect
                
            #ShipB Handle losing lives
            if event.type == shipB_hit: #check for "hit"
                  health_B -= 1 #ShipB loses 1 life
                  CollisionSound.play() #collision sound effect 
        
        winner_txt = "" #empty string defined until there is a winner
        if health_A <= 0: #check for health value reaching 0
            winner_txt = "Blue ship wins!" #Winner message is outputed
        
        if health_B <=0: #check for health value
              winner_txt = "Red ship wins!" #output winner message

        if winner_txt != "": #display winner text
              winner(winner_txt)
              break #break so game restarts aftermessage delay
        
        keys_pressed = pygame.key.get_pressed() #get pressed function to return keys that are pressed(multiple)
        shipA_movement(keys_pressed, pos_ShipA) #function call to pass movement keys for ShipA to movement function
        shipB_movement(keys_pressed, pos_ShipB) #function call to pass movement keys for ShipB to movement function
        
        handle_bullets(ShipA_bullets, ShipB_bullets, pos_ShipA, pos_ShipB) #function call for bullets
        #function call
        draw_window(pos_ShipA, pos_ShipB, ShipA_bullets, ShipB_bullets,health_A,health_B) #arument objects are drawn to screen
        
    main()#start game again after a restart
    
if __name__ == "__main__":
    main() #execute main function
    