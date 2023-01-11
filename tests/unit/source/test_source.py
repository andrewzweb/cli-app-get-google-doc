import pytest

from source import source as src


class MockResponse:
    def __init__(self, code, text):
        self.status_code = code
        self.text = text

    def get(self, *args, **kwargs):
        return self

    def __call__(self, *args, **kwargs):
        return self


def test_create_source_google_drive_with_url():
    url = "http://test.com"

    source_manager = src.GoogleDrive(url)

    assert source_manager.source_url == url


def test_source_google_make_request_to_network(mocker):
    response_mock = MockResponse(code=200, text="fake response")
    mock = mocker.patch("source.source.requests.get", side_effect=response_mock)
    url = "https://drive.google.com/"

    src.GoogleDrive(url).get_source()

    mock.assert_called()


def test_source_google_throw_exception_when_page_not_found(mocker):
    response_mock = MockResponse(code=404, text="fake response")
    mock = mocker.patch("source.source.requests.get", side_effect=response_mock)
    url = "https://drive.google.com/"

    with pytest.raises(Exception) as exc:
        src.GoogleDrive(url).get_source()

    mock.assert_called()
