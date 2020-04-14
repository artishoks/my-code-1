guess1 = int(input('Введите первое число '))
guess2 = int(input('Введите второе число '))

if guess1 > guess2:
  print(guess1, " Больше чем ", guess2)
elif guess1 < guess2:
  print(guess1, " Меньше чем ", guess2)
else:
  print(guess1, " Равно ", guess2)

