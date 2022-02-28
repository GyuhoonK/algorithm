from collections import defaultdict 
def solution(record):
    uid_name = defaultdict(str)
    answer = []
    for rec in record : 
        if rec[0] == 'L' :
            action, uid = rec.split(' ')
            answer.append(f"{uid}님이 나갔습니다.")
            continue
        action, uid, name = rec.split(' ')
        uid_name[uid] = name
        if action == 'Enter':
            answer.append(f"{uid}님이 들어왔습니다.")
            
    for idx in range(len(answer)):
        uid, rest = answer[idx].split('님')
        nickname = uid_name[uid]
        answer[idx] = f"{nickname}님"+rest
    
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])