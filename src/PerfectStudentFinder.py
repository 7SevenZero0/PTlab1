# -*- coding: utf-8 -*-
from Types import DataType
from CalcRating import CalcRating


class PerfectStudentFinder:
    """
    Класс для нахождения студента, имеющего минимум 76 баллов по >=3 дисциплинам.
    """

    def __init__(self, data: DataType) -> None:
        self.data = data

    def find_student(self) -> str | None:
        for student, subjects in self.data.items():
            high_scores = [score for _, score in subjects if score >= 76]
            if len(high_scores) >= 3:
                return student
        return None
