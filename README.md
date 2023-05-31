# Exercise for Dojo

This is an exercise where multiple answers are accepted, depending on the purpose of the solution.
The purpose is emulated with different tests.

Tests will have a timeout, so choose the right data structure and algorithm for the test.

## Install

```
git clone https://github.com/tcarreira/ex-multi-answer-dojo.git
cd ex-multi-answer-dojo
```

## Run first tests

```sh
$ python3 solution.py
01. ✘ test_append
02. ✘ test_pop
03. ✘ test_len
04. ✘ test_check
05. ✘ check_non_existing_elements
06. ✘ insert_unique
07. ✘ insert_with_repeats
```

## Solving

- open `solution.py`
- implement the class `Algorithm` based on `BootstrapAlgorithm`
- try baby steps, and check 1 test at a time
  - all tests run by calling `run_tests()`. Check its arguments.
- it is expected to have to try a different approach when tests fail


The function `run_tests()` accepts some arguments. Some examples are commented inside `solution.py`:

```py
run_tests(7, hide_reason=True) # run only the first 7 tests, and do NOT show the reason of failure
run_tests(7) # run only the first 7 tests, showing the reason of failure
run_tests() # run all default tests
run_tests(only="check_1M_unique_elements") # run only the test named "check_1M_unique_elements"
run_tests(only="check_5M_unique_elements_str_number_only")  # This is a hidden test (advanced!)
run_tests(ignore_skip=True) # run all tests, including the hidden ones

```

## List of tests

| test name                                | constraint     |
| ---------------------------------------- | -------------- |
| test_append                              | implementation |
| test_pop                                 | implementation |
| test_len                                 | implementation |
| test_check                               | implementation |
| check_non_existing_elements              | implementation |
| insert_unique                            | implementation |
| insert_with_repeats                      | implementation |
| insert_500k_unique                       | time           |
| insert_500k_with_repeats                 | time           |
| check_1M_unique_elements                 | time           |
| check_5M_unique_elements_str_number_only | memory + time  |
| check_100k_big_elements_any_str          | memory         |
