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

# UC5 & UC6
pos = 0
roll = 0
noplay = 0
ladder = 1
snake = 2
win = 3

while (pos != 100):
    dice = random.randint(1, 6)
    options = random.randint(0, 3)
    old_pos = pos
    print("The dice number is", dice)
    print("The current position of the player is", pos)
    print("The option is", options)
    roll += 1

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

    print("The new position of the player is", pos)

print("The total Rolls taken to win", roll)


# uc6
pos1 = 0
pos2 = 0
roll1 = 0
roll2 = 0
noplay = 0
ladder = 1
snake = 2
win = 3
current_player = 1

while (pos1 != 100 and pos2 != 100):
    dice = random.randint(1, 6)
    options = random.randint(0, 3)

    if current_player == 1:
        old_pos = pos1
        print("Player 1 turn")
        print("The dice number is", dice)
        print("Player 1 current position is", pos1)
        print("The option is", options)
        roll1 += 1

        if options == noplay:
            print("No play")
        elif options == ladder:
            print("Move up the ladder")
            pos1 += dice
        elif options == snake:
            print("Move down the snake")
            pos1 -= dice
        else:
            print("Move")
            pos1 += dice

        if pos1 > 100:
            pos1 = old_pos
            print("Stay in the same position")

        if pos1 < 0:
            pos1 = 0
            print("Restart from 0")

        print("Player 1 new position is", pos1)
        current_player = 2
    else:
        old_pos = pos2
        print("Player 2 turn")
        print("The dice number is", dice)
        print("Player 2 current position is", pos2)
        print("The option is", options)
        roll2 += 1

        if options == noplay:
            print("No play")
        elif options == ladder:
            print("Move up the ladder")
            pos2 += dice
        elif options == snake:
            print("Move down the snake")
            pos2 -= dice
        elif options == win:
            print("Move")
            pos2 += dice

        if pos2 > 100:
            pos2 = old_pos
            print("Stay in the same position")

        if pos2 < 0:
            pos2 = 0
            print("Restart from 0")

        print("Player 2 new position is", pos2)
        current_player = 1

if pos1 == 100:
    print("Player 1 wins")
    print("Player 1 total rolls", roll1)
    print("Player 2 total rolls", roll2)
else:
    print("Player 2 wins")
    print("Player 1 total rolls", roll1)
    print("Player 2 total rolls", roll2)