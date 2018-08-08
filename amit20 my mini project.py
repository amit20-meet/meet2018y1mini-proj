import turtle
import random #We'll need this later in the lab


turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for snake1 in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+= SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stamp_l = snake.stamp()
    stamp_list.append(stamp_l)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
DOWN = 1
LEFT = 2
RIGHT = 3

direction = UP

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
   
    print("You pressed the up key!")
def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
    
    print("You pressed the dawn key!")
def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    
    print("You pressed the left key!")
def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up

    print("You pressed the right key!")

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, UP_ARROW)# Create listener for up key
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()


turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif") 
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
for this_food_pos in food_pos :
    food.goto(this_food_pos)
    stamp =food.stamp()
    food_stamps.append(stamp)

def make_food():
    global food_stamps
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    stamp = food.stamp() 
    food_stamps.append(stamp)

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==DOWN:
        snake.goto(x_pos , y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif direction==UP:
        snake.goto(x_pos , y_pos + SQUARE_SIZE)
        print("You moved up!")
        
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("you hit the down edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("you hit the up edge! Game over!")
        quit()


    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

        print("You have eaten the food!")

        if len(food_stamps) <= 6 :
            make_food()
    if snake.pos() in pos_list:
        quit()

        
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail


    
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()  

    

    
