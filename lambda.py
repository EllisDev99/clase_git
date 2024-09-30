# funciones Lambda o anonímas
def retornar_nota(estudiante):
    return estudiante[1]

list_estudens = [('Edwar', 4.2),
                 ('Brayan', 5),
                 ('Maria', 3.1),
                 ('Carlos', 4.5)]

lista_num = [1, 2, 3, 4]

retorno = lambda x:x[1]

list_ordenada = sorted(list_estudens, key=lambda x:x[1]) # estudiante:estudiante[1]

print(list_ordenada)
print(retorno(lista_num)) #2

x = 5
y = 2
retorno2 = lambda x, y : x + y 
print(retorno2(x, y))