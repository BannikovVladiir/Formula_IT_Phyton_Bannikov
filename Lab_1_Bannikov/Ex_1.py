numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers[4] = 0
sum_numbers = sum(numbers)
len_numbers = len(numbers)
uniqe_number = sum_numbers / len_numbers
numbers[4] = uniqe_number
print("Измененный список:", numbers)
