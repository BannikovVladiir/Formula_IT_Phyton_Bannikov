# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, arg=","):
    set_1 = set(str_1.split(arg))
    set_2 = set(str_2.split(arg))
    group = list(set_1.intersection(set_2))
    group.sort()
    return group

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, "|")