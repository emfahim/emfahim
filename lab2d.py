#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' name' + ' age')
    sys.exit()


else:
    Name = sys.argv[1]
    age = sys.argv[2]
    print('Hi ' + Name + ', you are ' + age + ' years old.')
