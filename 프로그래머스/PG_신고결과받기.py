def solution(id_list, report, k):
    answer = []
    
    id_dict = {}
    id_num = {}
    
    for people in id_list:
        id_dict[people] = id_dict.get(people, list())
        id_num[people] = id_num.get(people, 0)
        
        
    for report_name in report:
        reporter, name = report_name.split()
        if name not in id_dict[reporter]:
            id_dict[reporter].append(name)
            id_num[name] += 1
            

    for value in id_dict.values():
        cnt = 0
        for v in value:
            if id_num[v] >= k:
                cnt += 1
        
        answer.append(cnt)
        
        
    return answer
