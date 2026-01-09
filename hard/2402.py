class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)] #minheap
        used = [] # end time, room
        meetcount = [0] * n # meetings scheduled room n = meetcount[n]

        for s, e in meetings:
            while used and s >= used[0][0]: #end the meeting 
                end, room = heapq.heappop(used)
                heapq.heappush(available, room)

            #if no room available
            if not available:
                endtime, room = heapq.heappop(used)
                e = endtime + ( e - s )
                heapq.heappush(available, room)
            
            #if room is available
            room = heapq.heappop(available)
            heapq.heappush(used, (e, room))
            meetcount[room] += 1

            


        return meetcount.index(max(meetcount))