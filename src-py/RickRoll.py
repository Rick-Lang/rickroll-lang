from sys import argv, stdout
from time import time
from os.path import exists
from traceback2 import format_exc

from crickroll import run_in_cpp
from pyrickroll import run_in_py
# from AudioGenerator import init


# Help message
rick_help = """
Programming by writing code:   rickroll -s [File_Name]
Generate an audio: rickroll -r [File_Name] -audio [Audio_Name]
Sing code:  rickroll -sing [Audio_Name] [File_Name]

Other Options:
--time:      Show execution time ofyour code
--help/--h:  Help
"""

# Set and start a timer
start = time()

audio_engine = None

# def generate_audio(self, src_file_name):

#     with open(src_file_name, mode='r', encoding='utf-8') as src:
#         for statement in src.readlines():
#             obj = Token(statement)

#             for i in range(len(obj.t_types)):
#                 audio_engine.generate(obj.t_values[i])

def main():
    # is_audio = False
    is_help = False
    show_time = False
    is_cpp = False
    src_file_name = ''


    if len(argv) <= 1:
        exit(rick_help)

    for i in range(len(argv)):
        current_arg = argv[i].lower()

        # Run code. -r [file_name]
        if current_arg == '-r':
            src_file_name = argv[i + 1]

        # Generate audio. -audio [Output audio file name]
        # if current_arg == '-audio':
        #     global audio_engine
        #     is_audio = True

            # audio_engine = init(argv[i + 1])

        if current_arg == '--cpp' or current_arg == '--c++':
            is_cpp = True

        # Help message
        if current_arg == '--help' or current_arg == '--h':
            is_help = True

        # Show execution time
        if current_arg == '--time':
            show_time = True

    # Run the RickRoll program
    if src_file_name:
      if exists(src_file_name):
          if is_cpp: run_in_cpp(src_file_name)
          else:
            try: exec(run_in_py(src_file_name), locals(), globals())
            except:
              error = format_exc().split('File "<string>",')[-1]
              stdout.write(f'Exception in{error}\n' + '-------'*10)
              stdout.write('"'+"There ain't no mistaking, is true love we are making~"+'"')
      else: exit(f"File [{src_file_name}] doesn't exist...")
    else: stdout.write('Warning: [Not executing any script...]')


    # if is_audio:
        # self.generate_audio(src_file_name)
        # audio_engine.export()

    if is_help:
        stdout.write(rick_help)

    if show_time:
        stdout.write(f'\nExecution Time: [{time() - start}] sec.')


if __name__ == "__main__":
    main()
