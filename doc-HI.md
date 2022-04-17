# RickRoll भाषा ट्यूटोरियल
घोटालों, मजबूत गतिशीलता, व्याख्या के लिए एक गूढ़ प्रोग्रामिंग भाषा

## स्रोत कमांड निष्पादित करें

> स्रोत कोड को सामान्य तरीके से निष्पादित करें：
```
python3 RickRoll.py [Source Code File Name]
```
> .rickroll अनुवाद करने के लिए .cpp (C++): (G++ कंपाइलर की आवश्यकता है, और यह सुविधा अपरिपक्व है और समस्याग्रस्त हो सकती है)
```
python3 RickRoll.py -cpp [Source Code File Name]
```
> यदि ग्राहक निष्पादन समय जानना चाहता है：
```
python3 RickRoll.py [Source Code File Name] --time
```
> RickRoll स्रोत कोड से एक ऑडियो उत्पन्न करें और चलाएं (लेकिन यह सुविधा परिपक्व नहीं है और गलत हो सकती है)
```
python3 RickRoll.py [Source Code File Name] --audio
```


## Hello World
```
take me to ur heart                           # यह एक मुख्य कार्य/विधि है
    give msg up "तुम मूर्ख थे !\n"                 # एक चर परिभाषित करें
    i just wanna tell u how im feeling msg    # आउटपुट चर "संदेश"
say_good_bye                                  # मुख्य कार्य / विधि समाप्त करें
```
क्लाइंट की कमांड लाइन प्रिंट हो जाएगी：
```
तुम मूर्ख थे!
```

## चर परिभाषित करें
```
give a up 10
give b up "It is a string"
give c up ["This", "is", "an", "array"]
```

## If बयान
```
take me to ur heart~    # You can add after the statement “~”

    give a up 10

    and if u ask me how im feeling a is 10
        i just wanna tell u how im feeling "A is 10!"
    say goodbye

say_good_bye~
```
निम्नलिखित पायथन कोड के बराबर
```python
if __name__ == '__main__':
    a = 10
    if a == 10:
        print("A is 10!")

```

क्लाइंट की कमांड लाइन प्रिंट हो जाएगी：
```
"A is 10!"
```

## Loop चक्र
```
take me to ur heart
    together forever and never to part # अनंत लूप

    say goodbye

say_good_bye
```
निम्नलिखित पायथन कोड के बराबर
```Python
if __name__ == "__main__":
    while True:
        pass
```

## Function समारोह
```
never knew func arg1, arg2 could feel this way  # फ़ंक्शन को परिभाषित करें
    when i give_my arg1, arg2 it will be completely # वापसी arg1 और arg2
say goodbye
```
निम्नलिखित पायथन कोड के बराबर
```python
def func(arg1, arg2):
    return arg1, arg2
```
