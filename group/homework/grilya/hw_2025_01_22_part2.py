#name = input('Напиши своё имя \n')
#surname = input('Напиши свою фамиилию или порча на понос \n')
#age = input('Напиши сколько тебе полных/худых лет \n')
#hobby = input('Чем ты любишь занимать больше всего? \n')
#balls: dict = {
#    'name': name,
#    'surname': surname,
#    'age': age,
#    'hobby': hobby
#}
#print(f'''Привет! Давай знакомиться {balls['name']} {balls['surname']}. \t
#Ахуеть тебе уже {balls['age']}, а ты всё ещё занимаешься такой хуйнёй как {balls['hobby']}, пока!''')


balls: dict = {
    'name': input('Напиши своё имя \n'),
    'surname': input('Напиши свою фамиилию или порча на понос \n'),
    'age': input('Напиши сколько тебе полных/худых лет \n'),
    'hobby': input('Чем ты любишь занимать больше всего? \n')
}
print(f'''Привет! Давай знакомиться {balls['name']} {balls['surname']}. \t
Ахуеть тебе уже {balls['age']}, а ты всё ещё занимаешься такой хуйнёй как {balls['hobby']}, пока!''')