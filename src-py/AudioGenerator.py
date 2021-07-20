from pyttsx3 import init
from playsound import playsound as play_wav

from PublicVariables import *

engine = init()

au_print = 'print.wav'
au_let = 'let.wav'
au_main = 'main.wav'
au_if = 'if.wav'
au_end = 'end.wav'
au_break = 'break.wav'
au_loop = 'loop.wav'
au_while_loop = 'whileloop.wav'

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
