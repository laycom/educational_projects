# Программа для вывода на экран по спирали двумерного массива 
# (нечетной размерности). Начальная точка середина массива 
# Приведен пример для массива размерностью 5 х 5


# n = int(input())
# nums = []
# for i in range(n):
    # nums.append(list(map(int, input().split())))
    
n = 5
    
nums = [[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
]



def spiral_output(n, nums):
    start = n // 2
    x, y = start, start
    dx = 0
    dy = -1

    min_x = start
    limit_x = start
    min_y = start - 1
    limit_y = start 
    for i in range(1, n ** 2 + 1):
        print(nums[y][x])
        nx, ny = x + dx, y + dy
    
        if min_x <= nx <= limit_x and min_y <= ny <= limit_y:
            x, y = nx, ny
        else:
            if dy != 0:
                if y == min_y and limit_x != n:
                    limit_x += 1
                elif y == limit_y and min_x != 0:
                    min_x -= 1
            else:
                if x == limit_x and limit_y != n:
                    limit_y += 1
                elif x == min_x and min_y != 0:
                    min_y -= 1
            
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    
if n > 0:       
    spiral_output(n, nums)

