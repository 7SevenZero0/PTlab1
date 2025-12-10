# -*- coding: utf-8 -*-
import pytest
from src.PerfectStudentFinder import PerfectStudentFinder
from Types import DataType

class TestPerfectStudentFinder:

    @pytest.fixture()
    def input_data(self) -> DataType:
        return {
            "Иванов Иван Иванович": [("математика", 80), ("русский", 76), ("программирование", 100)],
            "Петров Петр Петрович": [("математика", 61), ("русский", 80), ("программирование", 78)],
            "Сидоров Сидор Сидорович": [("математика", 90), ("русский", 92), ("литература", 95), ("физика", 100)]
        }

    def test_find_student(self, input_data):
        finder = PerfectStudentFinder(input_data)
        student = finder.find_student()
        assert student in ["Иванов Иван Иванович", "Сидоров Сидор Сидорович"]
