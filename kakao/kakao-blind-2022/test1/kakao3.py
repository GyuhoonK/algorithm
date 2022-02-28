from collections import defaultdict
from math import ceil, floor
def convert_min(t):
    HH, MM = t.split(':')
    return int(MM) + int(HH) * 60
def solution(fees, records):
    base_time, base_fee, split_time, fee_time = fees
    veh = defaultdict(list)
    answer = []
    for rec in records : 
        t, vin, in_out = rec.split(" ")
        veh[vin].append(convert_min(t))
    key_loop = sorted(veh.keys())
    for key in key_loop:
        log = veh[key]
        if len(log) % 2 != 0 :
            log.append(convert_min("23:59"))
       
        times = 0
        for idx in range(0, len(log)-1, 2) : 
            times += (log[idx+1] - log[idx])
        tmp = base_fee
        if times > base_time:
            tmp += ceil(float(times - base_time)/split_time) * fee_time
        answer.append(tmp)
        
    answer = list(map(lambda x :int(x), answer))
    return answer


print(solution([180, 5000, 10, 600]	, ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10]	, ["00:00 1234 IN"]	))

