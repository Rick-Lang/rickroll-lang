from os.path import exists
from os import remove as delete_file
from pyttsx3 import init
import wave
import soundfile

au_print = wave.open("print.wav", "rb")
au_let = wave.open("let.wav", "rb")
au_main = wave.open("main.wav", "rb")
au_if = wave.open("if.wav", "rb")
au_end = wave.open("end.wav", "rb")
au_break = wave.open("break.wav", "rb")


engine = init()


class init:
    def __init__(self, audio_name):
        self.audio_name = audio_name
        self.audio_data = []


    def generate(self, word):

        if word == 'i_just_wanna_tell_u_how_im_feeling':
            self.audio_data.append([au_print.getparams(), au_print.readframes(au_print.getnframes())])

        elif word == 'give_u_up':
            self.audio_data.append([au_let.getparams(), au_let.readframes(au_let.getnframes())])

        elif word == 'take_me_to_ur_heart':
            self.audio_data.append([au_main.getparams(), au_main.readframes(au_main.getnframes())])

        elif word == 'and_if_u_ask_me_how_im_feeling':
            self.audio_data.append([au_if.getparams(), au_if.readframes(au_if.getnframes())])

        elif word == 'say_good_bye':
            self.audio_data.append([au_end.getparams(), au_end.readframes(au_end.getnframes())])

        elif word == 'desert_u':
            self.audio_data.append([au_break.getparams(), au_break.readframes(au_break.getnframes())])

        else:
            temp_path = "temp_audio.wav"

            engine.save_to_file(word, temp_path)
            engine.runAndWait()


            with wave.open(temp_path, "rb") as temp_audio:
                self.audio_data.append([temp_audio.getparams(), temp_audio.readframes(temp_audio.getnframes())])


            if exists(temp_path):
                delete_file(temp_path)


    def export(self):
        output = wave.open(self.audio_name, "wb")

        output.setparams(self.audio_data[0][0])

        for i in range(len(self.audio_data)):
            output.writeframes(self.audio_data[i][1])

        output.close()