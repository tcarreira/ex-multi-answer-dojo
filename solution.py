#!/usr/bin/env python3
from mysolution import *


class BootstrapAlgorithm:
    def __init__(self):
        self.db = None
        ...

    def append(self, s: str) -> None:
        raise NotImplementedError

    def check(self, s: str) -> bool:
        raise NotImplementedError

    def pop(self, s: str) -> str:  # return "" if not found
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


class Algorithm(BootstrapAlgorithm):
    ...


def main():
    from solution_test import run_tests

    run_tests(7, hide_reason=True)  # run only the first 7 tests, and do NOT show the reason of failure
    # run_tests(7) # run only the first 7 tests, showing the reason of failure
    # run_tests() # run all default tests
    # run_tests(only="check_1M_unique_elements") # run only the test named "check_1M_unique_elements"
    # run_tests(only="check_5M_unique_elements_str_number_only")  # This is a hidden test (advanced!)
    # run_tests(ignore_skip=True) # run all tests, including the hidden ones


if __name__ == "__main__":
    main()
