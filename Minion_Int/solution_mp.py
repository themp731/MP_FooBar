#For each set, we know we can get the solution by using the
# "guarantee" function on last subject

#Length of time for each other is the time for each minion, times the 
#probability that the latter interrogations will be needed.

#Float division needs to imported for python v2
from __future__ import division

#Import item getter for sorting lists/tuples
from operator import itemgetter

def answer(minions):
    #Always try shortest time first, then so on based on the probability that the previous question was right.
    min_time = [(time/(numer/denom)) for time, numer, denom in minions]

    #id each time
    min_id = range(len(min_time))
    min_sort = zip(min_id,min_time)

    #sort the minions
    min_order = sorted(min_sort, key=itemgetter(1))
    
    #list of only the minion id number
    min_list = [i[0] for i in min_order]
    return min_list

print answer([[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]])