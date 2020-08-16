import heapq
"""
def maxEvents(events):
    events.sort()  # sort in ascending order by start time
    cnt = 0  # the number of events we'll attend
    event_id = 0  # think of this as the index for the event
    day = 1  # start at day 1
    last_day = max(d for d in events[1])
    min_heap = []

    while day <= last_day:

        # if there are no events today, then let's move the day to the next available event's start day
        if event_id < len(events) and not min_heap:
            day = events[event_id][0]

        # while there are events available TODAY, add them to the heap by end date
        while event_id < len(events) and events[event_id][0] <= day:
            heapq.heappush(min_heap, events[event_id][1])
            event_id += 1

        # while there are events that have already passed, delete them off the heap
        while min_heap and min_heap[0] < day:
            heapq.heappop(min_heap)

        # if there are events to see today, see the one with the shortest duration
        if min_heap:
            heapq.heappop(min_heap)
            cnt += 1
        # else, if the index is already past the length of the events array, then there's no more events to attend
        elif event_id >= len(events):
            break
        # after checking for events, putting them in our heap, and maybe attending one, go on to next day
        day += 1

    return cnt
"""

def maxEvents(events):
    events.sort()  # sort in ascending order by start day
    min_heap = []
    cnt = 0
    day = 0
    while events or min_heap:
        # if there's no events 'down' on our 'to see today list' (the heap), skip to the next event's start day
        if not min_heap:
            day = events[0][0]
        # while there are events available TODAY, add them to the heap by end date and take them off our events list
        while events and events[0][0] <= day:  # <= could be == also
            heapq.heappush(min_heap, events.pop()[1])
        # attend an event (the one with the soonest end day)
        heapq.heappop(min_heap)
        cnt += 1
        day += 1
        # while there are events that have already passed, delete them off the heap
        while min_heap and min_heap[0] < day:
            heapq.heappop(min_heap)
    return cnt

events = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
print(maxEvents(events))
