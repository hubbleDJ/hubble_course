# Прекратить сортировку, если массив уже отсортирован
# Оптимизировать это в функцию
puz_meth: list = [12, 32, 0, -4, 4, 564564]

print(f'Исходные данные {puz_meth}')

def puzirk_m(puz: list[int|float]) -> None:
    """Сортирует список методом пузырька, 
    не перепроверяя его лишний раз, 
    если он уже отсортирован."""
    
    n: int = 0

    for i in range(len(puz)):
        print(puz)
        for j in range(len(puz) - 1):
            if puz[j] < puz[j + 1]:
                n += 1
                if n == len(puz):
                    exit(f'Итоговое значение: {puz}')
            elif puz[j] > puz[j + 1]:
                n=0
                puz[j], puz[j + 1] = puz[j + 1], puz[j]


puzirk_m(puz_meth)
