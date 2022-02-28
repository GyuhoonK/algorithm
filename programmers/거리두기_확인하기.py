def getDist(x1, y1, x2, y2) : 
    return abs(x1-x2) + abs(y1-y2)

def isPartition(x1, y1, node) : 
    if node[x1][y1] == 'X':
        return True
    else : False

def isPossible(x1, y1, x2, y2, node): 
    dist = getDist(x1,y1,x2,y2) 
    if dist > 2 :
        return 1
    else : 
        if x1 == x2 : 
            if not isPartition(x1, int((y1+y2)/2), node) : 
                # print('here', x1, y1, x2, y2)
                return 0
            else : return 1
        if y1 == y2 : 
            if not isPartition(int((x1+x2)/2), y1, node) :
                # print('here', x1, y1, x2, y2)
                return 0
            else : return 1
        if not isPartition(x1, y2, node) :
            return 0
        if not isPartition(x2, y1, node) : 
            return 0
        return 1
    
def solution(places):
    answer = []

    for lines in places : 
        NODE = []
        for line in lines : 
            NODE.append(list(line))
        P = []
        for x in range(5):
            for y in range(5):
                if NODE[x][y] == 'P' : 
                    P.append((x,y))
        # print(NODE)
        TF = 1
        for x1,y1 in P :
            for x2,y2 in P :
                if x1 == x2 and y1 == y2 :
                    continue
                tmp = isPossible(x1,y1,x2,y2, NODE)

                TF = min(TF, tmp)
        answer.append(TF)
                
                

    return answer
# print(getDist(0,0,0,0))
# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))