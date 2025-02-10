# Прекратить сортировку, если массив уже отсортирован
# Оптимизировать это в функцию
puz_meth: list = [12, 32, 0, -4, 4, 564564]

print(f'Исходные данные {puz_meth}')

def puzirk_m(puz: list[int|float]) -> None:
    """Сортирует список методом пузырька, не перепроверяя его лишний раз, если он уже отсортирован."""
    
    n: int = 0

    for i in range(len(puz_meth)):
        print(puz_meth)
        for j in range(len(puz_meth) - 1):
            if puz_meth[j] < puz_meth[j + 1]:
                n += 1
                if n == len(puz_meth):
                    exit(f'Итоговое значение: {puz_meth}')
            elif puz_meth[j] > puz_meth[j + 1]:
                n=0
                puz_meth[j], puz_meth[j + 1] = puz_meth[j + 1], puz_meth[j]

puzirk_m(puz_meth)
