import readchar
import os
import random

POS_X = 0 #this is for the position in the list of my_position
POS_Y = 1 #this is for the position in the list of my_position


NUM_OF_MAP_OBJECTS = 11

obstacle_definition = '''\
#####  ######################
####                   ######
#####################  ######
###  ######  ########  ######
###  ######            ######
###########  ################
##           ################
##  #############          ##
##  #############  ######  ##
##                 ######  ##
#########################  ##
####               ######  ##
####  ###########          ##
####  #######################
####  #######################\
''' #the \ is to take care of the return button

my_position = [4,1]
tail_length = 0
map_objects = []
tail = []

end_game = False

#create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]#splits each string in different strings
#obstacle_definition[][]# row * height . to look if there is an obstacle in a position
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)
#print(map_objects)

while not end_game:
    os.system("clear")
    #DRAW MAP
    print("+" + "-" * MAP_WIDTH * 2 + "+")

    #GENERATE RANDOM OBJECTS IN THE MAP
    while len(map_objects) < NUM_OF_MAP_OBJECTS:

        new_position = [random.randint(0, MAP_WIDTH - 1),
                        random.randint(0, MAP_HEIGHT - 1)]  # generating random 2 values for a list

        if new_position not in map_objects and new_position != my_position and \
                obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":  # to make sure that the values are not in the list
            # also making sure that the positions of both are not in the same spot
            map_objects.append(new_position)

    for coordinate_y in range(MAP_HEIGHT): #when this coordinate_y = 1
        print("|", end = " ")
        for coordinate_x in range(MAP_WIDTH): #when this coordinate_x = 3   #ponerlo en blanco
            char_to_draw = "  "
            object_in_cell = None  #to erase every time it goes to the next loop
            tail_in_cell = None



            for map_obj in map_objects:  #to put object * in here where it belongs
                if map_obj[POS_X] == coordinate_x and map_obj[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_obj

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:#coordinate_x = 1-20, coordinate_y =1-15
                char_to_draw = " @"  #it overwrites here

                if object_in_cell: #to state where it is
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                if tail_in_cell:  #if tail_in_cell has something

                    end_game = True


            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"



            print("{}".format(char_to_draw), end = " ")
        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")
    print("Tamaño de la cola {}".format(tail_length))
    print("Posicion de la cola {}".format(tail))

    #Ask where he wants to move
    #direction = input("Donde te quieres mover? [WASD]: ")

    direction = readchar.readchar()

    new_position = None#To determine if you can move or not

    if direction == "w": #<---OK
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
        #tail.insert(0, my_position.copy()) #to insert a copy of a list
        #tail = tail[:tail_length] #to cut the tail

        #my_position = new_position
        ##my_position[POS_Y] -= 1

        ###if my_position[POS_Y] == -1:
        ###    my_position[POS_Y] += MAP_HEIGHT
        ##my_position[POS_Y] %= MAP_HEIGHT #updates to the same number if is btwn the boundaries of 15 in this case
        ###if number is not in btw 1 or 14 ex: -1%15 or 16%15 then it will be = 14 and 1
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
        #tail.insert(0, my_position.copy())
        #tail = tail[:tail_length]
        #my_position = new_position
        ##my_position[POS_Y] += 1

        ###if my_position[POS_Y] == MAP_HEIGHT:
        ###    my_position[POS_Y] -= MAP_HEIGHT
        ##my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":  #<---OK
        new_position = [(my_position[POS_X] - 1)% MAP_WIDTH, my_position[POS_Y]]
        #tail.insert(0, my_position.copy())
        #tail = tail[:tail_length]
        #my_position = new_position
        ##my_position[POS_X] -= 1

        ###if my_position[POS_X] == -1:
        ###    my_position[POS_X] += MAP_WIDTH
        ##my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1)% MAP_WIDTH, my_position[POS_Y]]
        #tail.insert(0, my_position.copy())
        #tail = tail[:tail_length]
        #my_position = new_position
        ##my_position[POS_X] += 1

        ###if my_position[POS_X] == MAP_WIDTH:
        ###    my_position[POS_X] -= MAP_WIDTH
        ##my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        end_game = True  #break breaks the loop and goes out

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())  # to insert a copy of a list
            tail = tail[:tail_length]  # to cut the tail
            my_position = new_position
if end_game == True:
    print("You died!")

