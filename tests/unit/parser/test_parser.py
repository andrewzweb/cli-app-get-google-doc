import pytest

from parser import parser as prs

persons_dict = [
    {
        "name": "Josh",
        "age": 29,
        "save": 54993.00
    },
    {
        "name": "Anna",
        "age": 18,
        "save": 11662.01
    },
    {
        "name": "Dino",
        "age": 47,
        "save": 321662.01
    }
]


def test_parser_can_parser_raw_csv():
    persons_raw_csv = prs.ParseRawSource.create_csv_from_list(persons_dict)
    parsed_persons_dict = prs.ParseRawSource(persons_raw_csv).to_dict()

    assert parsed_persons_dict == persons_dict
