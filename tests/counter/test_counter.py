from src.counter import count_ocurrences


def test_counter():
    results_of_words = {
        "python": 1639,
        "javascript": 122,
    }
    assert count_ocurrences("src/jobs.csv", "python") == results_of_words.get(
        "python"
    )
    assert count_ocurrences(
        "src/jobs.csv", "javascript"
    ) == results_of_words.get("javascript")
    assert count_ocurrences("src/jobs.csv", "PYTHON") == results_of_words.get(
        "python"
    )
    assert count_ocurrences(
        "src/jobs.csv", "jaVAscript"
    ) == results_of_words.get("javascript")
