# TODO решите задачу
import json
def task() -> float:
    sum = 0
    with open ("input.json") as file:
        reader = json.load(file)
        for i in reader:
            sum += i["score"] * i["weight"]
    return round(sum,3)

print(task())
