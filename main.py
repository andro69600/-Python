import random
import time
class Weapon:
    def __init__(self,damage,mana_usage,ability):
        self.damage = damage
        self.mana_usage = mana_usage
        self.ability = ability
magic_staff=Weapon(damage=40,mana_usage=95,ability="Магический щит")
bow=Weapon(damage=20,mana_usage=100,ability="Тройной выстрел")
sword=Weapon(damage=25,mana_usage=90,ability="Удар с размаха")
current_weapon = "nothing"
health_points = 100
mana = 100
weapon_stats = 0
stat_weapon = 0
weapon = 0
defense = 0
dodge = 0
print("Выберите свой класс, за который будете играть (1 - это воин) (2 - это лучник) (3 - это маг)")
player_class = int(input())
if player_class == 1:
    current_weapon = "Меч"
    weapon_stats = sword
    health_points = 150
    defense = 30
    dodge = 0
elif player_class == 2:
    current_weapon = "Лук"
    weapon_stats = bow
    health_points = 90
    defense = 20
    dodge = 50
elif player_class == 3:
    current_weapon = "Посох мага"
    weapon_stats = magic_staff
    health_points = 100
    defense = 10
    dodge = 10
if weapon == 1:
    current_weapon = "Меч"
    weapon_stats = sword
elif weapon == 2:
    current_weapon = "Лук"
    weapon_stats = bow
elif weapon == 3:
    current_weapon = "Посох мага"
    weapon_stats = magic_staff
if current_weapon == "Посох мага":
    stat_weapon = magic_staff.damage,magic_staff.mana_usage
elif current_weapon == "Лук":
    stat_weapon = bow.damage,bow.mana_usage
elif current_weapon=="Меч":
    stat_weapon = sword.damage,sword.mana_usage
def stats(health_points, mana, current_weapon,weapon_stats):
    print(f"Ваша статистика:""\n"
          f"{health_points} очков здоровья""\n"
          f"{mana} очков маны"'\n'
          f"{current_weapon} в снаряжении""\n"
          f"{dodge} текущее кол-во шанса уворота""\n"
          f"{defense} текущее кол-во защиты(10 защиты = на 5 урона меньше")
    print(f"Статистика оружия: {stat_weapon} (урон,использование маны для спец.атак)")
    print("Что по способностям?"
          "Маг - Магический Щит - дает 5 уворота навсегда и дает 100 шанс увернуться от следующего удара"
          "Лучник - Тройной выстрел - дает 5 урона навсегда, делает следующий выстрел тройным(тоесть урон умножили на 3, добавленный урон в счет идет)"
          "Воин - Удар с размаха - дает 100 защиты на следующий ход (50 урона не пройдет по вам) и делает два удара")
stats(health_points, mana, current_weapon,weapon_stats)