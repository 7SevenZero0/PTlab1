# -*- coding: utf-8 -*-
import yaml
from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            data = yaml.safe_load(file)
            for student, subjects in data.items():
                self.students[student] = []
                for subj, score in subjects.items():
                    self.students[student].append(
                        (subj.strip(), int(score))
                    )
        return self.students
