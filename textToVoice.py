#!usr/bin/env python3

import os
import contextlib

#This function takes in a string and has espeak say it
def say(n):
    os.system("espeak '"+n+"'")
    print(chr(27) + "[2J")

say("Hello world jpeI am super cool")
