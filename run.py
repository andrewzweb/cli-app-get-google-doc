from cli import cli
from source import source as src
from formatter import formatter as frm
from parser import parser as prs


class Worker:
    def __init__(self):
        query = cli.CLIArgs().to_dict()
        table_source = src.GoogleDrive(query["url"]).get_source()
        table = prs.ParseRawSource(table_source).to_dict()
        data = frm.Formatter(table, query["fields"]).to_json()
        self.data = data

    def execute(self):
        return self.data


if __name__ == "__main__":
    data = Worker().execute()
    print(data)
