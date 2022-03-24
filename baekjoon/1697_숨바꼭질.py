# https://www.acmicpc.net/problem/1697
# 이동 시간이 모두 1초이므로 BFS로 접근
# 

import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().strip().split())

MAX_NUM = 10**5
visit = [0 for i in range(MAX_NUM + 1)]
def bfs(x, K):
    stack = deque()
    stack.append(x)
    while len(stack) > 0 :
        cur = stack.popleft()
        #print(cur)
        if cur == K :
            print(visit[K])
            return
        next_nodes = [cur + 1, cur - 1 , 2 * cur] # 다음 이동 가능한 node
        for next_node in next_nodes :
            if (0 <= next_node < MAX_NUM + 1) and (visit[next_node] == 0): 
                stack.append(next_node)
                visit[next_node] = visit[cur] + 1
bfs(N, K)