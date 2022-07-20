# توثيق
انها ليست rickroll! ركب السيارة وستبدأ الرحلة بعد 3 ثوانٍ

# يلاحظ:
**يختلف بناء جملة RickRoll-Lang عن Python**
1. لا يحتاج إلى مسافة بادئة
2. 2. يجب كتابة الكود داخل الطريقة الرئيسية ، وإلا فلن يقوم المترجم بالتنفيذ

## أوامر لتنفيذ التعليمات البرمجية الخاصة بك
نفذ بتحويل .rickroll إلى Python
```
python3 RickRoll.py [Source Code File Name]
```
نفذ عن طريق تحويل .rickroll إلى C ++ (يتطلب برنامج التحويل البرمجي g ++ ، ولكن هذه الميزة غير ناضجة تمامًا ، وربما لن تعمل في بعض الأحيان)
```
python3 RickRoll.py -cpp [Source Code File Name]
```
إذا كنت تريد معرفة وقت التنفيذ:
> إضافة "- time"
```
python3 RickRoll.py [Source Code File Name] --time
```
قم بإنشاء وتشغيل مقطع صوتي من .rickroll (هذه الميزة جديدة تمامًا)
```
python3 RickRoll.py [Source Code File Name] --audio
```

## مرحبا بالعالم
```
take me to ur heart                                                    # This is the MAIN METHOD
    give msg up "Never gonna give you up, never gonna let you down~\n" # Define a variable
    i just wanna tell u how im feeling msg                             # print the "msg" variable
say goodbye                                                            # End the main method
```
ويمكنك الحصول على الإخراج على جهازك:
```
Never gonna give you up, never gonna let you down~
```

## تحديد المتغير
يمكنك تحديد int و float و string و list / array و set و tuple.
```
give a up 10
give b up "It is a string"
give c up ["This", "is", "an", "array"]

```

## إذا البيان
المسافة البادئة في RickRoll-lang اختيارية.
```
take me to ur heart~    # You can add "~" at the end of the statement (it is totally optional)
    give a up 10

    and if u ask me how im feeling a is 10
        i just wanna tell u how im feeling "A is 10!"
    say goodbye

say goodbye~
```
ما يعادل Python:
```python
if __name__ == '__main__':
    a = 10
    if a == 10:
        print("A is 10!")

```

وستحصل على هذا في جهازك الطرفي
```
"A is 10!"
```

## عقدة
يدعم RickRoll نوعين من الحلقات ، الأول هو حلقة لا نهاية لها ، والثاني أثناء الحلقة
```
take me to ur heart
    together forever and never to part # Endless loop

    say goodbye

say_good_bye
```
ما يعادل Python:
```Python
if __name__ == "__main__":
    while True:
        pass
```
حائط اللوب
```
take me to ur heart
    give a up 10
    together forever with a is less than 10
        give a up a + 1
    say goodbye

say goodbye
```
ما يعادل بيثون:
```
if __name__ == "__main__":
    a = 0
    while a < 10:
        a += 1

```

## تحديد الوظيفة
يدعم RickRoll وظيفة الإرجاع
```
gonna do_something arg1, arg2 # Define a function
    when i give my arg1, arg2 it will be completely # Return arg1 and arg2
say goodbye
```
ما يعادل Python:
```python
def do_something(arg1, arg2):
    return arg1, arg2
```

## استيراد مكتبة / ملف Python
```
we know the LIB_NAME and we're gonna play it
```
ما يعادل Python:
```python
import LIB_NAME
```

### تضمين كود Python
```
py: print("hello Rick Astley")
py: import sys
```
ما يعادل Python:
```python
print("hello Rick Astley")
import sys
```