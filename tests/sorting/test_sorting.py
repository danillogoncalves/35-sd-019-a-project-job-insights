from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "job_title": "Marketing",
            "min_salary": "",
            "max_salary": "",
            "date_posted": "2020-04-25",
        },
        {
            "job_title": "Senior Salesforce Developer",
            "min_salary": "44587",
            "max_salary": "82162",
            "date_posted": "2020-05-08",
        },
        {
            "job_title": "OT/ICS Systems Engineer",
            "min_salary": "122296",
            "max_salary": "148734",
            "date_posted": "2020-04-28",
        },
        {
            "job_title": "Principal, Sr. Consultant – Creative Technologist",
            "min_salary": "64829",
            "max_salary": "104769",
            "date_posted": "data-invalid",
        },
    ]

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == "148734"
    assert jobs[1]["max_salary"] == "104769"
    assert jobs[2]["max_salary"] == "82162"
    assert jobs[3]["max_salary"] == ""

    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == "44587"
    assert jobs[1]["min_salary"] == "64829"
    assert jobs[2]["min_salary"] == "122296"
    assert jobs[3]["min_salary"] == ""

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2020-05-08"
    assert jobs[1]["date_posted"] == "2020-04-28"
    assert jobs[2]["date_posted"] == "2020-04-25"
    assert jobs[3]["date_posted"] == "data-invalid"
