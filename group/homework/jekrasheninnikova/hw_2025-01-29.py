puz_meth: list = [12, 32, 0, -4, 4, 564564]

print(f'Исходные данные {puz_meth}')

for i in range(len(puz_meth)):
    for j in range(len(puz_meth)-1):
        if puz_meth[j] > puz_meth[j + 1]:
            puz_meth[j], puz_meth[j + 1] = puz_meth[j + 1], puz_meth[j]
            print(puz_meth)