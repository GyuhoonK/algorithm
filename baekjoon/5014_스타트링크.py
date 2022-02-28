import sys 
input = sys.stdin.readline

from collections import deque

F, S, G, U, D = map(int, input().split(' '))

building = [0 for i in range(F+1)] # 건물은 1층부터 시작, building[F]까지 존재
# building[idx] = 0 : idx층을 방문하지 않았음 
# building[idx] > 0 : idx층을 방문했음

def bfs() : 
    queue = deque([S])
    building[S] = 1
    while queue : 
        cur = queue.popleft()
        if cur == G : 
            print(building[G]-1)
            return
        if cur+U <= F and building[cur+U] == 0 : # UP 조건 : F층 이하 & 미방문
            building[cur+U] = building[cur] + 1
            queue.append(cur+U)
            
        if cur-D > 0 and building[cur-D] == 0 : # DOWN 조건 : 1층 이상 & 미방문 
            building[cur-D] = building[cur] + 1
            queue.append(cur-D)
    return 

bfs()

if building[G] == 0 : 
    print("use the stairs")
else :
    print(building[G]-1)