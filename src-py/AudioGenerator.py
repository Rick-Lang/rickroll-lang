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

from Keywords import *

engine = init()

audio = {
    KW.PRINT.value: 'audios/print.wav',
    KW.LET.value: 'audios/let.wav',
    KW.MAIN.value: 'audios/main.wav',
    KW.IF.value: 'audios/if.wav',
    KW.END.value: 'audios/end.wav',
    KW.BREAK.value: 'audios/break.wav',
    KW.WHILE_LOOP.value:  'audios/whileloop.wav',
    KW.ENDLESS_LOOP.value: 'audios/loop.wav',
}

def play(token: str):
    au = audio.get(token)

    if au:
        play_wav(au)
    else:
        engine.say(token)
        engine.runAndWait()
