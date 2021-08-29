from time import time
start = time()

from sys import argv, stdout
from argparse import ArgumentParser


# Help message
rick_help = """
Programming by writing code:   rickroll -py [File_Name]
Generate an audio: rickroll -py [File_Name] -audio [Audio_Name]

Other Options:
--time:      Show execution time of your code
--help/--h:  Help
"""

# Set and start a timer


def play_audio(src_file_name):
    import AudioGenerator
    from pyrickroll import Token

    with open(src_file_name, mode='r', encoding='utf-8') as src:
        content = src.readlines()
        content[-1] += '\n'
        for statement in content:
            obj = Token(statement)

            while len(obj.v_types) != 0:
                AudioGenerator.play(obj.t_values[i])

def main():

    arg_parser = ArgumentParser()
    arg_parser.add_argument("file", nargs='?', default="")
    arg_parser.add_argument("-py", action = "store_true")
    arg_parser.add_argument("-cpp", action = "store_true")
    arg_parser.add_argument("-intpr", action = "store_true")
    arg_parser.add_argument("--time", action = "store_true")
    arg_parser.add_argument("--audio", action = "store_true")
    args = arg_parser.parse_args()

    src_file_name = args.file


    # Run the RickRoll program
    if args.file:
        from os.path import exists
        # Convert .rickroll to C++
        if args.cpp:
            from crickroll import run_in_cpp
            run_in_cpp(args.file)

        # Convert .rickroll to Python
        elif args.py:
            try:
                from pyrickroll import run_in_py
                exec(run_in_py(args.file), globals(), globals())
            except:
                from traceback2 import format_exc
                error_msg = format_exc().split('File "<string>",')[-1]
                stdout.write(f'Exception in{error_msg}')

        # Execute .rickroll using the interpreter
        elif args.intpr:
            from interpreter import run_in_interpreter
            run_in_interpreter(args.file)

    else: stdout.write('Warning: [Not executing any script...]')


    if args.audio:
        play_audio(args.file)

    if args.time:
        stdout.write(f'\nExecution Time: [{time() - start}] sec.\n')


if __name__ == "__main__":
    main()
