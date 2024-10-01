def scope_alcanze():
    global var
    var = 0
    print(var)

def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def saludar(nombre='Mundo'):
    """
    -> Imprime un saludo con el nombre que se le pase como argumento.
    Keyword arguments:
        nombre: digito su nombre como string
    Return_deafault: 'Hola Mundo'
    """
    print(f'Hola {nombre}')


var = 1
saludar()
saludar('Brayan')
promedio = media(15, 18, 11)
print(f'{promedio:.2f}')

# se toma el valor que esta dentro de la función como prioridad
scope_alcanze()
var = 2
scope_alcanze()
print(var)