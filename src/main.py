import os
import re
from typing import List


def read_file() -> List:

    list_of_entries = []
    list_of_expected_results = []

    with open(os.path.abspath(os.path.join('..', os.getcwd())) + "/resource/tests.txt", encoding='utf-8') as file:
        for line in file:
            entry, result = line.split("|")
            list_of_entries.append(entry.split(","))
            list_of_expected_results.append(result.strip())

    return list_of_entries, list_of_expected_results


def main():
    print("Starting the Challenge!")
    data, expected_result = read_file()
    for item in data:
        print(item)
    print(expected_result)


if __name__ == '__main__':
    main()
