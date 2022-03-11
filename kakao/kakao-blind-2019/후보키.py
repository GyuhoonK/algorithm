## https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations
from collections import defaultdict

def isUsed(target, candidate_keys) :
    if not candidate_keys : 
        return False
    for can_key in candidate_keys :
        if len(can_key.intersection(target)) == len(can_key) :
            return True
    return False

def solution(relation):
    answer = 0
    n_row = len(relation)
    n_col = len(relation[0])
    cols = [idx for idx in range(n_col)]
    candidate_keys = []
    for N in range(1, n_col+1) :
        for comb in combinations(cols, N):
            dict_ = defaultdict(int)
            for row in relation : 
                target_idx = set([col for col in comb])
                target = [str(row[col]) for col in comb]
                candidate_key = "_".join(target)
                dict_[candidate_key] += 1
            if 2 not in dict_.values() and len(dict_.keys()) == n_row:
                if not isUsed(target_idx, candidate_keys): 
                    answer += 1
                    candidate_keys.append(target_idx)

    return answer
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

print(solution([['a','b','c'],
[1,'b','c'],
['a','b',4],
['a',5,'c']]))

print(solution([
    ['a',1,4],
[2,1,5],
['a',2,4],
]))

print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']])

)