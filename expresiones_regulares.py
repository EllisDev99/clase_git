"""
Breve clase sobre secuencias regulares

También conocidas como regex o patrones regulares, son secuencias de caracteres que 
definen patrones de búsqueda dentro de cadenas de texto.

¿Para qué sirven?
* Validación de datos: Verificar si una cadena de texto cumple con un formato expecífico
(ej: emails, números de teléfono, contraseñas)

* Extracción de información: Obtener partes específicas de una cadena.

* Reemplazo de texto: Sustituir partes de una cadena por otras.

* División de cadenas: Separar cadenas en subcadenas basadas en un patrón

En Python, utilizamos el módulo re para trabajar con expresiones regulares.
Este módulo proporciona funciones para compilar patrones, buscar coincidencias
y realizar reemplazos.
"""
import re

texto = "El gato está en el saco"
patron = "gato"

resultado = re.search(patron, texto) # re.search(): Esta función busca la primera ocurrencia del patrón en el texto.

if resultado: #Si re.search() encuentra una coincidencia, devuelve un objeto de coincidencia, de lo contrario devuelve None.
    print("Encontramos al gato!")

"""
Caracteres literales: Coinciden con ellos mismos (ej: 'a', '1', '$'). * **Metacaracteres:** Tienen un significado especial (ej: '.', '*', '+', '?', '^', '$')
Clases de caracteres: Representan conjuntos de caracteres (ej: [a-z], [0-9])
Cuantificadores: Indican cuántas veces puede repetirse un elemento (ej: *, +, ?, {n})

. (punto): Coincide con cualquier carácter excepto un salto de línea.
^: Coincide con el inicio de la cadena.
$: Coincide con el final de la cadena.
*: Coincide con cero o más repeticiones del elemento anterior.  
+: Coincide con una o más repeticiones del elemento anterior.
?: Coincide con cero o una repetición del elemento anterior.  
{n}: Coincide con exactamente n repeticiones del elemento anterior.  
[ ]: Define una clase de caracteres (ej: [a-z] para letras minúsculas).
"""

texto = "Mi número de teléfono es 0424-000-1111"
patron = r"\d{4}-\d{3}-\d{4}"  # r antes de la cadena para evitar problemas con las barras invertidas

resultado = re.search(patron, texto)

if resultado:
    print("Número de teléfono encontrado:", resultado.group())

"""
Este ejemplo busca un número de teléfono en formato 0000-000-0000. La r antes de la cadena
indica que es una cadena raw, evitando que Python interprete las barras invertidas 
como caracteres de escape.
"""