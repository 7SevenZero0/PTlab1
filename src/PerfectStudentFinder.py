# -*- coding: utf-8 -*-
from Types import DataType
from YamlDataReader import YamlDataReader


class PerfectStudentFinder:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def find(self) -> str | None:
        for student, subjects in self.data.items():
            high_scores = sum(1 for subj in subjects if subj[1] >= 76)
            if high_scores >= 3:
                return student
        return None
