#!/usr/bin/env python3


#"Author:"Esrak Fahim"
#"Author ID:"emfahim"
#"Date Created:"2021/09/24"

import sys

if len(sys.argv) == 1:
   timer = 3
   while timer > 0:
    print(timer)
    timer -=1
    print('blast off!')
    sys.exit()

if len(sys.argv) == 2:
   timer = int(sys.argv[1])
   while timer > 0:
       print(timer)
       timer -=1
   print('blast off!')
