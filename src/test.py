from argparse import ArgumentParser
import traceback
import time
import os

import crickroll
import pyrickroll
import interpreter

start = time.time()

if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-cpp", action="store_true")
    arg_parser.add_argument("-intpr", action="store_true")
    arg_parser.add_argument("--time", action="store_true")
    arg_parser.add_argument("file", nargs="?", default="")
    args = arg_parser.parse_args()

    parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    f_name = parent_path + "/examples/" + args.file
    print(f_name)
    if args.cpp:
        crickroll.run_in_cpp(f_name)
    elif args.intpr:
        interpreter.run_in_interpreter(f_name)
    else:
        try:
            pycode = pyrickroll.run_in_py(f_name)
            exec(pycode, globals(), globals())
        except Exception:
            error_msg = traceback.format_exc().split('File "<string>",')[-1]
            print(f'Python Exception in{error_msg}')


    if args.time:
        print(f'\nExecution Time: [{time.time() - start}] sec.\n')