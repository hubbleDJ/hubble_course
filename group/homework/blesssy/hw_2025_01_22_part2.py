# 2. Создать dict со своими параметрами name, surname, hobby, age и все, что придумаете

dictUser: dict = {
    'name': input("Please enter your name: "),                
    'surname': input("Please enter your surname: "),         
    'age': input("Please enter your age: "),                  
    'gender': input("Please choose your gender (male/female): "),     
    'hobbies': input("Please enter at least two of your hobbies (using commas): ").split(', '),

}

print(f"Hi {dictUser['name']} {dictUser['surname']}, you are {dictUser['age']} y.o.'")
print(f"Your sex is {dictUser['gender']} and your hobbies are {', '.join(dictUser['hobbies'])}")
