# https://www.acmicpc.net/problem/10282

from math import inf
import sys 
import heapq
input = sys.stdin.readline

def dikstra(start_node, nodes) :
    dist = [inf] * (len(nodes)+1) # dist[i] : i까지 오는데 걸리는 거리
    dist[start_node] = 0 # 자기 자신까지의 거리는 0
    Q = []
    heapq.heappush(Q, (dist[start_node], start_node))
    while Q : 
        cur_dist, cur_node = heapq.heappop(Q)
        if dist[cur_node] < cur_dist : # 현재 노드까지 오는데 걸린 거리(dist[cur_node])보다 방금 지난 edge의 거리가 크다면
            continue # 고려 대상에서 제외한다
        for (w, n) in nodes[cur_node] : 
            if dist[n] > cur_dist + w : 
                dist[n] = cur_dist + w
                heapq.heappush(Q, (cur_dist+w,n)) # (노드를 방문했을 때의 거리, 노드)
    return dist

T = int(input()) 
for _ in range(T) : 
    N, D, C = map(int, input().split()) 
    nodes = [[] for _ in range(N+1)] # nodes[i] : (weight, node)
    for _ in range(D) : 
        a, b, s = map(int, input().split())
        nodes[b].append((s,a))
    dist = dikstra(C, nodes)
    answer = [i for i in dist if i != inf]
    print(len(answer), max(answer))