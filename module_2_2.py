first =  int(input('Введите первое число, '))
second =  int(input('Введите второе число, '))
third =  int(input('Введите третье число, '))
if first == second == third: # Проверяем равенство всех чисел, как самое маловероятное
    print(3)
elif first == second or second == third or third == first: # Проверяем равенство хотя бы 2-х чисел
    print(2)
else:
    print(0)