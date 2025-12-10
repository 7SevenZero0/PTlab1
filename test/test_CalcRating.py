# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcRating import CalcRating
import pytest

RatingsType = dict[str, float]


class TestCalcRating:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "РђР±СЂР°РјРѕРІ РџРµС‚СЂ РЎРµСЂРіРµРµРІРёС‡":
                [
                    ("РјР°С‚РµРјР°С‚РёРєР°", 80),
                    ("СЂСѓСЃСЃРєРёР№ СЏР·С‹Рє", 76),
                    ("РїСЂРѕРіСЂР°РјРјРёСЂРѕРІР°РЅРёРµ", 100)
                ],

            "РџРµС‚СЂРѕРІ РРіРѕСЂСЊ Р’Р»Р°РґРёРјРёСЂРѕРІРёС‡":
                [
                    ("РјР°С‚РµРјР°С‚РёРєР°", 61),
                    ("СЂСѓСЃСЃРєРёР№ СЏР·С‹Рє", 80),
                    ("РїСЂРѕРіСЂР°РјРјРёСЂРѕРІР°РЅРёРµ", 78),
                    ("Р»РёС‚РµСЂР°С‚СѓСЂР°", 97)
                ]
        }

        rating_scores: RatingsType = {
            "РђР±СЂР°РјРѕРІ РџРµС‚СЂ РЎРµСЂРіРµРµРІРёС‡": 85.3333,
            "РџРµС‚СЂРѕРІ РРіРѕСЂСЊ Р’Р»Р°РґРёРјРёСЂРѕРІРёС‡": 79.0000
        }

        return data, rating_scores

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      RatingsType]) -> None:

        calc_rating = CalcRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, RatingsType]) -> None:

        rating = CalcRating(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]
