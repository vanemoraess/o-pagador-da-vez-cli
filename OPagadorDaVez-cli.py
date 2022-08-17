#The check is yours

quantity = 0
while True:
    try:
        quantity = int(input('Quantos amigos estão no bar hoje?'))
        if quantity > 0 and quantity <= 30:
            print(f'Muito bem, {quantity} participantes.')
            break
        else:
            raise ValueError('Somente valores de 1 a 30.')
    except ValueError as error:
        print(error)
    

import random

each_persons_name = []
for number in range(1, quantity + 1):
    persons_name = ""
    while(persons_name.strip() == ""):
        persons_name = input(f'Sorte ou azar? Digite o nome da pessoa {number}: ')
    
    each_persons_name.append(persons_name)


fee_paying = random.randint(1, quantity + 1)
print(f"Serão {fee_paying}  sugar friends")

randomly_selected = []
for number in range(0, fee_paying):
    while(True):
        index = random.randint(0, quantity - 1)
        person_list = each_persons_name[index]
        if(not person_list in randomly_selected):
            randomly_selected.append(person_list)

            break

print(f"Que azar. {randomly_selected}, vocês irão pagar!")




