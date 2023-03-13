
def solution(rows, columns, queries):
    matrix = [[0] * columns for _ in range(rows)]
    answer = [] # min 값 대입해주기
    
    # matrix 에 값을 대입시켜주기 위해서
    num = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = num
            num += 1
    
    # 행, 열은 -1 한 값이어야함
    for x1, y1, x2, y2 in queries:
        value = matrix[x1-1][y1-1]
        min_num = value
         
        # x2, y1에서 시작 x1, y1까지
        for k in range(x1, x2):
            tmp = matrix[k][y1-1]
            matrix[k-1][y1-1] = tmp
            min_num = min(min_num, tmp)
        
        # x2, y2-1에서 시작
        for l in range(y1, y2):
            tmp = matrix[x2-1][l]
            matrix[x2-1][l-1] = tmp
            min_num = min(min_num, tmp)
        
        # x1, y2에서 시작 x2, y2까지
        
        for m in range(x2-1, x1-1, -1):
            tmp = matrix[m-1][y2-1]
            matrix[m][y2-1] = tmp
            min_num = min(min_num, tmp)

        # x1, y1의 값을 x1, y2에 대입 x1, y2까지
        for n in range(y2-1, y1-1, -1):
            tmp = matrix[x1-1][n-1]
            matrix[x1-1][n] = tmp
            # print(matrix[x1-1][n], x1-1, n)
            min_num = min(min_num, tmp)
            
        
        matrix[x1-1][y1] = value
        
        
        answer.append(min_num)


    return answer
    