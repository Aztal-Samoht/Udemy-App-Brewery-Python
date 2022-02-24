import random
print('imported game')
def play(dificulty):
    guesses = dificulty ** 2
    goal = random.randint(1,100)
    #print(goal)
    gamestate = False
    while guesses > 0 and not gamestate:
        gamestate = do_guess(goal)
        guesses -= 1
        print(str(guesses) + ' guesses remain')
    if gamestate:
        print('you win!')
    else:
        print('you lose :(\nthe answer was: ' + str(goal))

def do_guess(target):
    guess = int(input('pick an int '))

    if guess == target:
        print('you win!')
        return True
    elif target > guess:
        print('too low')
    else:
        print('too high')
    return False
