#!/usr/bin/env python3
from argparse import ArgumentParser
from sys import stdout
from time import time
from typing import Final
from traceback import format_exc

# Internal modules
import crickroll
import pyrickroll
import interpreter


def play_audio(src_file_name: str):
    import AudioGenerator
    from pyrickroll import Token
    from Lexer import lexicalize

    with open(src_file_name, mode='r', encoding='utf-8') as src:
        content = src.readlines()
        if len(content) > 0:
            content[-1] += '\n'
        for statement in content:
            tokens = lexicalize(statement)
            tok = Token(tokens)

            for v in tok.t_values:
                AudioGenerator.play(v)

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

def main():

    arg_parser = ArgumentParser()
    arg_parser.add_argument("file", nargs='?', default="")
    arg_parser.add_argument("-cpp", action="store_true")
    arg_parser.add_argument("-intpr", action="store_true")
    arg_parser.add_argument("--time", action="store_true")
    arg_parser.add_argument("--audio", action="store_true")
    arg_parser.add_argument("--debug", action="store_true")
    args = arg_parser.parse_args()

    start: Final = time()


    # No file
    if not args.file:
        stdout.write('Warning: [Not executing any script...]')
        return

    # Convert .rickroll to C++
    if args.cpp:
        crickroll.run(args.file)

    # Execute .rickroll using the interpreter
    elif args.intpr:
        interpreter.run(args.file, debug=args.debug)

    # Convert .rickroll to Python
    else:
        try:
            pycode = pyrickroll.run(args.file)
            if args.debug:
                print(pycode)
            exec(pycode, globals(), globals())
        except Exception:

            error_msg = format_exc().split('File "<string>",')[-1]
            stdout.write(f'Python Exception in{error_msg}\n')

            sp_pycode = pycode.split('\n')
            for i in range(len(sp_pycode)):
                stdout.write(f'{i + 1}: {sp_pycode[i]}\n')

    # Generate audio from source code
    if args.audio:
        play_audio(args.file)

    # Show time
    if args.time:
        stdout.write(f'\nExecution Time: [{time() - start}] sec.\n')


if __name__ == "__main__":
    main()
