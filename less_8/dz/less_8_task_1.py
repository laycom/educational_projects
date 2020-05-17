# 1. На улице встретились N друзей. Каждый пожал руку 
# всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

def friends_handshake(n):
    handshake = [[1 if i != j else 0 for i in range(n)] for j in range(n)]
    sum = 0
    for i, items in enumerate(handshake):
        for item in items[i:]:
            if item == 1:
                sum += 1
    return(sum)

n = 10
print(f'У {n} друзей было {friends_handshake(n)} рукопожатий') 
