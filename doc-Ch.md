# 骗子语言教程
一个面向诈骗，强动态，解释性的深奥编程语言

## 执行源码命令
> 用一般方法执行源代码：
```
python3 rick.py -s [Source Code File Name]
```
> 如果客户想知道执行时间：
```
python3 rick.py -s [Source Code File Name] -time
```
> 解释器也可以从你的源码中生成一个MP3文件（但此需求尚未完成）
```
python3 rick.py -s [Source Code File Name] -mp3
```
> 客户还可以通过唱歌的方式写代码 (但这个功能我们也没有完成)
```
python3 rick.py -sing [MP3 File Name] [Source Code(Text) File Name]
```


## Hello World
```
take_me_to_ur_heart                           # 这是一个Main函数/方法
    give_u_up msg =  "你 被 骗 了 !"           # 定义一个变量
    i_just_wanna_tell_u_how_im_feeling: msg   # 输出变量 “msg”
never_let_me_go                               # 结束Main函数/方法
```
客户的命令行会打印出：
```
你 被 骗 了 !
```

## If 语句
```
take_me_to_ur_heart
    give_u_up a = 10

    and_if_u_ask_me_how_im_feeling a is 10
        i_just_wanna_tell_u_how_im_feeling: "A is 10!"
    say_good_bye

never_let_me_go
```
客户的命令行会打印出：
```
"A is 10!"
```
