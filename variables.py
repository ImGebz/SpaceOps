#Created by Gabe Seale 
#assets and audio-ib Jace
#Adapted from TechWithTims' "Space Invaders" single player game
#https://youtu.be/Q-__8Xw9KTM


#Declare all GUI and game variables

import pygame #import pygame module
import os #import OS to load local files
pygame.font.init() #initialize font module
pygame.mixer.init() #initialize sound mixer

#GUI settings
pygame.display.set_caption("SpaceOps") #change gui window display name
WIDTH, HEIGHT = 900, 500 #width and height variables for surface(tuple)
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #create new window WIN with set dimensions

WHITE = (255,255,255) #variable contains the color white in rgb as a tuple
BLACK = (0,200,200) #color of middle barrier
NEON= (57,255,20) #bullet color 


BARRIER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT) #dimensions and position of middle barrier
                    #(left position, top position, width, height)
#load background image
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Images','BackGroundIMG.jpg')), (WIDTH, HEIGHT)) 

FPS = 60 #frames per second variable
Velocity = 6 #velocity value to control movement speed
BULLET_VEL = 15 #speed of projectiles
Max_Bullets = 4 #max bullets that can be on the screen at once for each ship

#Load sound effects from "mixer"
CollisionSound = pygame.mixer.Sound('Assets/Sounds/explosion.wav')
LaserSound = pygame.mixer.Sound('Assets/Sounds/laser.wav')

Ship_Width, Ship_Height = 90,70 #global width and height for ship obj


shipA_hit = pygame.USEREVENT + 1 #Define two new pygame events
shipB_hit = pygame.USEREVENT + 2 #each defines collision event for each ship

#font variables for health and winner text
HealthFont = pygame.font.SysFont('aldhabi', 40)
WinnerFont = pygame.font.SysFont('bahnschrift', 100)

#load ship A from file
Ship_A_IMG = pygame.image.load( #store image in _IMG variable
    os.path.join('Assets', 'Images', 'ShipA.png'))
Ship_A = pygame.transform.rotate(pygame.transform.scale(Ship_A_IMG, (Ship_Width,Ship_Height)), 90) #pass scaled ship image as arg for rotation function
#load ship B from files
Ship_B_IMG = pygame.image.load(
    os.path.join('Assets', 'Images','ShipB.png'))
Ship_B = pygame.transform.rotate(pygame.transform.scale(Ship_B_IMG, (Ship_Width,Ship_Height)), 90)

#Load image for WASD keys into _IMG variable
WASD_keysIMG = pygame.image.load(
      os.path.join('Assets', 'Images','WASDKeys.png'))
WASDkeys = pygame.transform.scale(WASD_keysIMG, (95,70)) #scale the image and store in obj variable

#load image for arrow keys into _IMG variable
Arrow_keysIMG = pygame.image.load(
      os.path.join('Assets', 'Images','ArrowKeysIMG.png'))
ARROWkeys = pygame.transform.scale(Arrow_keysIMG, (95,70)) #scale the image and store in obj var
