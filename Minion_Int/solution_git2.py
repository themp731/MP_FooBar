# from operator import itemgetter

# def answer(minions):
# 	ratio_list = [(0.0 + minion[0])/((0.0 + minion[1])/minion[2])  for minion in minions]
# 	return [minion[0] for minion in sorted(list(enumerate(ratio_list)), key=itemgetter(1))]

#https://www.reddit.com/r/learnmath/comments/3oyedw/precalculus_probability_word_problems_and/?

class Minion:

    def __init__(self, minion, id):
        self.time = minion[0]
        self.numerator = minion[1]
        self.denominator = minion[2]
        self.id = id
        self.probability = (0.0 + self.numerator)/self.denominator
    def __repr__(self):
        return "%d: [%d, %d, %d]" % (self.id, self.time, self.numerator, self.denominator)

def getTime(minions):
    if len(minions) == 1:
        return minions[0].time

    first = minions[0]
    probability = (0.0 + first.numerator)/first.denominator

    time = probability*first.time + (1.0 - probability)*(first.time + getTime(minions[1:]))

    return time

def answer_recursive(minions, cache):
    if (len(minions) == 1):
        return [minions[0]]

    order = tuple([i.id for i in minions])
    if order in cache:
        return cache[order]

    optimal_order = []
    min_time = 0

    for i in range(0, len(minions)):
        current = minions[i]
        current_probability = (0.0 + current.numerator)/current.denominator
        this_time = current_probability*current.time

        others = minions[:i] + minions[(i + 1):]
        optimal_others = answer_recursive(others, cache)
        other_time = getTime(optimal_others)

        time = this_time + (1.0 - current_probability)*(current.time + other_time)

        if min_time == 0 or time < min_time:
            optimal_order = [minions[i]]
            for m in optimal_others:
                optimal_order.append(m)

            min_time = time

    cache[order] = optimal_order
    return optimal_order

def answer(minions):
    ms = []
    for i in range(0, len(minions)):
        m = minion.Minion(minions[i], i)
        ms.append(m)

    minion_order = answer_recursive(ms, {})
    return [i.id for i in minion_order]
Iterative N! solution

def answer(minions):

if len(minions) == 0:
    return []
# generate a convenience list of all the minions
ms = []
for i in range(0, len(minions)):
    m = Minion(minions[i], i)
    ms.append(m)

min_time = 1024.0*1024*1024
optimal_order = []

# for each permutation of the list calculate the 2nd order terms of the series
# Assuming that going out to 2nd-order should be enough
lis = [i for i in range(0,len(minions))]
permutations = [p for p in all_perms(lis)]
for permutation in permutations:
    time = 0.0

    # Calculate the 2nd-order term in the series
    for i in range(0,len(minions)-1):
        for j in range(i+1, len(minions)):
            time -= ms[permutation[i]].probability * ms[permutation[j]].time

    if time < min_time:
        optimal_order = permutation
        min_time = time

return optimal_order
    def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]