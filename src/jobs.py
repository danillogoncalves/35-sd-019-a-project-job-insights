import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, mode="r", encoding="utf-8") as file:
        file_reader = csv.reader(file, delimiter=",", quotechar='"')
        headers, *data = file_reader

    new_list = []

    for row_data in data:
        new_dict = {}
        index = 0
        for header in headers:
            new_dict[header] = row_data[index]
            index += 1

        new_list.append(new_dict)

    # with open(path, mode="r", encoding="utf-8") as file:
    #     file_reader = csv.DictReader(file)
    #     new_list = list(file_reader)

    return new_list
