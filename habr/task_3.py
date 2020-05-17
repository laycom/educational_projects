# Перемещение чанков

def read_int():
    return map(int, input().split())

def read_ints():
    return list(map(int, input().split()))
    
def check(list, chanks_servers):
    server_1 = list[0]
    server_2 = list[1]
    count = 0
    for chank in range(list[2], list[3] + 1):
        if server_1 != chanks_servers[chank - 1]:
            return 0
        else:
            count += 1
    if count == list[3] + 1 - list[2]:
        return 1
    else:
        return 0
    
    

nums_chanks, nums_servers, nums_requests = read_int()
chanks_servers = read_ints()
requests = []
responses = []

for _ in range(nums_requests):
    requests.append(read_ints())


for request in requests:
    if check(request, chanks_servers) == 1:
        for chank in range(request[2], request[3] + 1):
            chanks_servers[chank - 1] = request[1]
        responses.append([1])
    else:
        responses.append([0])
        
for response in responses:
    print(*response)