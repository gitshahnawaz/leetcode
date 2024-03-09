"""
539. Minimum Time Difference
Solved
Medium
Topics
Companies
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
"""


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minutes(time):
            hrs, minutes = time.split(":")
            return 60 * int(hrs) + int(minutes)

        times = set(timePoints)
        if len(times) != len(timePoints): return 0
        times = list(map(convert_to_minutes,times))
        times.extend([minute + 24 * 60 for minute in times])
        times.sort()

        min_diff = 24*60

        for i in range(1, len(times)):
            min_diff = min(min_diff, times[i] - times[i-1])
        
        return min_diff


        