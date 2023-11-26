# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    spis = []
    with open (INPUT_FILENAME, "r") as file_in:
        reader = csv.DictReader(file_in, delimiter=",", quotechar="\n")
        with open(OUTPUT_FILENAME, "w") as file_ou:
            for i in reader:
                spis.append(i)
            json.dump(spis, file_ou, indent=4)

    # TODO считать содержимое csv файла

    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
            
