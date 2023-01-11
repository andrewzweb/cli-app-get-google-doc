import pandas as pd
import io
import csv


class ParseRawSource:

    def __init__(self, source: str):
        self.source = source

    def to_dict(self) -> list:
        csv_raw = io.StringIO(self.source)
        df = pd.read_csv(csv_raw)
        return df.to_dict('records')

    @staticmethod
    def create_csv_from_list(csvdata):
        output = io.StringIO()
        fields = [x for x in csvdata[0].keys()]
        writer = csv.DictWriter(output, fieldnames=fields, delimiter=',')
        writer.writeheader()
        writer.writerows(csvdata)
        return str(output.getvalue())
