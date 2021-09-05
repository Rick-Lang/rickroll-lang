# RickRoll 语言教程
一个面向诈骗，强动态，解释性的深奥编程语言

## 执行源码命令

> 用一般方法执行源代码：
```
python3 RickRoll.py -py [Source Code File Name]
```
> 将 .rickroll 翻译到 .cpp (C++): (需要G++编译器，而且此功能目前还不成熟，可能会出问题)
```
python3 RickRoll.py -cpp [Source Code File Name]
```
> 如果客户想知道执行时间：
```
python3 RickRoll.py -py [Source Code File Name] --time
```
> 从RickRoll源码中生成并播放一个音频（但此功能不算成熟，可能会出错）
```
python3 RickRoll.py -py [Source Code File Name] --audio
```
> 客户还可以通过唱歌的方式写代码 (但这个功能我们也没有完成)
```
python3 RickRoll.py -sing [MP3 File Name] [Source Code(Text) File Name]
```


## Hello World
```
take me to ur heart                           # 这是一个Main函数/方法
    give msg up "你 被 骗 了 !\n"              # 定义一个变量
    i just wanna tell u how im feeling msg    # 输出变量 “msg”
say_good_bye                                  # 结束Main函数/方法
```
客户的命令行会打印出：
```
你 被 骗 了 !
```

## 定义变量
```
give a up 10
give b up "It is a string"
give c up ["This", "is", "an", "array"]
```

## If 语句
```
take me to ur heart~    # 你可以在语句后面加 “~”

    give a up 10

    and if u ask me how im feeling a is 10
        i just wanna tell u how im feeling "A is 10!"
    say goodbye

say_good_bye~
```
相当于以下Python代码
```python
if __name__ == '__main__':
    a = 10
    if a == 10:
        print("A is 10!")

```

客户的命令行会打印出：
```
"A is 10!"
```

## Loop 循环
```
take me to ur heart
    together forever and never to part # 死循环

    say goodbye

say_good_bye
```
相当于以下Python代码
```Python
if __name__ == "__main__":
    while True:
        pass
```

## Function 函数
```
never knew func arg1, arg2 could feel this way  # 定义函数
    when i give_my arg1, arg2 it will be completely # 返回arg1和arg2
say goodbye
```
相当于以下Python代码
```python
def func(arg1, arg2):
    return arg1, arg2
```
