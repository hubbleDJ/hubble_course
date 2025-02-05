popList: list = [2, 4, 5, 4, 7, 2, 8, 4, 9, 2]
popLeight: int = len(popList)
print("sort start= ", popList)

for i in range(popLeight):
    for j in range(popLeight-1):
        if popList[j] > popList[j+1]:
           popList[j], popList[j+1] = popList[j+1], popList[j]
print("sort end= ", popList)