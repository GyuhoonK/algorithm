## https://programmers.co.kr/learn/courses/30/lessons/60057

from collections import defaultdict
def solution(s):
    if len(s) == 1 : return 1
    answer = len(s)
    for n in range(1, len(s)):
        L = len(s)
        
        key = list()
        for i in range(len(s)):
            if not s[n*i:n*(i+1)]:
                break
            key.append(s[n*i:n*(i+1)])
        dup = [1]
        dup_key = list()
        for idx in range(1,len(key)):
            if key[idx] == key[idx-1] :
                dup[-1] += 1
            else :
                dup.append(1)
                dup_key.append(key[idx-1])
        dup_key.append(key[idx])
        
        tmp = 0
        for word, cnt in zip(dup_key, dup):
            if cnt == 1 :
                tmp += len(word)
            else :
                tmp += (len(str(cnt)) + len(word))
        
        if tmp < answer :
            answer = tmp
            print(dup, dup_key)
    return answer