# Напишите программу по следующему описанию. Есть класс "Воин". 
# От него создаются два экземпляра-юнита. Каждому устанавливается здоровье в 100 очков. 
# В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет. 
# У того, кого бьют, оно уменьшается на 20 очков от одного удара. После каждого удара 
# надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья. 
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением 
# о том, кто одержал победу.

import random

class Warrior():

    def __init__(self, name, damage, health=100):
        self.name = name
        self.damage = damage
        self.health = health
    
    def display(self):
        return self.name, self.damage, self.health
        
    def hit(self, enemy):
        if enemy.health != 0:	
            enemy.health -= self.damage
            if enemy.health == 0:
                print('Убит', end=' ') 
            return enemy.health	
        else:
            print('Он уже мертв')
        
warrior_1 = Warrior('warrior_1', 10)
warrior_2 = Warrior('warrior_2', 10)



while warrior_1.health and warrior_2.health != 0:
    count = random.randint(0, 1)
    if count == 1:
        warrior_1.hit(warrior_2)
        print('warrior_1 attack warrior_2')
        print(f' health warrior_1 = {warrior_1.health}\n',
              f'health warrior_2 = {warrior_2.health}')
    else:
        warrior_2.hit(warrior_1)
        print('warrior_2 attack warrior_1')
        print(f' health warrior_1 = {warrior_1.health}\n',
              f'health warrior_2 = {warrior_2.health}')
    
    print()

if warrior_1.health > 0:
    print('warrior_1 win')
    
else:
    print('warrior_1 win')

