# Program created by Brayan Vera.
# Date: 09/17/21

# Program name: Dodging_falling_bricks
import pygame
import sys
import random

# Creating constants
WIDTH = 800
HEIGHT = 600
red_color = (255,0,0)
black_color = (0,0,0)
blue_color = (0,0,255)

# Player position and size declaration
player_size = 50
player_pos = [WIDTH / 2, HEIGHT - player_size * 2] # WIDTH/2 makes sure the cube starts at the middle of the screen every time.

#Making enemies
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size),0] #Top make enemy random blocks appear on the top

#writing code to detect collision
def collision_detect(player_pos, enemy_pos):
    #storing x and y axis of my player and enemy.
    player_x = player_pos[0]
    player_y = player_pos[1]
    enemy_x = enemy_pos[0]
    enemy_y = enemy_pos[1]

    #Collision code. 
    #How it works is that if the enemy block dimension comes in contact with the players dimension, 
    # then collision oddurs, the program quits.
    # Collisions can happen from enemy block's botton and player's block top part, side to side from left or right.
    if (enemy_x >= player_x and enemy_x < (player_x + player_size)) \
        or (player_x >= enemy_x and player_x < (enemy_x + enemy_size)):
        if (enemy_y >= player_y and enemy_y < (player_y + player_size)) \
            or (player_y >= enemy_y and player_y < (enemy_y + enemy_size)):
            return True
    return False


#creating a window dimension
window = pygame.display.set_mode((WIDTH,HEIGHT)) #the tuple is the high and large of my window 

#to make sure the window remains open
# mapping all the events that happen in the windown/screen
#here identifying all the events that will happen in the screen
game_over = False
clock = pygame.time.Clock() #To reduce the speed of frames per second

while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        #Now we want to make the suare move
        #So we have to map the keyboard keys.
        #KEYDOWN: key, mod , unicode, scancode  <-Is found under events in pygame.org
        if event.type == pygame.KEYDOWN:
            #need to know the keys
            #need to store key coordinates of player
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x -= player_size
            if event.key == pygame.K_RIGHT:
                x += player_size
            #updating coordinates here
            player_pos[0] = x

    #Cleaning window. Leaving it to its origianl color after moving sqaure left or right.
    window.fill(black_color)

    #Giving drop movement of enemy. incrementing their Y to give the sense that is moving down
    #Checking if the enemy block is still on screen and moving it down.
    if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
        enemy_pos[1] += 20  #to move the enemy square down
    else:
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size) #to make it appear at random position.
        enemy_pos[1] = 0

    #Collisions
    if collision_detect(player_pos, enemy_pos):
        game_over = True #When true the program quits, meaning the player has lost.

    #Drawing enemies "squares in blue"
    pygame.draw.rect(window, blue_color, 
                    (enemy_pos[0],enemy_pos[1],
                    player_size,player_size))

    #Drawing player "a square"
    #declaring the color and the square size (position and size)
    pygame.draw.rect(window, red_color,
                    (player_pos[0],player_pos[1],
                    player_size,player_size))

    clock.tick(30) #clock tick/speed to 30 frames per second
    #To make it appear on the screen
    pygame.display.update()


