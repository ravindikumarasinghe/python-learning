#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    

if( 1 <= n <= 100):
    if(n % 2 == 0):
        if( 2 <= n <= 5 | n > 20):
            print("Not Weird")
        elif(6 <= n <= 20):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
else:
        print("Weird")