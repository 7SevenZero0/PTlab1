# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.PerfectStudentFinder import PerfectStudentFinder


class TestPerfectStudentFinder:

    @pytest.fixture()
    def input_data(self) -> DataType:
        return {
            "РРІР°РЅРѕРІ РРІР°РЅ": [
                ("РјР°С‚РµРјР°С‚РёРєР°", 80),
                ("РїСЂРѕРіСЂР°РјРјРёСЂРѕРІР°РЅРёРµ", 90),
                ("Р»РёС‚РµСЂР°С‚СѓСЂР°", 76)
            ],
            "РџРµС‚СЂРѕРІ РџРµС‚СЂ": [
                ("РјР°С‚РµРјР°С‚РёРєР°", 60),
                ("РїСЂРѕРіСЂР°РјРјРёСЂРѕРІР°РЅРёРµ", 50),
                ("Р»РёС‚РµСЂР°С‚СѓСЂР°", 70)
            ]
        }

    def test_find(self, input_data: DataType) -> None:
        finder = PerfectStudentFinder(input_data)
        student = finder.find()
        assert student == "РРІР°РЅРѕРІ РРІР°РЅ"
