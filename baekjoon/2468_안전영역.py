import sys 
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

from collections import deque

N = int(input())
zone = []
for _ in range(N) : 
    line = list(map(int, input().split(" ")))
    zone.append(line)

def dfs(cur_x,cur_y,nodes, visited) : 
    visited[cur_x][cur_y] = 1
    nxt_X = [cur_x,   cur_x,  cur_x-1, cur_x+1]
    nxt_Y = [cur_y-1, cur_y+1, cur_y,  cur_y]
    for nxt_x, nxt_y in zip(nxt_X, nxt_Y) : 
        if nxt_x >= 0 and nxt_x < N and nxt_y >= 0 and nxt_y < N and visited[nxt_x][nxt_y] != 1:
            dfs(nxt_x, nxt_y, nodes, visited)
    

def getMaxNotSubmerged(high) : 
    notSbmgd = [[1 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N) : 
        for col in range(N): 
            if zone[row][col] <= high : 
                notSbmgd[row][col] = 0
                visited[row][col] = 1
    answer = 0
    for row in range(N) : 
        for col in range(N): 
            if visited[row][col] == 0 :
                answer += 1
                dfs(row, col, notSbmgd, visited)
    return answer
answer = 0
for high in range(101) : 
    tmp = getMaxNotSubmerged(high)
    if tmp == 0 : 
        print(answer)
        sys.exit()
    else :
        answer = max(answer, tmp)
print(answer)