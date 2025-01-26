# Нужно заполнить тела функций, согласно комментариев, внутри функции
# Комментарии не менять и не удалять

def maxNumList(numbers: list[int]) -> int:
    """
        Находит максимальное значение в списке
        Использовать функцию max нельзя

        Пример: maxNumList([0, -1, 19999, -80898, 898]) вернет 19999
    """
    '''maxNum = None
    return maxNum'''
    if not numbers:
        return None

    maxNum = numbers[0]
    for element in numbers:
        if element > maxNum:
            maxNum = element
    return maxNum

result = maxNumList([0, -1, 19999, -80898, 898])
print(result)

def minNumList(numbers: list[int]) -> int:
    """
        Находит минимальное значение в списке
        Использовать функцию min нельзя

        Пример: minNumList([0, -1, 19999, -80898, 898]) вернет -80898
    """

    '''minNum = None
    return minNum'''
    if not numbers:
        return None

    minNum = numbers[0]
    for element in numbers:
        if element < minNum:
            minNum = element
    return minNum

result = minNumList([0, -1, 19999, -80898, 898])
print(result)

def sumNumbersInList(numbers: list[int]) -> int:
    """
        Находит сумму значений в списке
        Использовать функцию sum нельзя

        Пример: sumNumbersInList([0, -1, 19999, -80898, 898]) вернет -60002
    """

    '''sumNum = None
    return sumNum'''

    sumNum = 0
    for element in numbers:
        sumNum += element
    return sumNum

result = sumNumbersInList([0, -1, 19999, -80898, 898])
print(result)

def getChetNumsInList(numbers: list[int]) -> list[int]:
    """
        Возвращает все четные числа в списке

        Пример: getChetNumsInList([0, -1, 19999, -80898, 898]) вернет [-80898, 898]
    """

    """chetNums = []
    return chetNums"""

    chetNums =[]
    for element in numbers:
        if element % 2 == 0:
                chetNums.append(element)
    return chetNums

result = getChetNumsInList([0, -1, 19999, -80898, 898])
print(result)

def getCountNumsMoreNum(numbers: list[int], num: int) -> int:
    """
        Возвращает количество чисел в списке, которые больше, чем num

        Пример: getCountNumsMoreNum([0, -1, 19999, -80898, 898], 19) вернет 2
    """

    """countNumsMoreNum = 0
    return countNumsMoreNum"""

    countNumsMoreNum = 0
    for element in numbers:
        if element > num:
            countNumsMoreNum += 1
    return countNumsMoreNum

result = getCountNumsMoreNum([0, -1, 19999, -80898, 898], 19)
print(result)

