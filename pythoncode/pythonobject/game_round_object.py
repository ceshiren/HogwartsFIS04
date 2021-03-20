"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/20 3:59 下午'
"""


class Game:
    # 血量，攻击
    def __init__(self, my_hp, enemy_hp):
        self.my_hp = my_hp
        self.my_power = 200

        self.enemy_hp = enemy_hp
        self.enemy_power = 199

    def fight(self):
        # fight() 打架
        while True:
            # 我最终的血量 = 我的血量 - 敌人的攻击力
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)
            print(self.enemy_hp)
            # 三目表达式
            # print("我赢了") if my_final_hp > enemy_final_hp else print("敌人赢")
            if self.my_hp > self.enemy_hp:
                print("我赢了")
                break
            else:
                print("敌人赢")
                break

    def back_home(self):
        print("准备 回城~")


class HouYi(Game):

    def __init__(self, my_hp, enemy_hp):
        self.defense = 100
        super().__init__(my_hp, enemy_hp)

    def fight(self):
        # fight() 打架
        while True:
            # 我最终的血量 = 我的血量 - 敌人的攻击力
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)
            print(self.enemy_hp)
            # 三目表达式
            # print("我赢了") if my_final_hp > enemy_final_hp else print("敌人赢")
            if self.my_hp > self.enemy_hp:
                print("我赢了")
                break
            else:
                print("敌人赢")
                break


# 调用
# game1 = Game()
# game1.fight()
houyi = HouYi(1300, 200)
houyi.fight()
houyi.back_home()
