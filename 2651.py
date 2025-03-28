class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        final_time = (arrivalTime + delayedTime)% 24
        return final_time
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        