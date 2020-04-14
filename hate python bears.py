def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Ответ верный')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Ответ неверный. Попробуйте еще раз. ')
            attempt = attempt + 1
 
    if attempt == 3:
        print('Правильный ответ: ' + answer)
        
score = 0

print('Тест "Животные"')
guess1 = input('Какой медведь живет за полярным кругом?')
check_guess(guess1, 'белый')
guess2 = input('Какое сухопутное животное самое быстрое? ')
check_guess(guess2, 'гепард')
guess3 = input('Какое животное самое большое? ')
check_guess(guess3, 'кит')


print('Вы набрали очков: ' + str(score))

