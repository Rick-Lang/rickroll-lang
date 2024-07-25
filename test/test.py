#!/usr/bin/env python3
'''
This is a unit test.
It only tests the python transpiler running result of each example
'''

import path
import sys
import io
import unittest
 
# directory reach
directory = path.Path(__file__).absolute()

# setting path
sys.path.append(f'{directory.parent.parent}/src')

import pyrickroll

# Path of the example files
eg_dir = directory.parent.parent + '/examples/'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class TestRickrollPrograms(unittest.TestCase):

    expected_values = {'BubbleSort.rickroll': ('arr', [5, 6, 7, 9, 12]),
        'Counting.rickroll': ('idx', 100),
        'FindPrimes.rickroll': ('final_prime', 37),
        'HelloWorld.rickroll':\
            ('stdout', 'Never gonna give you up, never gonna let you down~'),
        'IfExample.rickroll': ('stdout', 'Man, never gonna give you up'),
        'WhileExample.rickroll': ('astleyCounter', 6),
        'LinearSearch.rickroll': ('stdout', '''Found in index 4\nFound in index 1\ngive up 0 :(''')
    }

    def test_all(self):
        cnt_total = 0
        cnt_pass = 0

        for key, value in self.expected_values.items():
            cnt_total += 1
            pycode = pyrickroll.run(eg_dir + key)
            loc = {}

            # Redirect stdout to capture the print output
            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout

            try:
                exec(pycode, globals(), loc)
                output = new_stdout.getvalue()
                sys.stdout = old_stdout

                if value[0] == 'stdout':
                    result = output.strip()
                    print(output)
                else:
                    result = loc.get(value[0])

                try:
                    self.assertEqual(value[1], result)
                    print(f"'{key}'{bcolors.OKGREEN} Testing passed!{bcolors.ENDC}")
                    cnt_pass += 1

                except AssertionError:
                    print(f"\n'{key}'{bcolors.FAIL} Testing Failed!{bcolors.ENDC}")
                    print(f"Found result: {result}. Expected {value[1]}\n")

            except Exception as e:
                sys.stdout = old_stdout
                print(f"\n'{key}' Testing Failed due to an exception: {e}\n")
                print(pycode)
            print('-'*70, '\n')

        print(f'\nUNIT TEST RESULT: {bcolors.OKBLUE}{cnt_pass}/{cnt_total}{bcolors.ENDC}')

if __name__ == '__main__':
    unittest.main()