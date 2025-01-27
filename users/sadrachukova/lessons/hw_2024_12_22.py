if __name__ == '__main__':
    print('Hello, world!')
   

#
# Процессор
# ОЗУ(Оперативная память)


# int
var_int: int = 56
varInt: int = 52
print(var_int)
varTwoInt: int = varInt
varThreeInt: int = 16/8
print(var_int **2)
print(var_int //3)
print(var_int %3)
var_int = var_int + 1
var_int += 1
print(var_int)


# float
var_float: float = 89.7
varFloat: float = -89.7
print(int(var_float))
print(float("15"))

# bool
var_bool: bool = True
varBool: bool = False

# str
var_str: str = 'Hello, world!'
varStr: str = '1'
print('''"три" кавычки''')
print("""'три кавычки' другие""")
print("кавычки")
print("5" + "a")

x = 45
y = 50
print("x + y =" + str(x + y))
print("x + y ={}".format(x + y))
print(f"x + y ={x + y}")
print("text"[0])
print("text"[-2])
print("text"[2:])
print("text"[:3])
print(len("text"))

x: str = 'lol'
y: int = 34567
z: float = 567.7
o: str = '45'
hvsh: str = 'vlksjhvjk 67'
hvsh: str = "vlksjhvjk 67"


# list
var_list: list = [1, 2, 4, '56', 890, -176, False]
var_list_int: list[int] = [1, 3, 7]

# tuple
var_tuple: tuple = (1, 2, 4, '56', 890, -176, False)

# set
var_set: set = {1, 2, 4, '56', 890, -176, False}

# frozenset
var_frozenset: frozenset = frozenset({1, 2, 4, '56', 890, -176, False})

# dict
var_dict: dict = {
    'name': 'Maks',
    'age': 27,
    'male': 'M',
    'hobby': ['', '']
}

var_dict: dict[str, str] = {
    'name': 'Maks',
    'male': 'M'
}

var_none = None

print(type(var_set))