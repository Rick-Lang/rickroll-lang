# RickRoll 语言教程
一个面向诈骗，强动态，解释性的深奥编程语言

## 执行源码命令
> 用一般方法执行源代码：
```
python3 RickRoll.py -r [Source Code File Name]
```
> 将 .rickroll 翻译到 .cpp (C++): (需要G++编译器，而且此功能目前还不成熟，可能会出问题)
```
python3 RickRoll.py -r [Source Code File Name] --cpp
或
python3 RickRoll.py -r [Source Code File Name] --c++
```
> 如果客户想知道执行时间：
```
python3 RickRoll.py -r [Source Code File Name] --time
```
> 解释器也可以从你的源码中生成一个MP3文件（但此需求尚未完成）
```
python3 RickRoll.py -r [Source Code File Name] -audio [Audio_File_Name]
```
> 客户还可以通过唱歌的方式写代码 (但这个功能我们也没有完成)
```
python3 RickRoll.py -sing [MP3 File Name] [Source Code(Text) File Name]
```


## Hello World
```
take_me_to_ur_heart                           # 这是一个Main函数/方法
    give_u_up msg =  "你 被 骗 了 !"           # 定义一个变量
    i_just_wanna_tell_u_how_im_feeling msg    # 输出变量 “msg”
say_good_bye                                  # 结束Main函数/方法
```
客户的命令行会打印出：
```
你 被 骗 了 !
```

## 定义变量
```
give_u_up a = 10~
give_u_up b = "bbc is fn"
```

## If 语句
```
take_me_to_ur_heart~    # 你可以在语句后面加 “~”
    give_u_up a = 10

    and_if_u_ask_me_how_im_feeling a is 10
        i_just_wanna_tell_u_how_im_feeling "A is 10!"
    say_good_bye

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
take_me_to_ur_heart
    together_forever_we_two # 死循环

    say_good_bye

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
never_knew func arg1, arg2 could_feel_this_way  # 定义函数
    when_i_give_my arg1, arg2 it_will_be_completely # 返回arg1和arg2
say_good_bye
```
相当于以下Python代码
```python
def func(arg1, arg2):
    return arg1, arg2
```
