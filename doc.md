# Language Documentation
A rick roll oriented, dynamic, strong, interpreting esoteric programming language.

# Notice:
**The syntax of RickRoll-Lang is not same as Python**
1. It doesn't need indentation
2. The code must be written inside the main method, otherwise the interpreter will not execute

## Commands to execute your code
> I usually execute my source code like this:
```
python3 RickRoll.py -r [Source Code File Name]
```
> If you want to know the execution time:
```
python3 RickRoll.py -r [Source Code File Name] --time
```

> If you want to translate RickRoll to C++: (Requires g++ compiler, however this feature is quite new, sometimes probably will not work)
```
python3 RickRoll.py -r [Source Code File Name] --cpp
OR
python3 RickRoll.py -r [Source Code File Name] --c++
```

> The interpreter can generate a .mp3 file from your source code (This feature is not completed yet)
```
python3 RickRoll.py -r [Source Code File Name] -audio [Audio_File_Name]
```
> Also the interpreter provides you to "sing" code (This feature is not completed yet)
```
python3 RickRoll.py -sing [MP3 File Name] [Source Code(Text) File Name]
```


## Hello World
```
take_me_to_ur_heart                                                      # This is the MAIN METHOD
    give_u_up msg = "Never gonna give you up, never gonna let you down~" # Define a variable
    i_just_wanna_tell_u_how_im_feeling msg                               # print the "msg" variable
say_good_bye                                                             # End the main method
```
And you can get the output on your terminal:
```
Never gonna give you up, never gonna let you down~
```

## Defining Variable
You can define int, float, string, list/array, set, and tuple.
```
give_u_up a = 10~
give_u_up b = "It is a string"
give_u_up c = ["This", "is", "an", "array"]

```

## If Statement
Indentation in RickRoll-lang is optional.
```
take_me_to_ur_heart~    # You can add "~" at the end of the statement (it is totally optional)
    give_u_up a = 10

    and_if_u_ask_me_how_im_feeling a is 10
        i_just_wanna_tell_u_how_im_feeling "A is 10!"
    say_good_bye

say_good_bye~
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
```
take_me_to_ur_heart
    together_forever_and_never_to_part # Endless loop

    say_good_bye

say_good_bye
```
Equivalent to Python:
```Python
if __name__ == "__main__":
    while True:
        pass
```

## Defining Function
RickRoll supports return function
```
never_knew func arg1, arg2 could_feel_this_way  # Define a function
    when_i_give_my arg1, arg2 it_will_be_completely # Return arg1 and arg2
say_good_bye
```
Equivalent to Python:
```python
def func(arg1, arg2):
    return arg1, arg2
```
