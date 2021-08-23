def solution(table, languages, preference):
    answer = ''
    
    encoded_table = []
    dict_prf = {}
    score_table = []
    result_table = []
    
    for i in table:
        encoded_table.append(i.split(" "))
    
    for i, j in zip(languages, preference):
        dict_prf[i] = j
        
    for i in range(0, 5):
        score_table.append([0, 5, 4, 3, 2, 1])
        
    print(score_table)
    for i in range(0, 5):
        for j in range(0, 6):
            if encoded_table[i][j] in dict_prf:
                score_table[i][j] = score_table[i][j] * dict_prf[encoded_table[i][j]]
            else : 
                score_table[i][j] = 0
    
    for i in range(0, 5):
        result_table.append([sum(score_table[i]), encoded_table[i][0]]);
    
    result_table = sorted(result_table, key = lambda x : (x[0], x[1]))
    max_result = result_table[4][0]
    
    for i in range(0, 5):
        if(result_table[i][0] == max_result):
            return result_table[i][1]
