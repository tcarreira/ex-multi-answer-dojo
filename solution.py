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

    return run_tests(7, hide_reason=True)
    # return run_tests(7)
    # return run_tests()
    # return run_tests(only="check_1M_unique_elements")
    # return run_tests(only="check_5M_unique_elements_str_number_only")
    # return run_tests(ignore_skip=True)


if __name__ == "__main__":
    raise SystemExit(main())
