from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    test = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert test[0].get("title") is not None
    assert test[0].get("salary") is not None
    assert test[0].get("type") is not None
