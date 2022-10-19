
<img src="https://avatars.githubusercontent.com/u/83736946?s=200&v=4" align="right" width="150" height="150"/>
<br>

# Lenguaje de Programación Rickroll
![Build](https://img.shields.io/badge/Build-passing-orange?style=for-the-badge&logo=appveyor)
![Python](https://img.shields.io/badge/Python-3.6%2B-brightgreen?style=for-the-badge&logo=appveyor)
![Licencia](https://img.shields.io/badge/License-MIT-red?style=for-the-badge&logo=appveyor)
<br>
Lenguaje de Programación Rick Roll, un lenguaje basado en rickroll!

![](https://repository-images.githubusercontent.com/367934588/4a27ae00-b73b-11eb-801b-36dd1756dc93)

## Hola Mundo
**Aunque Rickroll se puede transpilar a Python3, su sintaxis no es completamente similar a la de Python.**
1. No necesita sangría
2. El código debe escribirse dentro del método principal, de lo contrario, el intérprete no se ejecutará
3. **Las palabras clave se pueden separar libremente**

Rickroll-Lang:
```
take me to ur heart
    give msj up "Never gonna give you up, never gonna let you down~\n"
    i just wanna tell u how im feeling msj
say goodbye
```
Equivalente a Python
```python
if __name__ == '__main__':
  msj = "Never gonna give you up, never gonna let you down~\n"
  print(msj, end='')

```

Equivalente a C++
```c++
#include<iostream>
using namespace std;
int main(int argc, char* argv[]){
    string msj = "Never gonna give you up, never gonna let you down~\n";
    cout<<msj;
}
```
**Y puedes obtener la salida en tu terminal:**

<img src="https://camo.githubusercontent.com/e1e1abc53d498866b9a533d65cdfee7ac7cc289423dcbe3eead940051d93a275/68747470733a2f2f707265766965772e726564642e69742f77326e383169717833377035312e6769663f666f726d61743d706e673826733d61353631396661303039333863326161383137343936646464396563656461386137323733323463" width="460" height="460"/>

<br>

**Lo siento, es esto:**
```
Never gonna give you up, never gonna let you down~
```
**Las palabras clave se pueden separar libremente**
```
takemetourheart
    give msj up "Never gonna give you up, never gonna let you down~\n"
    i justwanna telluhowim feeling msj
say good bye
```
Esto también es ejecutable


## Ejecutar Código
Ejecutar convirtiendo .rickroll a Python
```shell
python3 RickRoll.py [Nombre del Archivo de Código Fuente]
```
Ejecutar convirtiendo .rickroll a C++ (Requiere compilador g++ y tiene numerosos bugs)
```shell
python3 RickRoll.py -cpp [Nombre del Archivo de Código Fuente]
```
Ejecutar con intérprete
```shell
python3 RickRoll.py -intpr [Nombre del Archivo de Código Fuente]
```
Si quieres saber el tiempo de ejecución:
> Añade "--time"
```shell
python3 RickRoll.py [Nombre del Archivo de Código Fuente] --time
```
Generate and play an audio from .rickroll
```shell
python3 RickRoll.py [Nombre del Archivo de Código Fuente] --audio
```

## Extensión de VsCode
https://marketplace.visualstudio.com/items?itemName=FusionSid.rickroll-lang


## Requisitos
- [Bibliotecas de Python](https://github.com/Rick-Lang/rickroll-lang/blob/main/requirements.txt)
- [Python 3.6+](https://www.python.org/downloads/release/python-3610/)
- G++ compiler (For translating RickRoll to C++)


## Características
- *[Turing-completo](https://en.wikipedia.org/wiki/Turing_completeness)*
- *Support [Python 3.6+](https://www.python.org/downloads/release/python-3610/)*
- *Keywords/statements are all comming from [Rick Astley's](https://en.wikipedia.org/wiki/Rick_Astley) lyrics*
- *Keywords can be separated freely*
- *[Examples](https://github.com/Rick-Lang/rickroll-lang/tree/main/examples) to get started*
- *Translate RickRoll source code to Python3 and C++*
- *[Generate and play audios from .rickroll source code](https://github.com/Rick-Lang/rickroll-lang#Generate-Audio)*
- *Chinese, Russian, and English documentation* (Hope you guys can pull request docs in other languages lol)
- [*An editor for writing .rickroll code*](https://github.com/RedEnder666/RickRoll_IDE)
- [*An Vscode extension*](https://marketplace.visualstudio.com/items?itemName=FusionSid.rickroll-lang)


## Generate Audio
Command:
```
python3 RickRoll.py [Nombre del Archivo de Código Fuente] --audio
```
After running this command, the generator is gonna generate an audio from the .rickroll program and play it on your terminal

![](https://github.com/Rick-Lang/rickroll-lang/blob/main/img/au_generator.PNG)

## Documentation
We don't usually update [The Chinese Documentation / 中文文档](doc-Ch.md)

**[English](doc.md)**
<br>
**[简体中文](doc-Ch.md)**
<br>
**[Russian](doc-RU.md)**

# Rickroll-lang Editor
See https://github.com/RedEnder666/RickRoll_IDE

# Todo!
In order to make RICKROll becoming a world heritage, YOU and I still have a bunch of things to do!
1. Add more keywords and built-in functions!
2. Write algorithms in RickRoll-Lang and upload them to [examples folder](examples).
3. Make syntax highlights for [VS Code](https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide) and [Sublime](https://www.sublimetext.com/docs/syntax.html)!
4. Improve the current audio generator!
5. Improve the RickRoll interpreter!
6. Support "writing code by singing"!
7. Design a better icon!
8. [**SPREAD RICKROLL EVERYWHERE!!!**](https://www.bilibili.com/video/BV1uT4y1P7CX)

# Rickroll Language Website
**[https://rickroll-lang.tech/introduction/](https://www.bilibili.com/video/BV1uT4y1P7CX)**
<br>
**_or_**
<br>
**https://rick-lang.github.io/rickroll-lang/**

# Offcial Discord Server/Contact
https://discord.gg/bRrbZPjVDH
Join this server to chat with cool people or for support
<br /> We currently need some people to join!

Wechat/微信: githubsherlockcxk
<br>
Discord: Satin Wuker#0572
<br/> Valcan#1407

# Purpose
Despite the fact that the Rickroll Language is considered an esoteric programming language, it has its unignorable significance. I believe that rick roll is not only a way to promote people’s communication, it is also one of the most paramount art in the human history. The purpose of the Rickroll Language is to introduce this art to people in a distinctive way – programming.

# Related Repos
Here are the projects that are inspired by Rickroll-lang
1. [Ricky](https://github.com/thevvx/Ricky)
2. [Rickroll-lang API](https://github.com/FusionSid/RicklangAPI)
3. [RickRoll IDE](https://github.com/RedEnder666/RickRoll_IDE)
4. [Rick Astley Bot](https://github.com/FusionSid/Rick-Astley-Bot)
5. [Rickroll Lang Vscode extension](https://github.com/FusionSid/Rickroll-Lang-VScode-Extension)

# Credit: Rick Astley
 Youtube: https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw
<br/> Twitter: https://twitter.com/rickastley
<br/> Facebook: https://www.facebook.com/RickAstley
<br/> Spotify: https://open.spotify.com/artist/0gxyHStUsqpMadRV0Di1Qt
