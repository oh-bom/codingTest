import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while len(scoville) > 1 and scoville[0] < K:
        least1 = heapq.heappop(scoville)
        least2 = heapq.heappop(scoville)
        new_scoville = least1 + least2 * 2
        heapq.heappush(scoville, new_scoville)
        count += 1

    if scoville[0] < K:
        return -1

    return count