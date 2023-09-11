#!/usr/bin/env python3
"""
This is a unit test.
It only tests the python transpiler running result of each example
"""

import path
import sys
 
# directory reach
directory = path.Path(__file__).abspath()

# setting path
sys.path.append(f'{directory.parent.parent}/src')

import PyRickroll

# Path of the example files
eg_dir = directory.parent.parent + '/examples/'

expected_values = {"BubbleSort.rickroll": ('arr', [5, 6, 7, 9, 12]),
                   "Counting.rickroll": ('idx', 100),
                   "FindPrimes.rickroll": ('final_prime', 37),
                   "HelloWorld.rickroll":\
                    ('msg', "Never gonna give you up, never gonna let you down~\n"),
}

def test_all():

    cnt_total = 0
    cnt_pass = 0

    for key, value in expected_values.items():
        cnt_total += 1
        pycode = PyRickroll.run(eg_dir + key)
        loc = {}
        exec(pycode, globals(), loc)

        try:
            assert value[1] == loc[value[0]]
            print(f'"{key}" Testing passed!')
            cnt_pass += 1

        except AssertionError:
            print(f'\n"{key}" Testing Failed!')
            print(f'Found result: {loc[value[0]]}. Expected {value[1]}\n')

    print(f"\nUNIT TEST RESULT: {cnt_pass}/{cnt_total}")


if __name__ == '__main__':
    test_all()