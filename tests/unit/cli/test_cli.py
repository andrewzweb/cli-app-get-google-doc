import pytest

from cli import cli as c


class MockCLI:
    def __init__(self, url, fields=None):
        self.url = url
        self.fields = fields

    def add_argument(self, *args, **kwargs):
        pass

    def parse_args(self, *args, **kwargs):
        return self

    def __call__(self):
        return self


def test_cli_parse_args(mocker):
    mock_obj = MockCLI("http://drive.google.com/", fields="date,source")
    mock = mocker.patch("argparse.ArgumentParser", side_effect=mock_obj())

    cli = c.CLIArgs()

    mock.assert_called()
    assert cli.url == mock_obj.url
    assert cli.fields == mock_obj.fields.split(",")


def test_cli_make_exception_if_url_wrong(mocker):
    url_wrong = "http://habbibi.com/"
    mock_obj = MockCLI(url_wrong, fields="date,source")
    mock = mocker.patch("argparse.ArgumentParser", side_effect=mock_obj())

    with pytest.raises(Exception) as exc:
        cli = c.CLIArgs()

    mock.assert_called()


def test_cli_to_dict(mocker):
    url = "http://drive.google.com/"
    fields = ["date", "source"]
    mock_obj = MockCLI(url, fields=",".join(fields))
    mock = mocker.patch("argparse.ArgumentParser", side_effect=mock_obj())

    query_dict = c.CLIArgs().to_dict()

    mock.assert_called()
    assert query_dict['url'] == url
    assert query_dict['fields'] == fields
