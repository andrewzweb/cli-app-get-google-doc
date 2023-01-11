import json
import pytest
from run import Worker

url_doc = "https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view\?usp\=sharing"


class MockCLI:
    def to_dict(self):
        return {
            "url": url_doc,
            "fields": ["date", "clicks"]
        }


def test_worker_return_json(mocker):
    mocker.patch("cli.cli.CLIArgs",
        side_effect=MockCLI)

    raw_json = Worker().execute()
    data = json.loads(raw_json)

    assert "data" in data
    assert "date" in data["data"][0]
    assert "clicks" in data["data"][0]
