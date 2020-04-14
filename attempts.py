def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
             print('Ответ верный')
             score = score + 3 - attempt
             still_guessing = False
             
        else:
             
             if attempt < 2:
                guess = input('Ответ неверный. Попробуйте еще раз.')
             attempt = attempt + 1

    if attempt == 3:
        print('Правильный ответ: ' + answer)

score = 0 
guess = input('Мыши -  это млекопитающие. Да или нет? ')
check_guess(guess, 'Да')
