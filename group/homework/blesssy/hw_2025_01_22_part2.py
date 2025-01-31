# 2. Создать dict со своими параметрами name, surname, hobby, age и все, что придумаете
DictUser: dict = {
    'name': input ("Please enter your name: "),                #'Olessya',
    'surname': input ("Please enter your surname: "),          #'Bogdanova',
    'age': input ("Please enter your age: "),                  #19,
    'gender': input ("Please choose your gender (M/F): "),     #'W',
    'hobby': input ("Please enter at least two of your hobbies (using commas): ").split(', '),
                                                               #Liguistics, Languages, IT
}

print(f'Hi {DictUser['name']} {DictUser['surname']}, you are {DictUser['age']} y.o.')
print(f'Your sex is {DictUser['gender']} and your hobbies are {DictUser['hobby']}')
