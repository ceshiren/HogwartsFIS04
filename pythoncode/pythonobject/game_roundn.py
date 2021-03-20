"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/20 3:52 下午'
"""
import random


def fight(enemy_hp, enemy_power):
    my_hp = 1000
    my_power = 200

    # enemy_hp = 1000
    # enemy_power = 200
    while True:
        # 我最终的血量 = 我的血量 - 敌人的攻击力
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        print(my_hp)
        print(enemy_hp)
        # 三目表达式
        # print("我赢了") if my_final_hp > enemy_final_hp else print("敌人赢")
        if my_hp > enemy_hp:
            print("我赢了")
            break
        else:
            print("敌人赢")
            break


# fight()
if __name__ == '__main__':
    # 生成一些血量，每次随机的去选择 血量
    hp = [x for x in range(990, 1100)]
    print(hp)
    enemy_hp = random.choice(hp)
    print(enemy_hp)

    enemy_power = random.randint(190, 210)
    print(enemy_power)

    fight(enemy_hp, enemy_power)
