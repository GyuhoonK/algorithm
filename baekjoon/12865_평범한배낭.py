# https://www.acmicpc.net/problem/12865
# DP[i][j] : 배낭에 넣은 물품 무게 합이 j일 때, 가치 합의 최대값
# DP[i][j] = DP[i-1][j] if j < W[i]
#          = max(DP[i-1][j], D[i-1][j-W[i]] +V[i]) if j >= W[i]

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = []
for _ in range(N) : 
    w, v = map(int, input().split())
    items.append((w, v))

DP = [[0 for _ in range(K+1)] for _ in range(N+1)]


for n, (w, v) in zip(range(1, N+1), items) : 
    for k in range(1, K+1) : 
        if k < w : # 가방의 무게(k)보다 현재 선택된 item이 더 무겁다면
            DP[n][k] = DP[n-1][k] # 해당 item을 담을 수 없으므로 이전 값을 그대로 사용
        else : # 가방의 무게(k)보다 현재 선택된 item이 더 가볍다면
            DP[n][k] = max(DP[n-1][k], DP[n-1][k-w] + v)
            # 가방에서 1개를 빼고(n-1), 현재 item을 넣은 것과 넣지 않은 것 중에서 더 가치가 높은 경우를 입력

print(DP[N][K])