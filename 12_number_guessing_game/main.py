import game
playing = True

while playing:
    mode = int(input('chose dificulty: 1, 2, 3: '))

    game.play(mode)
    keepGoing = input('do you wish to continue?(y/n)').lower()
    if not (keepGoing == 'y'):
        playing = False
print('Thank you for playing!')

