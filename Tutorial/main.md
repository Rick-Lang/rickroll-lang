## Get Started
Using the VsCode syntax highlighter of the rickroll language can improve the efficiency of development *significantly*.

go to https://marketplace.visualstudio.com/items?itemName=FusionSid.rickroll-lang

or search up "rickroll language" on VsCode Extension
## Rickrol Quickstart
Let's create a file: `hello.rickroll` or `hellow.rr`

Open VsCode

**hello.rr**
```
take me to ur heart
    give msg up "Never gonna give you up, never gonna let you down~\n"
    i just wanna tell u how im feeling msg
say goodbye
```

The Rickroll transpiler translates the code into Python and C++.
<br>
The interpreter interprets the code and execute directly.
Python:
```python3
if __name__ == '__main__':
  msg = "Never gonna give you up, never gonna let you down~\n"
  print(msg, end='')
```
C++:
```cpp
#include<iostream>
using namespace std;
int main(int argc, char* argv[]){
    string msg = "Never gonna give you up, never gonna let you down~\n";
    cout<<msg;
}
```
Output:
```
give msg up "Never gonna give you up, never gonna let you down~
```
