def check_guess(guess, answer):
    global score
    if guess == answer:
        print('ответ верный')
        score = score + 1
score = 0
guess1 = input('Какой медведь живет за полярным кругом? ')
check_guess(guess1, 'белый медведь')
