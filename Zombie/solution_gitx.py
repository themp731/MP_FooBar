#https://github.com/markholland/foobar/blob/master/zombit_antidote/zombitAntidote.py
import operator
def answer(meetings):
    smeetings = sorted(meetings, key=operator.itemgetter(1))
    accepted = []
    for m in smeetings:
        noroom = False
        for a in accepted:
            if m[0] < a[1] and m[1] > a[0]:
                    noroom = True
            elif m[1] > a[0] and m[0] < a[1]:
                    noroom = True
        if not noroom:
            accepted.append(m)
    return len(accepted)

print answer([[0, 1], [1, 2], [2, 3], [3,6], [3, 5], [4, 5]])
print answer([[0, 1000000], [42, 43], [0, 1000000], [42, 43]])