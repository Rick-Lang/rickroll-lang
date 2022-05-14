# Documentation
Se você ainda não é um rickroll! entre no carro e vamos iniciar nossa jornada em 3 segundos!

# Aviso:
**A sintaxe da linguagem RickRoll não é a mesma do Python**
1. Não precisa de identação
2. O Código precisa ser escrito dentro do método principal(Main), do contrário o interpretador não vai executar!

## Comandos para executar seu código
Executar convertendo o código fonte .rickroll para Python
```
python3 RickRoll.py #[Nome do arquivo de código fonte]
```
Executar convertendo .rickroll para C++ (Requer o compilador g++, no entanto, esse recurso é bastante novo, às vezes pode não funcionar como o esperado)
```
python3 RickRoll.py -cpp #[Nome do arquivo de código fonte]
```
Se você deseja visualizar o tempo de execução:
> Utilize o prefixo "--time"
```
python3 RickRoll.py #[Nome do arquivo de código fonte] --time
```
Gerar e reproduzir aúdio a partir do .rickroll (Esse recurso é novo)
>  Utilize o prefixo "--audio"
```
python3 RickRoll.py #[Nome do arquivo de código fonte] --audio
```

## Hello World(Olá Mundo) usando a Rickroll
```
take me to ur heart                                                    # Este é o MÉTODO PRINCIPAL
    give msg up "Never gonna give you up, never gonna let you down~\n" # Define uma variável
    i just wanna tell u how im feeling msg                             # Escreve o conteúdo da variável msg
say goodbye                                                            # Encerra o bloco do MÉTODO PRINCIPAL
```
Ao executar o trecho de código acima você tera o seguinte resultado em seu terminal:
```
Never gonna give you up, never gonna let you down~
```

## Definindo variáveis
Você pode definir os seguintes tipos primitivos da Rickroll int, float, string, list/array, set, e tuple.
```
give a up 10
give b up "It is a string"
give c up ["This", "is", "an", "array"]

```

## Estrutura condicional
Usar identação na RickRoll é totalmente opcional.
```
take me to ur heart~    # Você pode adicionar "~" ao fim da estrutura de decisão(Esse recurso é totalmente opcional)
    give a up 10

    and if u ask me how im feeling a is 10
        i just wanna tell u how im feeling "A is 10!"
    say goodbye

say goodbye~
```
O Trecho de código acima usando RickRoll é o equivalente ao seguinte trecho usando Python:
```python
if __name__ == '__main__':
    a = 10
    if a == 10:
        print("A is 10!")

```

A saída no seu terminal será a seguinte:
```
"A is 10!"
```

## Laços de Repetição(Loop)
RickRoll suporta 2 tipos de laços de repetição, o primeiro é loop infinito, e o segundo é o loop while.
```
take me to ur heart
    together forever and never to part # Endless loop

    say goodbye

say_good_bye
```
Equivalente em Python:
```Python
if __name__ == "__main__":
    while True:
        pass
```
While loop
```
take me to ur heart
    give a up 10
    together forever with a is less than 10
        give a up a + 1
    say goodbye

say goodbye
```
Equivalente em Python:

```Python
if __name__ == "__main__":
    a = 0
    while a < 10:
        a += 1

```

## Definindo uma função
RickRoll suporta retorno a partir de uma função
```
gonna do_something arg1, arg2 # Define a função
    when i give my arg1, arg2 it will be completely # Return arg1 e arg2
say goodbye
```
Equivalente tem Python:
```python
def do_something(arg1, arg2):
    return arg1, arg2
```

## Importando uma bibliotéca do Python/Arquivo
```
Nós conhecimentos a LIB_NAME então vamos executar
```
Equivalente em Python:
```python
import LIB_NAME
```

### Incorporando Código Python
```
py: print("hello Rick Astley")
py: import sys
```
Equivalente em Python:
```python
print("hello Rick Astley")
import sys
```
