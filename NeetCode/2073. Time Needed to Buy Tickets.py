class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        # timer = 0
        # i = 0
        # size = len(tickets)
        # while tickets[k] != 0:
        #     if i > size-1:
        #         i=0
        #     if tickets[i] != 0:
        #         tickets[i] -= 1
        #         timer+=1
        #     i+=1
        # return timer
        timer = 0
        for i in range(len(tickets)):
            if i <= k:
                timer += min(tickets[i],tickets[k])
            else:
                timer += min(tickets[i],tickets[k]-1)
        return timer