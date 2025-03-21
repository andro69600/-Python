import random
import time
dugeon_level=1

class Weapon:
    def __init__(self, damage, mana_usage, ability):
        self.damage = damage
        self.mana_usage = mana_usage
        self.ability = ability


magic_staff = Weapon(damage=40, mana_usage=95, ability="посох")
bow = Weapon(damage=20, mana_usage=100, ability="лук")
sword = Weapon(damage=1000, mana_usage=90, ability="меч")


class Monster:
    def __init__(self, name, health, mana, damage):
        self.name = name
        self.health = health
        self.mana = mana
        self.damage = damage
undead = Monster("Нежить", 100, 40, 25)
giant_spider = Monster("Гигантский паук", 200, 60, 30)
king_of_skelets = Monster("Король скелетов", 300, 70, 35)
dragon = Monster('Дракон',500, 100, 50)
current_weapon = None
health_points = 100
mana = 100
defense = 0
dodge = 0
print("Выберите свой класс, за который будете играть (1 - это воин, 2 - это лучник, 3 - это маг):")
player_class = int(input())
if player_class == 1:
    you_class = "Воин"
    current_weapon = sword
    health_points = 150
    defense = 30
    dodge = 0
elif player_class == 2:
    you_class = "Лучник"
    current_weapon = bow
    health_points = 90
    defense = 20
    dodge = 50
elif player_class == 3:
    you_class = "Маг"
    current_weapon = magic_staff
    health_points = 100
    defense = 10
    dodge = 10
print("Сюжет:""\n"
      "Был один человек, который решил отправиться в поземелье, в котором по легенде находился артефакт""\n"
      "Но на входе в подземелье, его встретили люди, которые сказали ему, что там находятся монстры""\n"
      "И решил он выбрать, кем он будет, дабы не помереть в нем""\n"
      f"Выбрал он свой класс, это был {you_class}.""\n"
      "И отправился он в подземелье...")
time.sleep(2)

def stats():
    print(f"Ваша статистика:\n"
          f"{health_points} очков здоровья\n"
          f"{mana} очков маны\n"
          f"{current_weapon.ability} в снаряжении\n"
          f"{dodge} текущее кол-во шанса уворота\n"
          f"{defense} текущее кол-во защиты (10 защиты = на 5 урона меньше)")
    print("Что по способностям?"'\n'
          "Маг - Магический Щит - дает 5 уворота навсегда и дает 100 шанс увернуться от следующего удара"'\n'
          "Лучник - Тройной выстрел - дает 5 урона навсегда, делает следующий выстрел тройным(тоесть урон умножили на 3, добавленный урон в счет идет)"'\n'
          "Воин - Удар с размаха - дает 100 защиты на следующий ход (50 урона не пройдет по вам) и делает два удара"'\n')

stats()

monsters = [undead, giant_spider,king_of_skelets ]
current_monster = random.choice(monsters)
print(f'Ваш противник: {current_monster.name}, его здоровье: {current_monster.health}, его мана: {current_monster.mana}, его урон: {current_monster.damage}.')
while health_points > 0 and current_monster.health > 0:
        print('Что вы делаете?\n1 - Атака\n2 - Подлечиться\n3 - Использовать спецатаку')
        action = int(input())
        if action == 1:
            current_monster.health -= current_weapon.damage
            print(f'Вы атаковали {current_monster.name}! Его здоровье: {current_monster.health}.')
            damage_taken = max(0, current_monster.damage - defense)
            health_points -= damage_taken
            print(
                f'{current_monster.name} атакует! Вы потеряли {damage_taken} здоровья. Текущее здоровье: {health_points}.')
        if action == 2:
            health_points += 30
            print(f'Вы подлечились {health_points+30}')
        if action == 3:
            current_monster.health -= current_weapon.damage
            print(f'Вы атаковали {current_monster.name}! Его здоровье: {current_monster.health}.')
            damage_taken = max(0, current_monster.damage - defense)
            health_points -= damage_taken
            print(
                f'{current_monster.name} атакует! Вы потеряли {damage_taken} здоровья. Текущее здоровье: {health_points}.')
            if current_monster.health <= 0:
                print(f'Вы победили {current_monster.name}!')
                dugeon_level += 1
                break
            if health_points <= 0:
                print("Вы проиграли!")
                break
monsters = [undead, giant_spider,king_of_skelets ]
current_monster = random.choice(monsters)
print(f'Ваш противник: {current_monster.name}, его здоровье: {current_monster.health}, его мана: {current_monster.mana}, его урон: {current_monster.damage}.')
while health_points > 0 and current_monster.health > 0:
        print('Что вы делаете?\n1 - Атака\n2 - Подлечиться\n3 - Использовать спецатаку')
        action = int(input())
        if action == 1:
            current_monster.health -= current_weapon.damage
            print(f'Вы атаковали {current_monster.name}! Его здоровье: {current_monster.health}.')
            damage_taken = max(0, current_monster.damage - defense)
            health_points -= damage_taken
            print(
                f'{current_monster.name} атакует! Вы потеряли {damage_taken} здоровья. Текущее здоровье: {health_points}.')
        if action == 2:
            health_points += 30
            print(f'Вы подлечились {health_points+30}')
        if action == 3:
            current_monster.health -= current_weapon.damage
            print(f'Вы атаковали {current_monster.name}! Его здоровье: {current_monster.health}.')
            damage_taken = max(0, current_monster.damage - defense)
            health_points -= damage_taken
            print(
                f'{current_monster.name} атакует! Вы потеряли {damage_taken} здоровья. Текущее здоровье: {health_points}.')
            if current_monster.health <= 0:
                print(f'Вы победили {current_monster.name}!')
                dugeon_level += 1
                break
            if health_points <= 0:
                print("Вы проиграли!")
                break
print(f'Ваш противник: {dragon}, его здоровье: {dragon.health}, его мана: {dragon.mana}, его урон: {dragon.damage}.')
while health_points > 0 and dragon.health > 0:
        print('Что вы делаете?\n1 - Атака\n2 - Подлечиться\n3 - Использовать спецатаку')
        action = int(input())
        if action == 1:
            current_monster.health -= current_weapon.damage
            print(f'Вы атаковали {dragon.name}! Его здоровье: {dragon.health}.')
            damage_taken = max(0, dragon.damage - defense)
            health_points -= damage_taken
            print(
                f'{current_monster.name} атакует! Вы потеряли {damage_taken} здоровья. Текущее здоровье: {health_points}.')
        if action == 2:
            health_points += 30
            print(f'Вы подлечились {health_points+30}')
        if action == 3:
            current_monster.health -= current_weapon.damage
            print(f'Вы атаковали {current_monster.name}! Его здоровье: {current_monster.health}.')
            damage_taken = max(0, current_monster.damage - defense)
            health_points -= damage_taken
            print(
                f'{current_monster.name} атакует! Вы потеряли {damage_taken} здоровья. Текущее здоровье: {health_points}.')
            if current_monster.health <= 0:
                print(f'Вы победили {current_monster.name}!')
                dugeon_level += 1
                break
            if health_points <= 0:
                print("Вы проиграли!")
                break
print('вы нашли легендарный артефакт')