"""
1. 아이디어
- 2중 for문 => 값 1 && 방문X ==> BFS
- BFS 돌면서 그림 개수 +1, 최대값을 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : m * n = 500 * 500
- E : V * 4 = 500 * 500 * 4
- V + E = V + 4V = 5V = 5 * m * n = 5 * 500 * 500 = 5 * 25000 = 100만 < 2억 ==> 가능!!

# m과 n은 최대 500
# 1초당 연산 2억개 가능

3. 자료구조형
- 그래프 전체 지도 : int[][] (2차원 배열)
- 방문 여부 : bool[][]
- Queue (BFS)

"""

import sys
input = sys.stdin.readline

n,m = map(int, input())
map = lis