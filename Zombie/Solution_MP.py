#Using "itemgetter" improves sorting over using for loop and splitting.
import operator
def answer(meetings):
    schedule = []
    total = 0
    appt_sort = sorted(meetings, key=operator.itemgetter(1))
    for appt in appt_sort:
        booked=False
        for scheduled in schedule:
            #Meetings that start before a scheduled appt ends, but finish after it starts are conflicting
            if scheduled[0] < appt[1] and scheduled[1] > appt[0]:
                booked=True
        if not booked:
            schedule.append(appt)
    #Look for alternative scheduling order if possible
    return len(schedule)