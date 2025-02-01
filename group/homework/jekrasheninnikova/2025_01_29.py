puzirek_method: list = [12, 32, 0, -4, 4, 564564]

print(f'Исходные данные: {puzirek_method}')

for i in range(len(puzirek_method)):
    for j in range (len(puzirek_method)-1):
        if puzirek_method[j]>puzirek_method[j + 1]:
            puzirek_method[j], puzirek_method[j + 1] = puzirek_method[j + 1], puzirek_method[j]
            print(puzirek_method)
