# %%
import sys
from queue import PriorityQueue
from math import inf

# %%
import sys
from queue import PriorityQueue
from math import inf
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
node = [[] for i in range(n+1)]
dist = [inf for i in range(n+1)]
p_node = [0 for i in range(n+1)]

for i in range(m):
    u, v, c = map(int, sys.stdin.readline().strip().split())
    node[u].append([v,c])
start, end = map(int, sys.stdin.readline().split())
dist[start] = 0

Q = PriorityQueue()
Q.put([dist[start],start]) #dist[start]를 기준으로 Priority
while not Q.empty():
    cur_dist, cur = Q.get()
    for edge in node[cur]:
        next_node, cost = edge
        if dist[next_node] > cost + cur_dist:
            dist[next_node] = cost + cur_dist
            p_node[next_node] = cur
            Q.put([dist[next_node],next_node])
print(dist[end])
path = []
t = end
while t != start:
    path.append(t)
    t = p_node[t]
path.append(t)
print(len(path))
path.reverse()
for i in range(len(path)):
    print(path[i], end = ' ')


