import requests
import json
import random

x_auth_token = "f5a4370d154f58a4b668798ebf98da56"
url = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

headers = {
    "X-Auth-Token" : x_auth_token,
    "Content-Type" : "application/json"
}

def startProb(url, prob, headers = {"X-Auth-Token" : x_auth_token,"Content-Type" : "application/json"}):
    start_url = url + '/start'
    params = {"problem" : prob}
    res = requests.post(start_url, headers = headers, params = params)
    return res.json()['auth_key']

def getWaitLine(url, auth_key):
    headers = {'Authorization' : auth_key,
              'Content-Type' : 'application/json'}
    res = requests.get(url + '/waiting_line', headers = headers)
    return res.json()['waiting_line']

def getGameResult(url, auth_key):
    headers = {'Authorization' : auth_key,
              'Content-Type' : 'application/json'}
    res = requests.get(url + '/game_result', headers = headers)
    return res.json()['game_result']

def getUserInfo(url, auth_key):
    headers = {'Authorization' : auth_key,
              'Content-Type' : 'application/json'}
    res = requests.get(url + '/user_info', headers = headers)
    return res.json()['user_info']

def putMatch(url, auth_key, pairs):
    headers = {'Authorization' : auth_key,
              'Content-Type' : 'application/json'}
    params = {
        "pairs" : pairs
    }
    res = requests.put(url + '/match', headers = headers, data = json.dumps(params))
    return res.json()

def putChangeGrade(url, auth_key, commands):
    headers = {'Authorization' : auth_key,
              'Content-Type' : 'application/json'}
    params = {
        "commands" : commands
    }
    res = requests.put(url + '/change_grade', headers = headers, data = json.dumps(params))

    return res.json()

def changeUserGrade(exist, userInfo, game_log, num):
    points = []
    for i in range(1, num+1):
        lose_point = 0
        for lose_log in game_log[i]['lose']:
            lose_point += (num - userInfo[lose_log-1]['grade'])
        win_point = 0
        for win_log in game_log[i]['win']:
            win_point += (num - userInfo[win_log-1]['grade'])
        i_point = win_point - lose_point
        points.append([i, i_point])
    max_point = max(list(map(lambda x : x[1], points)))
    min_point = min(list(map(lambda x : x[1], points)))
    for i, point in points :
        if len(game_log[i]['lose']) == 0 and len(game_log[i]['win']) == 0:
            
            points[i-1][1] = random.randint(min_point+1, max_point-1)
    points = sorted(points, key = lambda x : x[1], reverse=True)
    
    new_commands = [{'id' : i , 'grade' : grade} for grade,(i,point) in enumerate(points, 1)]
    return new_commands

def getScore(url, auth_key):
    headers = {'Authorization' : auth_key,
              'Content-Type' : 'application/json'}
    res = requests.get(url + '/score', headers = headers)
    return res.json()

def IsAbuser(key, game_log):
    avg_taken = sum(game_log[key]['taken']) / len(game_log[key]['taken'])
    if avg_taken <= 10:
        return True
    return False

def findMatch(wait_line, userGrade, game_log, turn, abusers):
    pairs = []
    wait_users = [line['id']  for line in wait_line]
    users_from = {line['id']:line['from']  for line in wait_line}
    
    
    wait_users = list(set(wait_users) - set(abusers))
    
    while wait_users : 
        diff = 99999999
        user1 = wait_users[0]
        if len(wait_users) == 1 :
            break
        fight = 0
        grade1 = userGrade[user1-1]['grade']
        
        for user2 in wait_users :
            if user2 == user1 : continue
