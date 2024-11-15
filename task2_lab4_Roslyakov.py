import json
import csv

# Определяем имя входного файла
INPUT_FILENAME = "input_task2.csv"
# Определяем имя выходного файла
OUTPUT_FILENAME = "output.json"


# Основная функция задачи
def task() -> None:
    # Открываем входной CSV файл для чтения
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # Считываем данные из CSV и конвертируем их в список словарей
        data = [row for row in reader]

    # Открываем выходной файл JSON для записи
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as j:
        # Записываем данные в JSON формате с отступами
        json.dump(data, j, ensure_ascii=False, indent=4)


# Проверка имени модуля
if __name__ == '__main__':
    # Нужно для проверки
    task()

    # Открываем выходной JSON файл для проверки результата
    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")

