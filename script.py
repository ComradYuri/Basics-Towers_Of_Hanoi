from stack import Stack

print("\n")
print('''        _|_              |                |
      _|_1_|_            |                |
    _|___2___|_          |                |
   |_____3_____|         |                |
 ________|_______________|________________|________
|____________Let's_play_Towers_of_Hanoi_!__________|

Objective: Move all disks from the left to the right stack!
Rules: 1. Each move the TOP disk is moved from on stack to another stack
       2. No disk may be placed on top of a smaller disk''')

# Create the Stacks

stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks += left_stack, middle_stack, right_stack

# Set up the Game
num_disks = int(input("How many disks do you want to play with? (normal = 4, difficult = 5)\nAnwser:"))
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

num_optimal_moves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {optimalmoves} moves".format(optimalmoves=num_optimal_moves))
# Get User Input


def get_input():
    # choices = [stack.get_name()[0] for stack in stacks] would do the same but in a list comprehension
    choices = []
    for stack in stacks:
        choices.append(stack.get_name()[0].lower())
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {0} for {1}".format(letter, name))
        user_input = input("")
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]
        else:
            print("That's the wrong button!. Try Again\n")


# Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
    print("..Current Stacks...")
    for stack in stacks:
        stack.print_items()
    while True:
        print("\nWhich stack do you want to move from?")
        from_stack = get_input()
        if from_stack.get_size() == 0:
            print("\nInvalid Move. Stack Is Empty. Try Again")
            break
#        elif from_stack.get_size() >= 1:
#            print("\nWhich stack do you want to move to?\n")
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nThe disk below is smaller! Invalid move! Try again!")
print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves,num_optimal_moves))



