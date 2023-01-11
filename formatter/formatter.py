import json


class Formatter:
    table = {}

    def __init__(self, table: dict, fields: list = None):
        self.fields = fields
        self.table = table

    def prepare(self) -> list:
        filtered_list = []
        for row in self.table:
            item = {}
            for cell, value in row.items():
                if cell in self.fields:
                    item[cell] = value
            filtered_list.append(item)
        return filtered_list

    def to_json(self, indent=2):
        table = self.prepare()
        return json.dumps({"data": table}, indent=indent)
