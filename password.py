import random
import string

adjectives = ['sleepy', 'slow', 'creepy', 'hot', 'cold', 'big', 'red', 'orange',
              'yelollow', 'green', 'blue', 'good', 'old', 'white', 'free', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'cat', 'goat', 'dragon', 'car', 'duck',
         'panda']


print('Добро пожаловать')

while True:
    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)

        password = adjective + noun + str(number) + special_char
        print('Новый пароль: %s' % password)

    response = input('Сгенерировать другой пароль? Введите д или н: ')
    if response == 'н':
        break
