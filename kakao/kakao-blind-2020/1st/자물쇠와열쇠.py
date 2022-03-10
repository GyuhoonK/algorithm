## https://programmers.co.kr/learn/courses/30/lessons/60059
## REF :  https://velog.io/@tjdud0123/%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python

def rotate(key) : 
    L = len(key)
    rotated = [[0 for _ in range(L)] for _ in range(L)]
    for l in range(L) : 
        for idx in range(L) :
            rotated[idx][(L-1)-l] = key[l][idx] 
    return rotated
    # return list(zip(*key[::-1]))

def inKey(x, y, M, key, board) :
    for i in range(M) : 
        for j in range(M) : 
            board[x+i][y+j] += key[i][j]
            
def outKey(x, y, M, key, board) :
    for i in range(M) : 
        for j in range(M) : 
            board[x+i][y+j] -= key[i][j]
            
def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True    

def solution(key, lock):
    M, N = len(key), len(lock) 
    board = [[0] * (M*2 + N) for _ in range(M*2 + N)]
    for i in range(N) : 
        for j in range(N) : 
            board[i+M][j+M] = lock[i][j]
    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate(rotated_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                # 열쇠 넣어보기
                inKey(x, y, M, rotated_key, board)
                # lock 가능 check
                
                if(check(board, M, N)):
                    return True
                outKey(x, y, M, rotated_key, board)
                
    return False    
    