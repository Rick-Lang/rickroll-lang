with open("let.mp3", 'rb') as f: let_audio = f.read()
with open("loop.mp3", 'rb') as f: loop_audio = f.read()
with open("print.mp3", 'rb') as f: print_audio = f.read()
with open("if.mp3", 'rb') as f: if_audio = f.read()
with open("end.mp3", 'rb') as f: end_audio = f.read()
with open("main.mp3", 'rb') as f: main_audio = f.read()



def generate(kw):
    with open("mp3.mp3", mode='ab') as f:
        if kw == 'i_just_wanna_tell_u_how_im_feeling:':
            f.write(print_audio)

        elif kw == 'give_u_up':
            f.write(let_audio)

        elif kw == 'take_me_to_ur_heart':
            f.write(main_audio)


generate()