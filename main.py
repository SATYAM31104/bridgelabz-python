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

# UC2
noplay = 0
ladder = 1
snake = 2
win = 3

dice = play_map.get(random.randint(0,3),"No play")
if dice == noplay:
    print("No play")
if dice == ladder:
    print("Move up the ladder")
elif(dice == snake):
    print("Move down the snake")
elif(dice == win):
    print("Move")

# UC3
# UC3 & UC4
pos = 0
while (pos != 100):
    dice = random.randint(1, 6)
    options = random.randint(0, 3)
    noplay = 0
    ladder = 1
    snake = 2
    win = 3
    old_pos = pos

    if options == noplay:
        print("No play")
    elif options == ladder:
        print("Move up the ladder")
        pos += dice
    elif options == snake:
        print("Move down the snake")
        pos -= dice
    elif options == win:
        print("Move")
        pos += dice

    if pos > 100:
        pos = old_pos
        print("Stay in the same position")

    if pos < 0:
        pos = 0
        print("Restart from 0")