#             if (user2 in game_log[user1]['win']) and (turn - users_from[user2] < 1): continue
            grade2 = userGrade[user2-1]['grade']
            if abs(grade1-grade2) < diff :
                diff = abs(grade1-grade2)
                fight = user2
        pairs.append([user1, fight])
        wait_users.remove(user1)
        if fight == 0 :
            pairs.remove([user1, fight])
        else :
            wait_users.remove(fight)
            
    wait_aubsers = [abu for abu in wait_users if abu in abusers]
    while wait_aubsers : 
        diff = 99999999
        user1 = wait_aubsers[0]
        if len(wait_aubsers) == 1 :
            break
        fight = 0
        grade1 = userGrade[user1-1]['grade']
        
        for user2 in wait_aubsers :
            if user2 == user1 : continue
#             if (user2 in game_log[user1]['win']) and (turn - users_from[user2] < 1): continue
            grade2 = userGrade[user2-1]['grade']
            if abs(grade1-grade2) < diff :
                diff = abs(grade1-grade2)
                fight = user2
        pairs.append([user1, fight])
        wait_aubsers.remove(user1)
        if fight == 0 :
            pairs.remove([user1, fight])
        else :
            wait_aubsers.remove(fight)
            
    return pairs

def changeUserGrade(exist, userInfo, game_log, num):
    points = []
    no_records = []
    for i in range(1, num+1):
        lose_point = 0
        if len(game_log[i]['lose']) == 0 and len(game_log[i]['win']) == 0 :
            no_records.append(i)
            points.append([i, 0])
            continue
        for lose_log in game_log[i]['lose']:
            lose_point += (num - userInfo[lose_log-1]['grade'])
        win_point = 0
        for win_log in game_log[i]['win']:
            win_point += (num - userInfo[win_log-1]['grade'])
        i_point = win_point - lose_point
        points.append([i, i_point])

    max_point = max(list(map(lambda x : x[1], points))) +1
    min_point = min(list(map(lambda x : x[1], points))) -1

    for idx in no_records:
        points[idx-1][1] = random.randint(min_point, max_point)
    points = sorted(points, key = lambda x : x[1])
    
    new_commands = [{'id' : i , 'grade' : grade} for grade,(i,point) in enumerate(points, 1)]
    
    return new_commands

# Set All Users Grade 
num = 900
auth_key = startProb(url, 2)
random_init = random.choices([i for i in range(1,num+1)], k = num)
commands = [{"id" : i, "grade" : grade} for i, grade in enumerate(random_init, 1)]
putChangeGrade(url, auth_key, commands)
putMatch(url, auth_key, [])

# Random Match
userInfo = getUserInfo(url, auth_key)
game_log = {i : {'win': [] ,'lose': [], 'taken' : [] } for i in range(1, num+1)}


putChangeGrade(url, auth_key, commands)
putMatch(url, auth_key, [])
wait_line = getWaitLine(url, auth_key)
abusers = []

pairs = findMatch(wait_line, userInfo, game_log, 1, abusers)

while True:
    turn = putMatch(url, auth_key, pairs = pairs)
    time = turn['time']
    print(time)
    userInfo = getUserInfo(url, auth_key)
    if time == 595 : 
        commands = changeUserGrade(commands, userInfo, game_log, num)
        putChangeGrade(url, auth_key, commands)
        putMatch(url, auth_key, [])
        break
    game_result = getGameResult(url, auth_key)
    if game_result : 
        for gs in game_result :
            game_log[gs['win']]['win'].append(gs['lose'])
            game_log[gs['lose']]['lose'].append(gs['win'])
            game_log[gs['win']]['taken'].append(gs['taken'])
            game_log[gs['lose']]['taken'].append(gs['taken'])
        for key in game_log.keys():
            if len(game_log[key]['taken']) >= 10:
                if IsAbuser(key, game_log) and key not in abusers:
                    abusers.append(key)
        commands = changeUserGrade(commands, userInfo, game_log, num)
    
    putChangeGrade(url, auth_key, commands)
    userInfo = getUserInfo(url, auth_key)
    wait_line = getWaitLine(url, auth_key)
    if wait_line :
        pairs = findMatch(wait_line, userInfo, game_log, time, abusers)
        
    else :
        pairs = []

print(getScore(url, auth_key))