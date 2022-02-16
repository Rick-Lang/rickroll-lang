pyttsxMissingBool = False
playsoundMissingBool = False
dependancyMissingBool = False
dependancyMissingCounter = 0

try:
    from pyttsx3 import init
except:
    pyttsxMissingBool = True
    dependancyMissingBool = True
    dependancyMissingCounter += 1

try:
    from playsound import playsound as play_wav
except:
    playsoundMissingBool=True
    dependancyMissingBool=True
    dependancyMissingCounter+=1

if dependancyMissingBool:
    print(dependancyMissingCounter, " packages are missing. Would you like to install them or stop the script?(Y/N)")
    installChoice=input().upper()
    if installChoice=="Y":
        print("pip needed for this to work.")
        import os
        if pyttsxMissingBool:
            print("Installing the pip package pyttsx3...")
            os.system("pip install pyttsx3")
        if playsoundMissingBool:
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

audio = {
    KW_print: 'audios/print.wav',
    KW_let: 'audios/let.wav',
    KW_main: 'audios/main.wav',
    KW_if: 'audios/if.wav',
    KW_end: 'audios/end.wav',
    KW_break: 'audios/break.wav',
    KW_while_loop:  'audios/whileloop.wav',
    KW_endless_loop: 'audios/loop.wav',
}

def play(token):
    au = audio.get(token)

    if au:
        play_wav(au)
    else:
        engine.say(token)
        engine.runAndWait()
