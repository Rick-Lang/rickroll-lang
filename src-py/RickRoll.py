from time import time
from sys import stdout
from traceback import format_exc
from argparse import ArgumentParser

start = time()      # Set and start a timer


def play_audio(src_file_name):
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
    arg_parser = ArgumentParser()
    arg_parser.add_argument("file")
    arg_parser.add_argument("-cpp", action="store_true")
    arg_parser.add_argument("-intpr", action="store_true")
    arg_parser.add_argument("--time", action="store_true")
    arg_parser.add_argument("--audio", action="store_true")
    args = arg_parser.parse_args()

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

    if args.audio:
        play_audio(args.file)

    if args.time:
        stdout.write(f'\nExecution Time: [{time() - start}] sec.\n')


if __name__ == "__main__":
    main()
