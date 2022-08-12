import os
from typing import List


class ReadFile:
    def __init__(self) -> None:
        self.enconding = 'utf-8'
    
    def read_file(self, dir_path: str) -> List:
        list_of_entries = []
        list_of_expected_results = []

        with open(os.path.abspath(os.path.join('..', os.getcwd())) + dir_path, encoding=self.enconding) as file:
            for line in file:
                entry, result = line.split("|")
                list_of_entries.append(entry.split(","))
                list_of_expected_results.append(result.strip())

        return list_of_entries, list_of_expected_results
