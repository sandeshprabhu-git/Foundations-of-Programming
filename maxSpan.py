"""


Consider the leftmost and righmost appearances of some value in an array. 
We'll say that the "span" is the number of elements between the two inclusive. 
A single value has a span of 1. Returns the largest span found in the given array. 
(Efficiency is not a priority.)


maxSpan([1, 2, 1, 1, 3]) → 4
maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6


"""

import collections

def maxSpan(nums):
    numdict = collections.defaultdict(list)
    maxlen = 0
    span = 0
    for i, num in enumerate(nums):
        numdict[num].append(i)
        print(numdict)
        n = len(numdict[num])
        if maxlen < n:
            maxlen = n
            span = numdict[num][-1] - numdict[num][0] + 1
    return span


print(maxSpan([1, 2, 1, 1, 3]))
print(maxSpan([1, 4, 2, 1, 4, 4, 4]))