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
print(f'''Имя пользователя: {my_dict["name"]}, фамилия: {my_dict["secondname"]}, возраст: {my_dict["age"]}, увлечения: {my_dict["hobby"]}, город: {my_dict["city"]}''')