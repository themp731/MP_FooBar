from math import factorial
from itertools import combinations

#Dynamic programming will allow us to remember options per iteration
#Needed guidance from https://github.com/rtheunissen
#Lack of knowledge of Stirling's numbers required help via GitHub

prev = {}

def results(pos, result, *args):
    if pos not in prev:
        prev[pos] = result(*args)
    return prev[pos]

def arrangements(rab, view):
    if view > rab:
        return 0
    elif view == rab:
        return 1
    elif view == 1:
        return factorial(rab-1)
    elif view == rab - 1:
        return combo(rab,2)
    else:
        pass
    return results((rab,view), lambda: arrangements(rab - 1, view - 1) + arrangements(rab - 1, view) * (rab - 1))

def combo(rab, view):
    combos = (factorial(rab) / (factorial(view) * factorial(rab - view)))
    return combos

def answer(x,y,n):
    return arrangements(n - 1, x + y - 2) * combo(x + y - 2, x - 1)