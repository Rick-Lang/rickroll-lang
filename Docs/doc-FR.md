# Documentation
"its not a rickroll! get into the car and the journey is gonna start in 3 secs"

# Notice:
**L'interface du RickRoll-Lang n'est pas le meme que Python**
1. Il n'as pas besoin d'indentation
2. Le code doit etre ecrit dans la methode principale, sinon le code ne marchera pas.

## Commandes pour executer votre code.
Executer en convertisant .rickroll a Python
```
python3 RickRoll.py [Nom du fichier source]
```
Executer en convertisant .rickroll a C++ (Un compilier g++ est obligatoire pour le bon fonctionnement (meme si cette fonction ne marche pas toujours) )
```
python3 RickRoll.py -cpp [Nom du fichier source]
```
Si vous voulez savoir le temps d'execution:
> Ajouter "--time"
```
python3 RickRoll.py [Nom du fichier source] --time
```
Généré et jouer un song depuis .rickroll (cette function est nouvelle)
```
python3 RickRoll.py [Nom du fichier source] --audio
```

## Hello World
```
take me to ur heart                                                    # Ceci est la METHODE PRINCIPAL
    give msg up "Never gonna give you up, never gonna let you down~\n" # Définie une variable
    i just wanna tell u how im feeling msg                             # Dit la variable "msg"
say goodbye                                                            # Fin de la methode principal
```
Et vous devez avoir ceci dans la console:
```
Never gonna give you up, never gonna let you down~
```

## Définire une Variable
Vous pouvez définir: int, float, string, list/array, set, and tuple.
```
give a up 10
give b up "C'est un texte"
give c up ["Ceci", "est", "une", "table"]

```

## Condition If
L'Indentation est optionel dans RickRoll-lang.
```
take me to ur heart~    # Vous pouvez ajouter "~" a la fin de l'expression (C'est optionel)
    give a up 10

    and if u ask me how im feeling a is 10
        i just wanna tell u how im feeling "A est 10!"
    say goodbye

say goodbye~
```
Equivalent dans python:
```python
if __name__ == '__main__':
    a = 10
    if a == 10:
        print("A est 10!")

```

Et vous devez avoir ceci dans la console
```
"A est 10!"
```

## Boucle
RickRoll a 2 types de boucle, le première est une boucle infinie, et la deuxième est une double "pendant"
```
take me to ur heart
    together forever and never to part # Boucle Infinie

    say goodbye

say_good_bye
```
Equivament en Python:
```Python
if __name__ == "__main__":
    while True:
        pass
```
Boucle "Pendant"
```
take me to ur heart
    give a up 10
    together forever with a is less than 10
        give a up a + 1
    say goodbye

say goodbye
```
Equivalent en Python:
```python
if __name__ == "__main__":
    a = 0
    while a < 10:
        a += 1

```

## Définire une function.
RickRoll supporte les function return.
```
gonna fait_quelquechose arg1, arg2 # Définie une function
    when i give my arg1, arg2 it will be completely # Retourne "arg1" et "arg2"
say goodbye
```
Equivalent en Python:
```python
def fait_quelquechose(arg1, arg2):
    return arg1, arg2
```

## Importer des fichier/lib
```
we know the LIB_NAME and we're gonna play it
```
Equivalent en Python:
```python
import LIB_NAME
```

### Python Intégrer
```
py: print("Bonjour Rick Astley")
py: import sys
```
Equivalent en Python:
```python
print("Bonjour Rick Astley")
import sys
```
