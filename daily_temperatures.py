"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

Input
The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

Sample
Input#1
T = [73, 74, 75, 71, 69, 72, 76, 73]
Output#1
[1, 1, 4, 2, 1, 1, 0, 0]

"""
# Time O(n) | Space O(n)?
# Time is n + n . The for loop AND the while loop run a total of n + n times since the while loop is not iterating
# over all of the elements in daily_temperatures over and over again. It compares the temperatures as it keeps moving
# forward with the iteration. It's kind of tricky to picture it. The important thing to underline here is that the
# answer array does not necessarily get updated in order from left to right. If the nextTemp is > currTemp
# sequentially, then it updates from left to right, but when nextTemp < currTemp, then it skips to the next one until
# it finds a hotter temp, then it updates that one, then it checks the previous one (thanks to the stack keeping track
# of the indexes), then the following previous one, and so on. So in some situations it is updated from left to right
# and others from right to left, then continues left to right after resolving the middle. This can help us see why it's
# not an n^2 time solution. We don't iterate from the beginning, we keep going, working with the next temperature and
# the previous lower temperature.
def daily_temperatures(daily_temperatures):
    # initialize an answer array of same size as daily_temperatures but with 0s as default values
    answer_array = [0]*len(daily_temperatures)
    # initialize a stack
    stack = []
    # loop through daily_temperatures with enumerate to keep track of current index as well as the temperature
    for index, temperature in enumerate(daily_temperatures):
        # while the stack is not empty and the previousTemp < current temperature
        while stack and daily_temperatures[stack[-1]] < temperature:
            # get the indexPreviousLowerTemp from top of stack
            index_previous_lower_temp = stack.pop()
            # calculate the distance between current index and indexPreviousLowerTemp
            # and update the days in our answerArray
            answer_array[index_previous_lower_temp] = index - index_previous_lower_temp
        # insert the current index into the stack
        stack.append(index)
    # return the answer array
    return answer_array

sampleInput = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(sampleInput))


# O(n^2) Time | O(n) Space?
def dailyTemperatures(dailyTemps):
  days_list = []
  for i in range(len(dailyTemps) - 1): # we don't need to check the last one
    found = False
    days = 0
    currTemp = dailyTemps[i]
    for nextTemp in dailyTemps[i+1:]:
      days += 1
      if currTemp < nextTemp:
        days_list.append(days)
        found = True
        break
    if not found:
      days_list.append(0)
  days_list.append(0) # last one is always going to be 0
  return days_list