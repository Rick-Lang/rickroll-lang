# Language Documentation
A rick roll oriented, dynamic, strong, interpreting esoteric programming language.

# Notice:
**The syntax of RickRoll-Lang is not same as Python**
1. It doesn't need indentation
2. The code must be written inside the main method, otherwise the interpreter will not execute
3. Every identifier (function or variable name) should contain more than one character

## Commands to execute your code
Execute by converting .rickroll to Python
```
python3 RickRoll.py [Source Code File Name]
```
Execute by converting .rickroll to C++ (Requires g++ compiler, however this feature is quite new, sometimes probably will not work)
```
python3 RickRoll.py -cpp [Source Code File Name]
```
If you want to know the execution time:
> Add "--time"
```
python3 RickRoll.py [Source Code File Name] --time
```
Generate and play an audio from .rickroll (This feature probably will fail becauese it is quite new)
```
python3 RickRoll.py [Source Code File Name] --audio
```

## Hello World
```
take me to ur heart                                                    # This is the MAIN METHOD
    give msg up "Never gonna give you up, never gonna let you down~\n" # Define a variable
    i just wanna tell u how im feeling msg                             # print the "msg" variable
say goodbye                                                            # End the main method
```
And you can get the output on your terminal:
```
Never gonna give you up, never gonna let you down~
```

## Defining Variable
You can define int, float, string, list/array, set, and tuple.
```
give a up 10
give b up "It is a string"
give c up ["This", "is", "an", "array"]

```

## If Statement
Indentation in RickRoll-lang is optional.
```
take me to ur heart~    # You can add "~" at the end of the statement (it is totally optional)
    give a up 10

    and if u ask me how im feeling a is 10
        i just wanna tell u how im feeling "A is 10!"
    say goodbye

say goodbye~
```
Equivalent to Python:
```python
if __name__ == '__main__':
    a = 10
    if a == 10:
        print("A is 10!")

```

And you will get this on your terminal
```
"A is 10!"
```

## Loop
RickRoll supports 2 kinds of loop, the first one is endless loop, and the second one is while loop
```
take me to ur heart
    together forever and never to part # Endless loop

    say goodbye

say_good_bye
```
Equivalent to Python:
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
Equivalent to python:
```
if __name__ == "__main__":
    a = 0
    while a < 10:
        a += 1

```

## Defining Function
RickRoll supports return function
```
gonna do_something arg1, arg2 # Define a function
    when i give my arg1, arg2 it will be completely # Return arg1 and arg2
say goodbye
```
Equivalent to Python:
```python
def do_something(arg1, arg2):
    return arg1, arg2
```
