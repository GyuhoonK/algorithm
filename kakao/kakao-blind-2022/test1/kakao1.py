from collections import defaultdict

def solution(id_list, report, k):
    user_reporting = defaultdict(set)
    user_reported = defaultdict(set)
    for rep in report :
        reporting, reported = rep.split(' ')
        user_reporting[reporting].update(set([reported]))
        user_reported[reported].update(set([reporting]))
    answer = []
    for user in id_list :
        tmp = 0
        for mail in user_reporting[user]:
            if len(user_reported[mail]) >= k:
                tmp += 1
        answer.append(tmp)
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"]	, 3))