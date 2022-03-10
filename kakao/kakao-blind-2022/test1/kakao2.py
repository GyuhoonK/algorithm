from itertools import combinations
from collections import defaultdict
def rep_combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in rep_combinations(array[i:], r-1):
                yield [array[i]] + next

def solution(n, info):
    answer = [-1, []]
    target = [i for i in range(11)]
    
    for comb in rep_combinations(target, n):
        dic = defaultdict(int)
        for ele in comb :
            dic[ele] += 1 # return list form {index : val}
        score1, score2 = 0, 0
        for i in range(11):
            if (dic[i] == 0) and (info[i] == 0) : continue
            if dic[i] > info[i] :
                score1 += (10-i)
            if dic[i] <= info[i] :
                score2 += (10-i)
        if (score1 > score2) and (answer[0] < (score1 - score2)) :
           answer[1] = [dic[i] for i in range(11)]
           answer[0] = score1 - score2

        if (score1 > score2) and (answer[0] == (score1 - score2)) :
        # if same score, get the list where small points are more.
           answer_1_rev = list(reversed(answer[1]))
           dict_i_rev = list(reversed([dic[i] for i in range(11)]))
           print(answer_1_rev, dict_i_rev)
           answer[1] = max(answer_1_rev, dict_i_rev)
           answer[1].reverse()
    
    if answer[0] == -1:    
        return [-1]
    
    return answer[1]