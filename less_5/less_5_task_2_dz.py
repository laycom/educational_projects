from collections import deque

def convert(num):
    deq_num = deque(num.upper())
    return deq_num
    
print(convert('A2'))