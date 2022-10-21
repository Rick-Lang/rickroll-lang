#!/usr/bin/env python3
from traceback import format_exc

def play_audio(src_file_name: str):
    import AudioGenerator
    from pyrickroll import Token
    from Lexer import lexicalize

    with open(src_file_name, mode='r', encoding='utf-8') as src:
        content = src.readlines()
        content[-1] += '\n'
        for statement in content:
            tokens = lexicalize(statement)
            tok = Token(tokens)

            for i in range(len(tok.t_values)):
                AudioGenerator.play(tok.t_values[i])

def main():
    from argparse import ArgumentParser
    from sys import stdout
    from time import time


    arg_parser = ArgumentParser()
    arg_parser.add_argument("file", nargs='?', default="")
    arg_parser.add_argument("-cpp", action = "store_true")
    arg_parser.add_argument("-intpr", action = "store_true")
    arg_parser.add_argument("--time", action = "store_true")
    arg_parser.add_argument("--audio", action = "store_true")
    args = arg_parser.parse_args()

    # excludes `def`s, `import`s and `argparse` times
    start = time()
    # Run the RickRoll program
    if args.file:
        # Convert .rickroll to C++
        if args.cpp:
            from crickroll import run_in_cpp
            run_in_cpp(args.file)

        # Execute .rickroll using the interpreter
        elif args.intpr:
            from interpreter import run_in_interpreter
            run_in_interpreter(args.file)

        else:
            try:
                from pyrickroll import run_in_py
                exec(run_in_py(args.file), globals(), globals())
            except Exception:
                error_msg = format_exc().split('File "<string>",')[-1]
                stdout.write(f'Exception in{error_msg}')

    else:
        stdout.write('Warning: [Not executing any script...]')


    if args.audio:
        play_audio(args.file)

    if args.time:
        stdout.write(f'\nExecution Time: [{time() - start}] sec.\n')


if __name__ == "__main__":
    main()
