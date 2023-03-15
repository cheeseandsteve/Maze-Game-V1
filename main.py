# Imports
import turtle  # Imports turtle module
import math  # Imports math module
import random  # Imports the random module
import winsound  # Used to play sounds

# Game window attributes
wn = turtle.Screen()  # Creates the screen
wn.bgcolor("black")  # Background colour
wn.title("A Maze Game")  # Game title (Appears at top of window
wn.bgpic("Background.gif")  # Sets the background image
wn.setup(700, 700)  # Creates the screen size
wn.tracer(0)  # Turns off the animations for the turtle creating the board

# scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("skyblue")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-200, 307)
scoreboard.write("Player gold : 0", align="center", font=("Arial", 20, "bold"))

# Health bar
Health = turtle.Turtle()
Health.speed(0)
Health.color("skyblue")
Health.penup()
Health.hideturtle()
Health.goto(185, 307)
Health.write("Player Health : 50", align="center", font=("Arial", 20, "bold"))

# The key
key_collected = False

# Register shapes
turtle.register_shape("knight_right.gif")
turtle.register_shape("knight_left.gif")
turtle.register_shape("wall.gif")
turtle.register_shape("treasure.gif")
turtle.register_shape("monster_right.gif")
turtle.register_shape("monster_left.gif")
turtle.register_shape("Background.gif")
turtle.register_shape("key.gif")
turtle.register_shape("door.gif")


class paused(turtle.Turtle):
    def __init__(self):  # allows the class to initialise the attributes of a class
        turtle.Turtle.__init__(self)  # Initialising the turtle.Turtle class
        print("Paused")


# Create Pen attributes
class Pen(turtle.Turtle):
    def __init__(self):  # allows the class to initialise the attributes of a class
        turtle.Turtle.__init__(self)  # Initialising the turtle.Turtle class
        self.shape("square")  # Wall shape
        self.color("white")  # Wall colour
        self.penup()  # penup removes the pen drawn behind the turtle
        self.speed(0)  # Turns off animation and increases turtle speed to highest


# Create Player class
class Player(turtle.Turtle):
    def __init__(self):  # allows the class to initialise the attributes of a class
        turtle.Turtle.__init__(self)  # Initialising the turtle.Turtle class
        self.shape("knight_right.gif")  # Wall shape
        self.color("blue")  # Wall colour (unimportant as we are using gif)
        self.penup()  # penup removes the pen drawn behind the turtle
        self.speed(0)  # Turns off animation and increases turtle speed to highest
        self.gold = 0  # Player starts off with zero gold

    def go_up(self):
        # Calculate the spot the player wants to go to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        # check if that space the player wants to go is a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # Calculate the spot the player wants to go to
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        if (move_to_x, move_to_y) not in walls:  # check if that space the player wants to go is a wall
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Calculate the spot the player wants to go to
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        self.shape("knight_left.gif")

        if (move_to_x, move_to_y) not in walls:  # check if that space the player wants to go is a wall
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # Calculate the spot the player wants to go to
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        self.shape("knight_right.gif")

        if (move_to_x, move_to_y) not in walls:  # check if that space the player wants to go is a wall
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


# Class for the key
class Key(turtle.Turtle):
    def __init__(self, x, y):  # allows the class to initialise the attributes of a class
        turtle.Turtle.__init__(self)  # Initialising the turtle.Turtle class
        self.shape("key.gif")  # Wall shape
        self.color("gold")  # Wall colour (unimportant as we are using gif)
        self.penup()  # penup removes the pen drawn behind the turtle
        self.speed(0)  # Turns off animation and increases turtle speed to highest
        self.goto(x, y)  # go to this position

    def destroy(self):
        self.goto(2000, 2000)  # Sends treasure off-screen t give illusion its collected
        self.hideturtle()  # Hides the turtle so no trail shows it going to 2000, 2000


# Class for the door
class Door(turtle.Turtle):
    def __init__(self, x, y):  # allows the class to initialise the attributes of a class
        turtle.Turtle.__init__(self)  # Initialising the turtle.Turtle class
        self.shape("door.gif")  # Wall shape
        self.color("gold")  # Wall colour (unimportant as we are using gif)
        self.penup()  # penup removes the pen drawn behind the turtle
        self.speed(0)  # Turns off animation and increases turtle speed to highest
        self.goto(x, y)  # go to this position


# Class for the treasure
class Treasure(turtle.Turtle):
    def __init__(self, x, y):  # allows the class to initialise the attributes of a class
        turtle.Turtle.__init__(self)  # Initialising the turtle.Turtle class
        self.shape("treasure.gif")  # Wall shape
        self.color("gold")  # Wall colour (unimportant as we are using gif)
        self.penup()  # penup removes the pen drawn behind the turtle
        self.speed(0)  # Turns off animation and increases turtle speed to highest
        self.gold = 100  # when the gold is collected, the player gets 100 gold
        self.goto(x, y)  # go to this position

    def destroy(self):
        self.goto(2000, 2000)  # Sends treasure off-screen t give illusion its collected
        self.hideturtle()  # Hides the turtle so no trail shows it going to 2000, 2000


