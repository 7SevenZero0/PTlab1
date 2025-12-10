# -*- coding: utf-8 -*-
import yaml
from DataReader import DataReader
from Types import DataType


class YamlDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        # Преобразуем YAML в DataType (словарь с ключами-студентами и списком предметов)
        for student_name, subjects in data.items():
            self.students[student_name] = [(subj, int(score)) for subj, score in subjects.items()]
        return self.students
