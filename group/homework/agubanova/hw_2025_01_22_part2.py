"""Homework 2025-01-22 part 2"""

my_dict: dict = {
    "name": "",
    "secondname": "",
    "age": "",
    "hobby": "",
    "city": "",
}

my_dict["name"] = input('Введите ваше имя: ')
my_dict["secondname"] = input('Введите вашу фамилию: ')
my_dict["age"] = input('Введите ваш возраст: ')
my_dict["hobby"] = input('Введите чем вы увлекаетесь: ')
my_dict["city"] = input('Введите город проживания: ')
print(
    f'''Имя пользователя: {my_dict["name"]}, '''
    f'''фамилия: {my_dict["secondname"]}, '''
    f'''возраст: {my_dict["age"]}, '''
    f'''увлечения: {my_dict["hobby"]}, '''
    f'''город: {my_dict["city"]}'''
)