class Enemy(turtle.Turtle):
    def __init__(self, x, y):  # allows the class to initialise the attributes of a class
        turtle.Turtle.__init__(self)  # Initialising the turtle.Turtle class
        self.shape("monster_left.gif")  # Wall shape (unimportant as we are using gif)
        self.color("red")  # Wall colour
        self.penup()  # penup removes the pen drawn behind the turtle
        self.speed(0)  # Turns off animation and increases turtle speed to highest
        self.gold = 25  # when you kill the enemy you get 25 gold
        self.goto(x, y)  # go to this position
        self.direction = random.choice(["up", "down", "left", "right"])  # choose random direction from list

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24

        elif self.direction == "down":
            dx = 0
            dy = -24

        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("monster_left.gif")

        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("monster_right.gif")
        else:  # Unimportant but used incase something went wrong with enemy (they would just sit there)
            dx = 0
            dy = 0

        '''
        # Check if the player is close
        #   --> If so go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"
        '''
        # Calculate spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            # Choose a different direction
            self.direction = random.choice(["up", "down", "left", "right"])

        # Set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Create levels list
levels = [""]

# Define first level
#   -> X = Wall
#   -> P = Player
#   -> T = Treasure
#   -> E = Enemy
level_1 = (
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXXT         XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X   K   XX  XXXXXX  XXXXX",
    "X     D XX  XXXE      TXX",
    "XXXXXX  XX  XXXT       XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXXT XXXXX",
    "XXXXXX        X TXXXXXXXX",
    "X  XXX  XXXXXXX         X",
    "X    T    XXXXXXXX  TX  X",
    "X E              XXXXX  X",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX   T     X",
    "XXX      E              X",
    "XXXT        XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX  TXXXXX   E         TX",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX    XXXXXXXXXXXX  XXXXX",
    "XXT       T XXXXT       X",
    "XXXX    E              TX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
)

# Add a treasures list
treasures = []

# Add a enemies list
enemies = []

# Add a keys list
keys = []

# Add a doors list
doors = []

# Add maze to mazes list
levels.append(level_1)


# Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the character at each x, y coordinate
            # NOTE the order of y and x in the next lne
            character = level[y][x]
            # Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)  # Puts the square on the Xs
                pen.shape("wall.gif")  # Sets the wall to be the wall gif
                pen.stamp()  # leaves square in the position
                walls.append((screen_x, screen_y))  # Add wall coordinates to wall list

            # Check if it is an P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)  # Puts the player on the P

            # Check if it is an T (representing the treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))  # Puts the treasure on the T

            # Check if it is an E (representing enemies)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))  # Puts the Enemy on the E

            # Check if it is an K (representing a key)
            if character == "K":
                keys.append(Key(screen_x, screen_y))  # Puts the Key on the K

            # Check if it is an D (representing the door)
            if character == "D":
                doors.append(Door(screen_x, screen_y))  # Puts the door on the D


# Create class instances
pen = Pen()
player = Player()

# Create wall coordinate list
walls = []

# Set up the level
setup_maze(levels[1])

# Player Health
playerHealth = 50

# Key bindings
turtle.listen()  # Tells the turtle to read keypress
turtle.onkey(player.go_left, "Left")  # When left key is pressed do the go_left function
turtle.onkey(player.go_right, "Right")  # When right key is pressed do the go_right function
turtle.onkey(player.go_up, "Up")  # When up key is pressed do the go_up function
turtle.onkey(player.go_down, "Down")  # When down key is pressed do the go_down function
turtle.onkey(paused, "Escape")  # When escape key is pressed do the paused function

# Start moving the enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

# Main Game loop
while True:

    # Check for player collision with treasure
    # Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            # Add the treasure gold to the player gold
            player.gold += treasure.gold
            scoreboard.clear()
            scoreboard.goto(-200, 307)
            scoreboard.write("Player gold : {}".format(player.gold), align="center", font=("Arial", 20, "bold"))
            winsound.PlaySound("Coin.wav", winsound.SND_ASYNC)  # Play sound when hit gold
            print("Woah gold !")
            print("Player Gold : {}".format(player.gold))
            if player.gold == 1500:
                print("Congrats !")
                print("Collect the key and go to the door to finish !")
            else:
                pass

            # Destroy (hide) the treasure
            treasure.destroy()
            # Remove the treasure from the treasures list
            treasures.remove(treasure)

    # Check for player collision with the key
    # Iterate through key list
    for door in doors:
        if player.is_collision(door):
            if key_collected and playerHealth > 0 and player.gold == 1500:
                print("Level complete !")
                winsound.PlaySound("Finish.wav", winsound.SND_ASYNC)  # Play sound when finished
            else:
                pass

    # Check for player collision with the key
    # Iterate through key list
    for key in keys:
        if player.is_collision(key):
            # State key is collected
            key_collected = True
            print("Key Collected !")

            # Destroy (hide) the key
            key.destroy()
            # Remove the key from the keys list
            keys.remove(key)

    # Iterate through enemy list to see if the player collides with the enemy
    for enemy in enemies:
        if player.is_collision(enemy):
            winsound.PlaySound("Hitmarker.wav", winsound.SND_ASYNC)  # Play sound when hit
            playerHealth -= 1
            Health.clear()
            Health.goto(185, 307)
            Health.write("Player Health : {}".format(playerHealth), align="center", font=("Arial", 20, "bold"))
            print("Health remaining : ", playerHealth)
            if playerHealth < 0:
                winsound.PlaySound("Player Dying.wav", winsound.SND_ASYNC)  # Play sound when player dead
                print("He Dead")
            else:
                pass

    # Update the screen
    wn.update()
