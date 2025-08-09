# WIP (obviously)

import difflib

def match(arg1,arg2):
    x =  int(difflib.SequenceMatcher(None,arg1,arg2).quick_ratio() * 100)
    print(x)
    return x
