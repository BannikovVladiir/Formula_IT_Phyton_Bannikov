# TODO  Напишите функцию count_letters
def count_letters(str_):
    str_ = str_.lower()
    list_index = []
    list_letter = []
    for i in str_:
        if i.isalpha():
            list_letter.append(i)
    for j in list_letter:
        number = list_letter.count(j)
        list_index.append(number)
    dict_letter = dict(zip(list_letter, list_index))
    return dict_letter


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_):
    sum_frequency = sum(dict_.values())
    for j in dict_:
        dict_[j] = format(round(dict_[j]/sum_frequency, 2),".2f")
    for letter, frequency in dict_.items():
        print(letter, frequency, sep=": ")

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letters = count_letters(main_str)
calculate_frequency(letters)