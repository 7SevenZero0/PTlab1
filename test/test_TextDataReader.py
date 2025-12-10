# -*- coding: utf-8 -*-
import pytest
from src.YamlDataReader import YamlDataReader
from Types import DataType
import tempfile
import os

class TestYamlDataReader:

    @pytest.fixture()
    def sample_yaml_file(self):
        content = """
Иванов Иван Иванович:
  математика: 80
  литература: 76
  программирование: 100
Петров Петр Петрович:
  математика: 61
  литература: 80
  программирование: 78
  химия: 97
"""
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".yaml")
        tmp_file.write(content.encode("utf-8"))
        tmp_file.close()
        yield tmp_file.name
        os.unlink(tmp_file.name)

    def test_read_yaml(self, sample_yaml_file):
        reader = YamlDataReader()
        data = reader.read(sample_yaml_file)
        assert "Иванов Иван Иванович" in data
        assert len(data["Иванов Иван Иванович"]) == 3
