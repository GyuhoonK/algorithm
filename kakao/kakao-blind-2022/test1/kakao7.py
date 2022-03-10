# 승패에는 관심 없다
# 최대한 많음 board를 밟아라 (최대한 많은 0을 만드는 경우를 찾아라)
# 2개가 동시에 탐색을 시작한다
# 완전탐색 !
import copy
def findBoard(board, loc) : 
    x, y = loc
    next_X = [x,   x,   x+1, x-1]
    next_Y = [y+1, y-1, y,   y]
    possible = []
    for n_x, n_y in zip(next_X, next_Y) : 
        if n_x < len(board) and n_y < len(board[0]) and n_x >= 0 and n_y >= 0 and board[n_x][n_y] == 1 :
            possible.append((n_x, n_y))
    return possible
def is_possible(board, aloc, bloc): 
    if len(findBoard(board, aloc)) == 0 or len(findBoard(board, bloc)) == 0 :
        return False
    else :
        return True
def serach(board, aloc, bloc, count, answer = [-1], turn = 'A') :
    print("A", aloc, "B", bloc, "count", count)
    new_board = copy.deepcopy(board)
    if aloc[0] == bloc[0] and aloc[1] == bloc[1] : 
        answer.append(count)
        return
    if is_possible(board, aloc, bloc) :
        if turn == 'A' : # A가 움직일 차례
            new_board[aloc[0]][aloc[1]] = 0 # 현재 발판을 사용했음 표시
            next_aloc = findBoard(new_board, aloc) # 움직일 수 있는 발판 찾기
            for n_aloc in next_aloc:
                serach(new_board, n_aloc, bloc, count+1, answer, turn = 'B')
        else : # B가 움직일 차례
            new_board[bloc[0]][bloc[1]] = 0
            next_bloc = findBoard(new_board, bloc)
            for n_bloc in next_bloc :
                serach(new_board, aloc, n_bloc, count+1, answer, turn = 'A')
    else : # 더 이상 움직일 수 없는 상태에 도달했다면,        
        answer.append(count)
        return
def solution(board, aloc, bloc):
    answer = [-1]
    serach(board, aloc, bloc, 0, answer, turn = 'A')
    answer = max(0, max(answer))
    return answer

print("TEST 1")
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))

print("TEST 2")
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))

print("TEST 3")
print(solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]))

print("TEST 4")
print(solution([[1]], [0, 0], [0, 0]
))