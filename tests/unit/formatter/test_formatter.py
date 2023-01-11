import json

from formatter import formatter as frm


table_example = [
    {
        "date": "2023-01-07",
        "spend": "2.45",
        "campaign": "powerbi",
     },
    {
        "date": "2023-01-03",
        "spend": "2.45",
        "campaign": "datastudio",
     },
    {
        "date": "2023-01-07",
        "spend": "0.45",
        "campaign": "tableu",
     },
    {
        "date": "2023-01-06",
        "spend": "1.45",
        "campaign": "powerbi",
     }
]

def test_make_formatter_obj():
    fields = ["date"]

    table_json = frm.Formatter(table_example, fields=fields)

    assert table_json.table == table_example
    assert table_json.fields == fields


def test_formatter_return_table_with_some_fields():
    fields = ["date"]

    table_json = frm.Formatter(table_example, fields=fields).to_json()
    table = json.loads(table_json)

    assert table
    assert "data" in table
    assert len(table['data']) == 4
    assert fields[0] in table['data'][0]


def test_formatter_get_full_table():

    table_json = frm.Formatter(table_example, fields="date").to_json()

    table = json.loads(table_json)

    assert table
    assert "data" in table
    assert len(table['data']) == 4
