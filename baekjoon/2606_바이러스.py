# https://www.acmicpc.net/problem/2606

import sys 
input = sys.stdin.readline

def dfs(current, node, visited):
    visited[current] = 1
    for next_node in node[current] : 
        if visited[next_node] != 1 :
            dfs(next_node, node, visited)
    return

N = int(input())
M = int(input())
NODE = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M) : 
    p, q = map(int, input().split())
    NODE[p].append(q)
    NODE[q].append(p)

dfs(1, NODE, visited)

print(sum(visited)-1)