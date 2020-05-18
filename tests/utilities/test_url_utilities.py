from utilities.url_utils import load_urls_from_file


def test_load_file():
    test_urls = load_urls_from_file("input.txt")
    assert (len(test_urls) == 1)
