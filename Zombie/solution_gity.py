#http://code.runnable.com/VRd17CSTemlZ89ya/unweighted-activity-selection-problem-for-python-google-foobar-and-googlefoobar
from operator import itemgetter
import random

def answer(meetings):
    meetings = sorted(meetings, key=itemgetter(1))
    solutions = [[meetings[0]]]
    max_meetings = 1
    for i in xrange(1, len(meetings)):
    	for solution in solutions:
    		if meetings[i][0] >= solution[-1][1]:
    			solution.append(meetings[i])
    			if len(solution) > max_meetings:
    				max_meetings = len(solution)
    	solutions.append([meetings[i]])
    return max_meetings

if __name__ == '__main__':
    for i in xrange(0, 10):
        
        meetings_length = random.randint(5, 10)
        a = random.randint(1, 49)
        b = random.randint(a+1, 50)
        meeting = [a, b]
        meetings = [meeting]

        for i in xrange(1, meetings_length):
    	      a = random.randint(1, 49)
    	      b = random.randint(a+1, 50)
    	      meeting = [a, b]
    	      meetings.append(meeting)
    
        print 'meetings= %s' % str(meetings)
        print 'max_meetings= %s' % str(answer(meetings))
        print