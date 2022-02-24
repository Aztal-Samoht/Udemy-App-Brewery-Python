import random

playing = True

def game():
    goal = random.randint(1,100)
    print(goal)
    gamestate = do_guess(goal)
def do_guess(target):
    guess = int(input('pick an int!'))
    if guess == target:
        print('you win!')
        return True
    elif target > guess:
        print('too low')
    else:
        print('too high')
    return False

while playing:
    game()
    keepGoing = input('do you wish to continue?(y/n)').lower()
    if not (keepGoing == 'y'):
        playing = False
print('Thank you for playing!')

