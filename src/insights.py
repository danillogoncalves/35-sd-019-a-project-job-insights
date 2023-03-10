from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them
    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    document = read(path)
    set_result = {job["job_type"] for job in document if job["job_type"] != ""}
    return set_result


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    document = read(path)
    set_result = {
        industry["industry"]
        for industry in document
        if industry["industry"] != ""
    }
    return set_result


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    document = read(path)
    set_result = {
        int(salaries["max_salary"])
        for salaries in document
        if salaries["max_salary"].isnumeric()
    }

    return max(set_result)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    document = read(path)
    set_result = {
        int(salaries["min_salary"])
        for salaries in document
        if salaries["min_salary"].isnumeric()
    }

    return min(set_result)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    # print("\n")
    # print(job.get("min_salary") is not None)
    # print(job.get("max_salary") is not None)
    # print(type(job.get("min_salary")) is int)
    # print(type(job.get("max_salary")) is int)
    # print(job.get("min_salary") > job.get("max_salary"))
    # print(type(salary) is int)
    # print(job.get("min_salary") >= salary <= job.get("max_salary"))
    if (
        job.get("min_salary") is not None
        and job.get("max_salary") is not None
        and type(job.get("min_salary")) is int
        and type(job.get("max_salary")) is int
        and job.get("min_salary") < job.get("max_salary")
        and type(salary) is int
    ):
        if job.get("min_salary") <= salary <= job.get("max_salary"):
            return True
        else:
            return False
    else:
        raise ValueError


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    new_job = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                new_job.append(job)
        except ValueError:
            pass

    return new_job
