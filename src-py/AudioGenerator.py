from gtts import gTTS
from playsound import playsound
from os.path import exists
from os import remove as delete_file


with open("print.wav", "rb") as f: au_print = f.read()
with open("let.wav", "rb") as f: au_let = f.read()
with open("main.wav", "rb") as f: au_main = f.read()
with open("if.wav", "rb") as f: au_if = f.read()
with open("end.wav", "rb") as f: au_end = f.read()
with open("break.wav", "rb") as f: au_break = f.read()


class init:
    def __init__(self, audio_name):
        self.audio_name = audio_name

        self.audio = open(self.audio_name, 'wb')


    def generate(self, word):

        if word == 'i_just_wanna_tell_u_how_im_feeling':
            self.audio.write(au_print)

        elif word == 'give_u_up':
            self.audio.write(au_let)

        elif word == 'take_me_to_ur_heart':
            self.audio.write(au_main)

        elif word == 'and_if_u_ask_me_how_im_feeling':
            self.audio.write(au_if)

        elif word == 'say_good_bye':
            self.audio.write(au_end)

        elif word == 'desert_u':
            self.audio.write(au_break)

        else:
            to_speak = gTTS(text=word, lang='en', slow=False)
            to_speak.save("temp_audio.wav")

            temp_audio = open("temp_audio.wav", "rb")

            audio_content = temp_audio.read()

            self.audio.write(audio_content)

            temp_audio.close()


            if exists("temp_audio.wav"):
                delete_file("temp_audio.wav")


    def export(self):
        self.audio.close()