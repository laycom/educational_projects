# Программист на пляже

nums_tests = int(input())
tests_diff = []

for _ in range(nums_tests):
    sunbeds = int(input())
    tested_sunbeds = sorted(list(map(int, input().split())))
    
    if len(tested_sunbeds) != sunbeds:
        print('неверное число лежаков')
    
    min_diff = tested_sunbeds[0] ^ tested_sunbeds[1]
    # for j in range(sunbeds - 1):
        # for k in range(j + 1, sunbeds):
            # if tested_sunbeds[j] ^ tested_sunbeds[k] < min_diff:
                # min_diff = tested_sunbeds[j] ^ tested_sunbeds[k]
                
    for i in range(1, sunbeds):
        min_diff = min(min_diff, tested_sunbeds[i - 1] ^ tested_sunbeds[i])
    
    tests_diff.append(min_diff)
    
for item in tests_diff:
    print(item)
            
            
        