## https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3

def isRight(p) :
    if p[0] == ')' : 
        return False
    q = []
    for idx in range(len(p)) : 
        if p[idx] == '(':
            q.append('(')
        else :
            if len(q) == 0 : 
                return False
            q.pop()
    return True

def reverse(p) :
    q = ""
    for idx in range(len(p)) : 
        if p[idx] == '(': 
            q += ")"
        else :
            q += "("
    return q

def split(inputs) : 
    open_cnt = 0
    end_cnt = 0
    if len(inputs) == 0 :
        return ""
    for idx in range(len(inputs)) : 
        if inputs[idx] == '(':
            open_cnt += 1
        else : 
            end_cnt += 1
        if open_cnt == end_cnt :
            break
    u, v = inputs[:idx+1], inputs[idx+1:]
    if not isRight(u) :
        return "("+split(v)+")"+reverse(u)[1:-1]
    else :
        return u + split(v)
    
def solution(p):
    if isRight(p) : 
        return p
    return split(p)