# Документация
Это не рикролл! Залезай в машину, приключение начинается через 3 секунды

# Важно:
**Синтаксис Rickroll-lang НЕ идентичен синтаксису Python**
1. Он не требует индентации (выделения табуляцией)
2. Код должен быть написан в главном методе, иначе его не запустит интерпретатор

## Комманды для запуска кода
Запуск, конвертируя .rickroll в Python
```
python3 RickRoll.py [Имя файла с кодом]
```
Запуск, конвертируя .rickroll в Python (Требует g++ compiler, эта функция ещё сырая, может не сработать)
```
python3 RickRoll.py -cpp [Имя файла с кодом]
```
Если хотите знать время запуска:
> Добавьте "--time"
```
python3 RickRoll.py [Имя файла с кодом] --time
```
Сгенерировать и запустить звук из .rickroll (This feature is quite new)
```
python3 RickRoll.py [Имя файла с кодом] --audio
```

## Здравствуй, мир
```
take me to ur heart                                                    # Объявление главного метода
    give msg up "Never gonna give you up, never gonna let you down~\n" # Объявление переменной
    i just wanna tell u how im feeling msg                             # Вывод переменной "msg" в консоль
say goodbye                                                            # Конец главного метода
```

И вы получите такой вывод в терминале:
```
Never gonna give you up, never gonna let you down~
```

## Объявление переменной
Вы можете объявить целочисленную переменную(int), строковую переменную(string), список/массив(list/array), множество(set), или кортеж(tuple).

```
give a up 10
give b up "It is a string"
give c up ["Это", "и", "есть", "массив"]
```

# Условия
Индентация в Rickroll-lang необязательна.
```
take me to ur heart~    # Вы можете добавить "~" в конце выражения (Это необязательно)
    give a up 10
    and if u ask me how im feeling a is 10
        i just wanna tell u how im feeling "A это 10!"
    say goodbye
say goodbye~
```
Эквивалент на Python:
```python
if __name__ == '__main__':
    a = 10
    if a == 10:
        print("A это 10!")

```

И вы получите вывод в терминале:
```
"A это 10!"
```

# Циклы
RickRoll поддерживает 2 вида циклов. Первый это бесконечный цикл, а второй это цикл с предусловием(while).
```
take me to ur heart
    together forever and never to part # Вечный цикл
    say goodbye
say_good_bye
```
Эквивалент на Python:
```Python
if __name__ == "__main__":
    while True:
        pass
```
Цикл с предусловием(while):
```
take me to ur heart
    give a up 10
    together forever with a is less than 10
        give a up a + 1
    say goodbye
say goodbye
```
Эквивалент на Python:
```
if __name__ == "__main__":
    a = 0
    while a < 10:
        a += 1
```
## Объявление функций
RickRoll поддерживает создание функций возврата(функций с return)
```
gonna do_something arg1, arg2 # Объявление функции
    when i give my arg1, arg2 it will be completely # Return arg1 and arg2
say goodbye
```
Эквивалент на Python:
```python
def do_something(arg1, arg2):
    return arg1, arg2
```

## Загрузка Python библиотек/файлов
```
we know the LIB_NAME and we're gonna play it
```
Эквивалент на Python:
```python
import LIB_NAME
```

### Встроенный Python код
```
py: print("hello Rick Astley")
py: import sys
```
Эквивалент на Python:
```python
print("hello Rick Astley")
import sys
```
