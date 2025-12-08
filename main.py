import random

# UC1
position = 0
dice = random.randint(1,6)
position += dice
print("The player moves by",position,"The number on the dice is",dice)

play_map = {
    0: "No play",
    1: "Move up the ladder",
    2: "Move down the snake",
    3: "Move"}

move_map = {
    1:"Snake",
    2:"Ladder",
    3:"Move"
}