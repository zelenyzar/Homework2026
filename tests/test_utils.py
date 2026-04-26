import json
from unittest.mock import patch

from src.utils import create_objects_from_json, read_json


def test_read_json(json_test):
    with patch("builtins.open") as mock_open:
        # Аналогично: read() возвращает JSON‑строку
        mock_open.return_value.__enter__.return_value.read.return_value = json.dumps(json_test)

        assert read_json("products.json") == json_test


def test_create_objects_from_json(json_test):
    assert create_objects_from_json(json_test)[0].name == "Смартфоны"
