print("Здравствуй дорогой пользователь")
name = input("Введите своё имя:")
race_list = ["Эльф", "Гном", "Гоблин", "Человек"]
print(f"Я рад видеть тебя, {name}!")
race = input(f"Выбери расу среди доступных, {race_list}:").capitalize()
hp = 0
damage = 0
if race == race_list[0]:
    hp += 100
    damage += 500
elif race == race_list[1]:
    hp += 120
    damage += 550
elif race == race_list[2]:
    hp += 140
    damage += 600
elif race == race_list[3]:
    hp += 200
    damage += 650
else:
    print("Такой расы нет")
    quit()
a = ["lvl 1", "lvl 2", "lvl 3"]
for lvl in a:
    print(lvl)
    print(f"{name},hp: {hp},damage: {damage}, race: {race}")
    hp += 5
    damage += 10