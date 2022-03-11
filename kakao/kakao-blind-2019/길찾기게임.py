## https://programmers.co.kr/learn/courses/30/lessons/42892
## https://wiselog.tistory.com/103

import sys
sys.setrecursionlimit(10**6)

def pre(sY,  order) : 
    cur_node = sY[0] # 현재 노드
    leftY = []
    rightY = []
    for i in range(1, len(sY)) :
        if cur_node[0] > sY[i][0] : # 현재 노드의 x 좌표보다 작은 값들만 선택(left)
            leftY.append(sY[i])
        else :# 현재 노드의 x 좌표보다 큰 값들만 선택(right)
            rightY.append(sY[i])
    order.append(cur_node[2]) # 현재 노드를 먼저 기록(전위방문)
    if leftY : 
        pre(leftY, order)
    if rightY : 
        pre(rightY, order)
    return

def post(sY, order) : 
    cur_node = sY[0] # 현재 노드
    leftY = []
    rightY = []
    for i in range(1, len(sY)) : 
        if cur_node[0] > sY[i][0] : 
            leftY.append(sY[i])
        else :
            rightY.append(sY[i])
    if leftY : 
        post(leftY, order)
    if rightY : 
        post(rightY, order)
    order.append(cur_node[2]) # 현재 노드를 나중에 기록(후위방문)
    return

def solution(nodeinfo):
    sortedY = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    
    for idx in range(len(nodeinfo)) : 
        nodeinfo[idx].append(idx+1)
    answer0 = []
    answer1 = []
    pre(sortedY, answer0)
    post(sortedY, answer1)
    
    return [answer0, answer1]

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])