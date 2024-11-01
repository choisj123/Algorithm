# 백준 2775

import sys
import heapq

# T = int(sys.stdin.readline())

# for _ in range(T):
#     K = int(sys.stdin.readline()) # 층
#     N = int(sys.stdin.readline()) # 호

#     # 0번째 층의 사람수
#     DP = [i for i in range(1, N+1)]

#     for a in range(K):
#         for b in range(1, N):
#             DP[b] += DP[b-1]
            
#     print(DP[N - 1])

# softeer 6283
# s =list(map(int, sys.stdin.readline().split()))

# if s == list(range(1, 9)):
#     print("ascending")
# elif s == list(range(8, 0, -1)):
#     print("descending")
# else:
#     print("mixed")

#softeer 9496
N = int(sys.stdin.readline())
processes = list(map(int, sys.stdin.readline().split()))

end_times = []
current_time = 0

for process in processes:
    # 작업을 시작할 수 있는 가장 이른 시점 계산
    while end_times and end_times[0] <= current_time:
        heapq.heappop(end_times)  # 끝난 작업 제거

    # 현재 작업을 시작할 수 있는지 확인
    if len(end_times) == 0 or (current_time + process) <= (end_times[0] - 1):
        # 작업을 시작하고 종료 시점을 힙에 추가
        heapq.heappush(end_times, current_time + process)
        current_time += 1  # 작업 시작 후 시간 증가
    else:
        # 겹침으로 인해 작업을 시작할 수 없을 때 다음 가능한 시점으로 이동
        current_time = end_times[0]

# 마지막 작업이 끝나는 시점을 찾기 위해 최종 종료 시점을 확인
while end_times:
    current_time = heapq.heappop(end_times)

# 최소 시간을 출력
print(current_time)