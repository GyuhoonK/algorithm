def solution(board, skill):
    row = len(board)
    col = len(board[0])
    point_board = [[0 for i in range(col)] for i in range(row)]
   
    for tp, r1, c1, r2, c2, degree in skill :
        if tp == 1 : 
            pm = -1
        else : pm = 1
        point = pm * degree
        rev_point = point * (-1)
        point_board[r1][c1] += point
        if r2+1 < row and c2+1 < col : 
            point_board[r2+1][c2+1] += point
        if r2+1 < row : 
            point_board[r2+1][c1] += rev_point 
        if c2+1 < col : 
            point_board[r1][c2+1] += rev_point
    for idx1 in range(row) :
        for idx2 in range(1, col) : 
            point_board[idx1][idx2] += point_board[idx1][idx2-1]
    for idx1 in range(1,row) :
        for idx2 in range(col) : 
            point_board[idx1][idx2] += point_board[idx1-1][idx2]
    for idx1 in range(row) :
        for idx2 in range(col) : 
            board[idx1][idx2] += point_board[idx1][idx2]
    answer = 0
    for idx1 in range(row): 
        for idx2 in range(col) :
            if board[idx1][idx2] > 0 :
                answer += 1
    
    return answer

ans = solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	, [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	)
print(ans)