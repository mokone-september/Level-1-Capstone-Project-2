import pygame 
import random 


# This code is not a replica or verbatim copy of the code originally authored/coded by Atanu Sarkar The code
# in mention can be found on https://github.com/mratanusarkar/Space-Invaders-Pygame/blob/master/Space%20Invaders/main.py I will be adding him as a resource
# used to avoid any form of plagiarism because I did originally see and understood the task better after seeing his
# verson of the code.



# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# Title and Icon
game_caption = pygame.display.set_caption("Drone Space")
icon = pygame.image.load('drone(2).png')
pygame.display.set_icon(icon)

#Background
background = pygame.image.load('space.jpg')

# This creates all the spites  and gives it the image found in this folder (similarly with the enemy image). 

player = pygame.image.load("drone.png")
enemy1 = pygame.image.load("crate.png")
enemy2 = pygame.image.load("wood.png")
enemy3 = pygame.image.load("steel.png")
prize = pygame.image.load("diamond.png")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()

#Enemy 1
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
#Enemy 2
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
#Enemy 3
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
#Prize
prize_height = prize.get_height()
prize_width = prize.get_width()


print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later.
#Player
playerXPosition = 100
playerYPosition = 50

# Make the enemy and prize start off screen and at a random y position.
# Enemy 1
enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
# Enemy 2
enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
# Enemy 2
enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)
# Prize
prizeXPosition =  screen_width
prizeYPosition =  random.randint(0, screen_height - prize_height)



# This checks if the up, down, left and right key is pressed.

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
while 1: 

    screen.fill(0) # Clears the screen.
    screen.blit(background, (0, 0)) #Background Image Window
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition)) #Enemy 1
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition)) #Enemy 2
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition)) #Enemy 3
    screen.blit(prize, (prizeXPosition, prizeYPosition)) #Prize
    
     
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.


     # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP:
                print("PLAYER LOG: Up Arrow Key Pressed Down")
                keyUp = True
            if event.key == pygame.K_DOWN:
                print("PLAYER LOG: Down Arrow Key Pressed Down")
                keyDown = True
            if event.key == pygame.K_LEFT:
                print("PLAYER LOG: Left Arrow Key Pressed Down")
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                print("PLAYER LOG: Right Arrow Key Pressed Down")
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # Events are checked for in the for loop above and values are set:
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height: # This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerXPosition += 1
            
    # Check for collision of the enemy with the player.
    # To do this we will use bounding boxes around the images of the player and enemy.
    
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy 1:
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    # Bounding box for the enemy 2:
    
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    # Bounding box for the enemy 3:
    
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

     # Bounding box for the enemy 3:
    
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemy1Box):
    
        # Display losing status to the user: 
        
        print("----------------")
        print("GAME OVER !!")
        print("----------------")
        print("----------------")
        print("Try Again !!")
        print("----------------")

        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

        # Test collision of the boxes:
    
    if playerBox.colliderect(prizeBox):
    
        # Display losing status to the user: 
        
        print("----------------")
        print("GAME OVER !!")
        print("----------------")
        print("----------------")
        print("YOU WIN !!")
        print("----------------")

        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

        # Test collision of the boxes:
        
    if playerBox.colliderect(enemy2Box):
    
        # Display losing status to the user: 
        
        print("----------------")
        print("GAME OVER !!")
        print("----------------")
        print("----------------")
        print("Try Again !!")
        print("----------------")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
    
        # Display losing status to the user: 
        
        print("----------------")
        print("GAME OVER !!")
        print("----------------")
        print("----------------")
        print("Try Again !!")
        print("----------------")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
    
    if enemy1XPosition < 0 - enemy1_width:
    
        # Display wining status to the user: 
        
        print("----------------")
        print("GAME OVER !!")
        print("----------------")
        print("----------------")
        print("YOU WIN !!")
        print("----------------")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)

        # If the enemy is off the screen the user wins the game:
    
    if enemy2XPosition < 0 - enemy2_width:
    
        # Display wining status to the user: 
        
        print("----------------")
        print("GAME OVER !!")
        print("----------------")
        print("----------------")
        print("YOU WIN !!")
        print("----------------")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)

    if enemy2XPosition < 0 - enemy2_width:
    
        # Display wining status to the user: 
        
        print("----------------")
        print("GAME OVER !!")
        print("----------------")
        print("----------------")
        print("YOU WIN !!")
        print("----------------")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
        
    if prizeXPosition < 0 - prize_width:
    
        # Display wining status to the user: 
        
        print("----------------")
        print("GAME OVER !!")
        print("----------------")
        print("----------------")
        print("Try Again !!")
        print("----------------")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
 
    
    # Make enemy and prize approach the player.
    
    enemy1XPosition -= 0.4
    enemy2XPosition -= 0.5
    enemy3XPosition -= 0.6
    prizeXPosition -= 0.3
    
    # ================The game loop logic ends here. =============
  
