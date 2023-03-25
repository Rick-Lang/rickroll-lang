# Documentación
no es un rickroll! súbete al auto y el viaje comenzará en 3 segs

# Aviso:
**La sintaxis de RickRoll-Lang no es la misma que la de Python**
1. No necesita sangría
2. El código debe escribirse dentro del método principal, de lo contrario, el intérprete no se ejecutará.

## Comandos para ejecutar tu código
Ejecutar convirtiendo .rickroll a Python
```
python3 RickRoll.py [Nombre del archivo de código fuente]
```
Ejecutar convirtiendo .rickroll a C++ (Requiere el compilador g++, sin embargo, esta característica es bastante inmadura, a veces probablemente no funcione)
```
python3 RickRoll.py -cpp [Nombre del archivo de código fuente]
```
Si quieres saber el tiempo de ejecución:
> Añade "--time"
```
python3 RickRoll.py [Nombre del archivo de código fuente] --time
```
Generar y reproducir un audio desde .rickroll (Esta característica es bastante nueva)
```
python3 RickRoll.py [Nombre del archivo de código fuente] --audio
```

## Hola Mundo
```
take me to ur heart                                                    # Este es el MÉTODO PRINCIPAL
    give msj up "Never gonna give you up, never gonna let you down~\n" # Definir una variable
    i just wanna tell u how im feeling msj                             # imprime la variable "msj"
say goodbye                                                            # Finalizar el método principal
```
Y puede obtener la salida en su terminal:
```
Never gonna give you up, never gonna let you down~
```

## Definiendo Variable
Puede definir int, float, string, list/array, set y tuple.
```
give a up 10
give b up "Es un string"
give c up ["Esto", "es", "un", "array"]

```

## Declaración If
La sangría en RickRoll-lang es opcional.
```
take me to ur heart~ # Puedes agregar "~" al final de la declaración (es totalmente opcional)
    give a up 10

    and if u ask me how im feeling a is 10
        i just wanna tell u how im feeling "¡A es 10!"
    say goodbye

say goodbye~
```
Equivalente a Python:
```python
if __name__ == '__main__':
    a = 10
    if a == 10:
        print("¡A es 10!")

```

Y obtendrás esto en tu terminal.
```
"¡A es 10!"
```

## Bucle
RickRoll admite 2 tipos de bucle, el primero es bucle sin fin y el segundo es bucle mientras
```
take me to ur heart
    together forever and never to part # Bucle sin fin

    say goodbye

say_good_bye
```
Equivalente a Python:
```Python
if __name__ == "__main__":
    while True:
        pass
```
Bucle mientras
```
take me to ur heart
    give a up 10
    together forever with a is less than 10
        give a up a + 1
    say goodbye

say goodbye
```
Equivalente a python:
```
if __name__ == "__main__":
    a = 0
    while a < 10:
        a += 1

```

## Definiendo Función
RickRoll admite función retorno
```
gonna hacer_algo arg1, arg2 # Definir una función
    when i give my arg1, arg2 it will be completely # Retornar arg1 y arg2
say goodbye
```
Equivalente a Python:
```python
def hacer_algo(arg1, arg2):
    return arg1, arg2
```

## Importar Archivo/Biblioteca de Python
```
we know the NOMBRE_BIB and we're gonna play it
```
Equivalente a Python:
```python
import NOMBRE_BIB
```

### Insertar código de Python
```
py: print("hola Rick Astley")
py: import sys
```
Equivalente a Python:
```python
print("hola Rick Astley")
import sys
```