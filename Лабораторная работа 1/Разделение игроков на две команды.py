list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

amount = int(len(list_players))
half = int(amount / 2)
list_1 = list_players[:half]
list_2 = list_players[half:]
print(list_1)
print(list_2)