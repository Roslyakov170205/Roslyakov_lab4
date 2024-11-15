import json


def calculate_weighted_sum() -> float:
    total = 0.0

    with open("input.json", "r") as file:
        data = json.load(file)

    for record in data:
        score = record.get("score", 0)
        weight = record.get("weight", 0)
        total += score * weight

    return round(total, 3)


print(calculate_weighted_sum())
