#2. Создать dict со своими параметрами name, surname, hobby, age и все, что придумаете
    # Поля заполняете функцией input(Как тебя зовут? Сколько тебе лет, и т д)
    # По итогу должен получиться dict, из которого вы генерируете строку с приветствием (Привет {name}, любящий {hobby[0]} и т д)
    # Выводим строку в консоль
   
firstDictVar: dict = {
'name' : ' Konstantin',
'surname' : ' Uvarov',
"where'a you?" : " jvcr",
"what time is't now?" : " 6 am",
"ты спишь?" : " no sleep",
}
print("Здравствуй путник, я расскажу тебе историю, но для начала познакомимся")
firstDictVar['name']= input("Звать тя как? ")
firstDictVar['surname']= input("А Фамилия твоя? ")
firstDictVar["where'a you?"]= input("откуда ж ты? ")
firstDictVar["what time is't now?"]= input("Время не подскажишь? ")
firstDictVar['ты спишь?']= input("спишь/не спишь? ")

print(f''' {firstDictVar['name']} {firstDictVar['surname']} из города {firstDictVar["where'a you?"]}''', end="" 
f''' был в состоянии {firstDictVar['ты спишь?']} до {firstDictVar["what time is't now?"]} и решил вызвать ктулху, если вы это видите, значит у него всё получилось''')