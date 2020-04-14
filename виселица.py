import random

lives = 9
words = ['пицца', 'петух', 'слоны', 'выдра', 'мираж', 'носки', 'ангел', 'песня']
secret_word = random.choice(words)
clue =list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print('Осталось жизней: ' + heart_symbol * lives)
    guess = input('Угадайте букву или слово целиком: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Неправильно. Вы теряете жизнь')
        lives = lives - 1

        if guessed_word_correctly:
            print('Победа! Было загадано ' + secret_word)
        else:
            print('Проигрыш! Было загадано слово ' + secret_word)
