import sys

# input = sys.stdin.readline().rstip()

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()



def getPi(P) :
    m = len(P)
    j = 0
    pi = [0 for _ in range(m+1)]
    for i in range(1, m) :
        while (j > 0 and P[i] != P[j]):
            j = pi[j-1]
        if P[i] == P[j] :
            j += 1
            pi[i] = j
    return pi

pi = getPi(P)

def KMP(T, P) : 
    answer = {"count" : 0 ,
             "index" : []}
    n = len(T)
    m = len(P)
    j = 0
    for i in range(n) : 
        while (j > 0 and T[i] != P[j]):
            j = pi[j-1]
        if T[i] == P[j]:
            if j == m-1 :
                answer['count'] += 1
                answer['index'].append(i-m+1)
                j = pi[j]
            else :
                j += 1
    return answer



answer = KMP(T, P)

print(answer['count'])
print(' '.join(list(map(lambda x : str(x+1), answer['index']))))