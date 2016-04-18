#Bring in string terms not always available, and operator for sorting dictionary
import string
import operator

#Build score of each letter, keep lowercase
letters = string.ascii_lowercase
numbers = range(1,27)
letter_score = dict(zip(letters,numbers))

"""
#This is what MP Made
def answer(name_list):
    names_dict = {}
    names = []
    for i in name_list:
        score=0
        for j in list(i):
            score+=letter_score[j]
        names_dict[i]=score
    name_sort = sorted(names_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    for k in name_sort:
        names.append(k[0])
    return names
"""

#This is based off of stack overflow
def answer(names):
	name_sort = sorted(names, key=value, reverse=True)
	return name_sort

input3=["annie", "bonnie", "liz", "bpnnid"]
answer(input3)