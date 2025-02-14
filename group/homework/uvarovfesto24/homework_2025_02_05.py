def elmax (x):
    """Максимальное число в списке"""
    
    t = x[-1]
    for i in range(len(x)-1):
        if x[i]>=x[i+1] and x[i]>=t:
            t = x[i]
    return t
def elmin (x):
    """Минимальное число в списке"""

    t = x[-1]
    for i in range(len(x)-1):
        if x[i]<=x[i+1] and x[i]<=t:
            t = x[i]
    return t
def odd(x):
    """помещает чётные числа в новый список"""

    newList=x.copy()
    for i in range(len(x)):
            if x[i]%2==1 or x[i]==0:          #если 1 после %2, то нечётное.
                    newList.remove(x[i])
    return newList    
def popsort_list(x):
    """Сортирует числа по возрастанию"""

    bleight = len(x)
    stagn_f = True
    for i in range(bleight-1):
        stagn_f = False
        for j in range(bleight-i-1): 
            if x[j] > x[j+1]:
               x[j], x[j+1] = x[j+1], x[j] 
        if not stagn_f:
            break
    return x
popList = [-12,5,7,8,2,6,0,-2, 12,47, 5, 2,6,234, 65, 0, 32]
print("""
      максимальное число в списке= {} 
      минимальное число в списке= {}  
      список чётных чисел= {} 
      отсортированный список= {}
      """.format(elmax(popList),elmin(popList),odd(popList),popsort_list(popList)))