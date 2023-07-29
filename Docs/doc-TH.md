# เอกสารประกอบ
ไม่ใช่ RickRoll แฮะ งั้นมาเริ่มกันเลยดีกว่า

# คำเตือน:
**วากย์สัมพันธ์ของ RickRoll-Lang ไม่เหมือนกับไพทอนนะ**
1. ไม่ต้องมีการจัดเว้นวรรค
2. โค้ดต้องอยูู่ในคำสั้ง main, ไม่อย่างนั้นอินเทอร์พรีเตอร์จะไม่ทำงาน

## คำสั่งเพื่อที่จะสั่งงานโค้ด
สั่งโดยแปลง .rickroll ไปไพทอน
```
python3 RickRoll.py [Source Code File Name]
```
สั่งโดยแปลง .rickroll ไป C++ (ต้องมีคอมไพเลอร์ g++, แต่ฟีเจอร์นี้ยังไม่เสร็จนะ อาจจะไม่เวิร์คบ้าง)
```
python3 RickRoll.py -cpp [Source Code File Name]
```
ถ้าอยากรู้เวลาที่ใช้สั่ง:
> Add "--time"
```
python3 RickRoll.py [Source Code File Name] --time
```
สร้างและเล่นเสียงจาก .rickroll (ฟีเจอร์นี้ใหม่อยู่)
```
python3 RickRoll.py [Source Code File Name] --audio
```

## สวัสดีชาวโลก
```
take me to ur heart                                                    # นี้คือฟังก์ชั่น MAIN 
    give msg up "Never gonna give you up, never gonna let you down~\n" # กำหนดค่าตัวแปร
    i just wanna tell u how im feeling msg                             # แสดงผลตัวแปร "msg"
say goodbye                                                            # จบฟังก์ชั่น MAIN
```
และจะได้ผลลัพธ์นี้ออกมาในเทอร์มินัล:
```
Never gonna give you up, never gonna let you down~
```

## กำหนดตัวแปร
สามารถกำหนด int, float, string, list/array, set, และ tuple ได้

```
give a up 10
give b up "นี่่คือสตริง"
give c up ["และ", "นี่", "คือ", "อาเรย์"]
```

## คำสั่ง If
การเว้นวรรคนั้นไม่จำเป็น เว้นก็ได้ไม่เว้นก็ได้ แล้วแต่เลยพี่
```
take me to ur heart~    # เพิ่ม "~" หลังคำสั่งได้ (ไม่จำเป็น แต่น่ารักดีนะ)
    give a up 10

    and if u ask me how im feeling a is 10
        i just wanna tell u how im feeling "A is 10!"
    say goodbye

say goodbye~
```

เหมือนโค้ดนี้ในไพทอน:
```python
if __name__ == '__main__':
    a = 10
    if a == 10:
        print("A is 10!")

```

ในเทอร์มินัลจะได้ผลลัพธ์นี้ออกมา:
```
"A is 10!"
```

## ลูป
RickRoll มีลูป 2 แบบให้เลือก อันแรกคือลูปไม่มีที่สิ้นสุด อีกอัน while-loop
```
take me to ur heart
    together forever and never to part # Endless loop

    say goodbye

say_good_bye
```
เหมือนโค้ดนี้ในไพทอน:
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
เหมือนโค้ดนี้ในไพทอน:
```
if __name__ == "__main__":
    a = 0
    while a < 10:
        a += 1

```

## กำหนดฟังก์ชั่น
RickRoll มี return function
```
gonna do_something arg1, arg2 # กำหนดฟังก์ชั่น
    when i give my arg1, arg2 it will be completely # Return arg1 กับ arg2
say goodbye
```
เหมือนโค้ดนี้ในไพทอน:
```python
def do_something(arg1, arg2):
    return arg1, arg2
```

## นำเข้าไลบรารี่หรือไฟล์จากไพทอน
```
we know the ชื่อไลบรารี่ and we're gonna play it
```
เหมือนโค้ดนี้ในไพทอน:
```python
import ชื่อไลบรารี่
```

### ฝังโค้ดไพทอน
```
py: print("สวัสดีครับ ผมคือ ริค แอสท์ลีย์")
py: import sys
```
Equivalent to Python:
```python
print("สวัสดีครับ ผมคือ ริค แอสท์ลีย์")
import sys
```