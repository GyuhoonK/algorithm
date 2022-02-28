def solution(rows, columns, queries):
    matrix = [[i for i in range(j, j+rows)] for j in range(1, columns*rows+1, rows)]
    answer = []
    for qry in queries : 
        x1, y1, x2, y2 = qry
        line1 = matrix[x1-1][y1-1:y2]
        line1 += matrix[x2-1][y1-1:y2]
        
        for x in range(x1, x2-1):
            line1 += [matrix[x][y1-1]]
            line1 += [matrix[x][y2-1]]
        answer.append(min(line1))
        print(line1)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	))
print(solution(100, 97, [[1,1,100,97]]	))