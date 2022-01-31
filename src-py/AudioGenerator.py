try:
 from pyttsx3 import init
except:
 print("pyttsx3 is missing. It's needed for Audio generation. Install package or stop?(Y/N)")
 installChoice=input()
 if installChoice=="Y":
  print("NOTE: pip needed for this to actually work.")
  import os
  os.system("pip install pyttsx3")
  try:
   from pyttsx3 import init
  except:
   print("Installation of pip package pyttsx3 failed :(")
   exit()
 else:
   print("stopping.")
   exit()
from playsound import playsound as play_wav

from PublicVariables import *

engine = init()

au_print = 'audios/print.wav'
au_let = 'audios/let.wav'
au_main = 'audios/main.wav'
au_if = 'audios/if.wav'
au_end = 'audios/end.wav'
au_break = 'audios/break.wav'
au_loop = 'audios/loop.wav'
au_while_loop = 'audios/whileloop.wav'

def play(token):
    if token == KW_print:
        play_wav(au_print)

    elif token == KW_let:
        play_wav(au_let)

    elif token == KW_main:
        play_wav(au_main)

    elif token == KW_if:
        play_wav(au_if)

    elif token == KW_end:
        play_wav(au_end)

    elif token == KW_break:
        play_wav(au_break)

    elif token == KW_while_loop:
        play_wav(au_while_loop)

    elif token == KW_endless_loop:
        play_wav(au_loop)

    else:
        engine.say(token)
        engine.runAndWait()
