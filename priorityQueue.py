import itertools
import heapq

# This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.


pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)
    
def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    print entry_finder
    print pq
    entry[-1] = REMOVED
    print pq
    #here entry[-1] is an address, when you changed it the related qp element will change. 
    #entry_finder only take the responsible for storing data
    
def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

add_task(5)
add_task(6,1)
add_task(7,3)
add_task(8,-1)
remove_task(5)

'''
testqueue = dict()
for i in range(10):
    testqueue[i] = i
xt = testqueue.pop(4)
print testqueue
'''
