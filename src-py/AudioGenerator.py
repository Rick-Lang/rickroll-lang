pyttsxMissingBool=False
playsoundMissingBool=False
dependancyMissingBool=False
dependancyMissingCounter=0
try:
 from pyttsx3 import init
except:
 pyttsxMissingBool=True
 dependancyMissingBool=True
 dependancyMissingCounter+=1
try:
 from playsound import playsound as play_wav
except:
 playsoundMissingBool=True
 dependancyMissingBool=True
 dependancyMissingCounter+=1
if dependancyMissingBool==True:
 print(dependancyMissingCounter, " packages are missing. Would you like to install them or stop the script?(Y/N)")
 installChoice=input()
 if installChoice="Y":
  print("pip needed for this to work.")
  import os
  if pyttsxMissingBool==True:
   print("Installing the pip package pyttsx3...")
   os.system("pip install pyttsx3")
  if playsoundMissingBool=True:
   print("Installing the pip package playsound...")
   os.system("pip install playsound")
  try:
   from pyttsx3 import init
  except:
   print("Failed. Stopping :(")
   exit()
  try:
   from playsound import playsound as play_wav
  except:
   print("Failed. Stopping :(")
   exit()
 else:
  print("Stopping...")
  exit()
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
