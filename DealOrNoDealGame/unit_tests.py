def check_if_cases_unique_values(cases: dict) -> None:
    """
    Use assertions to determine if any two values in the dict keys are the same.
    """

    for i in range(len(cases.values())):
        try:
            assert cases[i] != cases[i + 1]
        except KeyError:
            assert cases[i] != cases[i - 1]