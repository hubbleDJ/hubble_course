#2. Создать dict со своими параметрами name, surname, hobby, age и все, что придумаете
    # Поля заполняете функцией input(Как тебя зовут? Сколько тебе лет, и т д)
    # По итогу должен получиться dict, из которого вы генерируете строку с приветствием (Привет {name}, любящий {hobby[0]} и т д)
    # Выводим строку в консоль
   
firstDictVar: dict = {}

print("Здравствуй путник, я расскажу тебе историю, но для начала познакомимся")
firstDictVar['name'] = input("Звать тя как? ")
firstDictVar['surname'] = input("А Фамилия твоя? ")
firstDictVar["where_from"] = input("откуда ж ты? ")
firstDictVar["time__now"] = input("Время не подскажишь? ")
firstDictVar['sleep'] = input("спишь/не спишь? ")

print(f'''   {firstDictVar['name']} {firstDictVar['surname']}  
    из города {firstDictVar["where_from"]}''', end="" 
    f''' был в состоянии {firstDictVar['sleep']} 
    до {firstDictVar["time__now"]} и решил вызвать ктулху,
    если вы это видите, значит у него всё получилось''')