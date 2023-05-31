import _thread as thread
import random
import sys
import threading
import time
import tracemalloc
from itertools import chain

from solution import Algorithm


class AlgorithmError(RuntimeError):
    pass


def get_none():
    return ()


def timeout_function(fn, secs, args=()):
    def cdquit():
        thread.interrupt_main()  # raises KeyboardInterrupt

    timer = threading.Timer(secs, cdquit)
    timer.start()
    try:
        result = fn(*args)
    finally:
        timer.cancel()
    return result


def test_append():
    a = Algorithm()
    a.append("a")
    a.append("b")
    a.append("c")
    return a


def test_pop():
    a = Algorithm()
    a.append("a")
    a.append("b")
    a.append("c")

    if a.pop("a") != "a":
        raise AlgorithmError("'a' not popped")
    if a.pop("c") != "c":
        raise AlgorithmError("'c' not popped")
    if a.pop("b") != "b":
        raise AlgorithmError("'b' not popped")
    return a


def test_check():
    a = Algorithm()
    if a.check("a"):
        raise AlgorithmError("check('a') returned true")
    a.append("a")
    if not a.check("a"):
        raise AlgorithmError("check('a') returned false")
    return a


def test_len():
    a = Algorithm()
    a.append("a")
    a.append("b")
    a.append("c")

    if len(a) != 3:
        raise AlgorithmError("len not 3")

    a.pop("a")
    if len(a) != 2:
        raise AlgorithmError("size did not decrease after pop a")

    a.pop("c")
    if len(a) != 1:
        raise AlgorithmError("size did not decrease after pop c")

    a.pop("b")
    if len(a) != 0:
        raise AlgorithmError("size did not decrease after pop b")
    return a


def check_non_existing_elements():
    a = Algorithm()
    a.append("a")
    a.append("b")
    a.append("c")

    if a.check("d"):
        raise AlgorithmError("'d' found")
    if a.pop("e") != "":
        raise AlgorithmError("'e' popped (should not exist)")
    if len(a) != 3:
        raise AlgorithmError("size changed after popping a non-existing element")
    return a


def insert_unique():
    a = Algorithm()
    for i in range(10_000):
        a.append(f"element: {i}")
    if len(a) != 10_000:
        raise AlgorithmError("len() not 10k")

    if not a.check("element: 1234"):
        raise AlgorithmError("check for 'element: 1234' failed")
    if a.check("non element"):
        raise AlgorithmError("check got true for 'non element'")

    if a.pop("element: 1234") != "element: 1234" or len(a) != 9999:
        raise AlgorithmError("'element: 1234' not popped")
    if a.pop("element: 1234") != "" or len(a) != 9999:
        raise AlgorithmError("'element: 1234' popped again")
    return a


def insert_with_repeats():
    a = Algorithm()
    for i in range(5_000):
        a.append(f"element: {i}")
    for i in range(5_000):
        a.append(f"element: {i}")
    if len(a) != 10_000:
        raise AlgorithmError("len() not 10k")

    if not a.check("element: 1234"):
        raise AlgorithmError("check for 'element: 1234' failed")
    if a.check("non element"):
        raise AlgorithmError("check got true for 'non element'")

    if a.pop("element: 1234") != "element: 1234" or len(a) != 9999:
        raise AlgorithmError("'element: 1234' not popped")
    if a.pop("element: 1234") != "element: 1234" or len(a) != 9998:
        raise AlgorithmError("'element: 1234' not popped again")
    return a


def insert_500k_unique():
    a = Algorithm()
    for i in range(500_000):
        a.append(f"element: {i}")
    if len(a) != 500_000:
        raise AlgorithmError("len() not 500k")

    if not a.check("element: 1234"):
        raise AlgorithmError("check for 'element: 1234' failed")
    if a.check("non element"):
        raise AlgorithmError("check got true for 'non element'")

    if a.pop("element: 187654") != "element: 187654" or len(a) != 499_999:
        raise AlgorithmError("'element: 187654' not popped")
    return a


def insert_500k_with_repeats():
    a = Algorithm()
    for i in range(250_000):
        a.append(f"element: {i}")
    for i in range(250_000):
        a.append(f"element: {i}")
    if len(a) != 500_000:
        raise AlgorithmError("len() not 500k")

    if not a.check("element: 1234"):
        raise AlgorithmError("check for 'element: 1234' failed")
    if a.check("non element"):
        raise AlgorithmError("check got true for 'non element'")

    if a.pop("element: 123456") != "element: 123456" or len(a) != 499_999:
        raise AlgorithmError("'element: 123456' not popped")
    if a.pop("element: 123456") != "element: 123456" or len(a) != 499_998:
        raise AlgorithmError("'element: 123456' not popped again")
    return a


def check_1M_unique_elements(a):
    # depends on setup_check_1M_unique_elements
    if len(a) != 1_000_000:
        raise AlgorithmError("len() not 1M")

    for i in range(random.randint(0, 500), 1_000_000, 500):  # existing element
        if not a.check(f"element: {i%1_000_000}"):
            raise AlgorithmError(f"'element: {i}' not found")
    for i in range(random.randint(0, 1000), 1_000_000, 1000):  # non-existing
        if a.check(f"not element: {i}"):
            raise AlgorithmError(f"'not element: {i}' was found")
    return a


def setup_check_1M_unique_elements():
    sys.stdout.write(
        f"__. \033[34m?\033[0m Running setup for check_1M_unique_elements...\r"
    )
    sys.stdout.flush()

    a = Algorithm()
    for i in range(1_000_000):
        a.append(f"element: {i}")
    if len(a) != 1_000_000:
        raise AlgorithmError("len() not 1M")

    sys.stdout.write(" " * 120 + "\r")
    sys.stdout.flush()
    return (a,)


def check_5M_unique_elements_str_number_only(a, start, end, step):
    # depends on setup_check_5M_unique_elements_str_number_only
    factor = 50
    if len(a) != 5_000_000:
        raise AlgorithmError("len() not 5M", len(a))

    for i in range(start, end // factor, step):  # existing element
        if not a.check(f"{i}"):
            raise AlgorithmError(f"'{i}' not found")

    false_positives = 0
    for i in range(start + 1, end // factor, step):  # existing element
        if a.check(f"{i}"):
            false_positives += 1
    if false_positives > 5_000_000 // factor * 0.001:
        raise AlgorithmError(f"Too many false positives: {false_positives}")

    sys.stdout.write(" " * 47 + f"(fp={false_positives})" + "\r")
    return a


def setup_check_5M_unique_elements_str_number_only():
    s = "__. \033[34m?\033[0m Running setup for check_5M_unique_elements_str_number_only... ({})\r"

    a = Algorithm()
    if not hasattr(a, "set_check_mode"):
        raise AlgorithmError("set_check_mode() not implemented")
    getattr(a, "set_check_mode")(1)

    start = 0  # random.randint(0, 500)
    step = 2  # random.randint(300, 500)
    end = 5_000_000 * step + start
    for i in range(start, end, step):
        if (i - start) % (step * 10000) == 0:
            sys.stdout.write(s.format(f"{int(i/end*100)}%"))
            sys.stdout.flush()
        a.append(f"{i}")

    sys.stdout.write(" " * 120 + "\r")
    sys.stdout.flush()
    return (a, start, end, step)


def check_100k_big_elements_any_str(a, start, end, step):
    # depends on setup_check_100k_big_elements_any_str
    factor = 10
    if len(a) != 100_000:
        raise AlgorithmError("len() not 5M", len(a))

    for i in range(start, end // factor, step):  # existing element
        if not a.check(f"big element {i} {'a'*10000}"):
            raise AlgorithmError(f"'big element {i} {'a'*10000}' not found")

    false_positives = 0
    for i in range(start + 1, end // factor, step):  # existing element
        if a.check(f"big element {i} {'a'*10000}"):
            false_positives += 1
    if false_positives > 100_000 // factor * 0.01:
        raise AlgorithmError(f"Too many false positives: {false_positives}")

    sys.stdout.write(" " * 38 + f"(fp={false_positives})" + "\r")
    return a


def setup_check_100k_big_elements_any_str():
    s = "__. \033[34m?\033[0m Running setup for check_100k_big_elements_any_str... ({})\r"

    a = Algorithm()
    if not hasattr(a, "set_check_mode"):
        raise AlgorithmError("set_check_mode() not implemented")
    getattr(a, "set_check_mode")(2)

    start = 0  # random.randint(0, 500)
    step = 2  # random.randint(300, 500)
    end = 100_000 * step + start
    for i in range(start, end, step):
        if (i - start) % (step * 1000) == 0:
            sys.stdout.write(s.format(f"{int(i/end*100)}%"))
            sys.stdout.flush()
        a.append(f"big element {i} {'a'*20000}")

    sys.stdout.write(" " * 120 + "\r")
    sys.stdout.flush()
    return (a, start, end, step)


def timedout_test():
    for i in range(10):
        time.sleep(0.5)


def run_tests(
    n=1000, only=None, timeout=1, max_mem_mb=200, hide_reason=False, ignore_skip=False
) -> int:
    tests_with_timeout = [
        test_append,
        test_len,
        test_check,
        test_pop,
        check_non_existing_elements,
        insert_unique,
        insert_with_repeats,
        insert_500k_unique,
        insert_500k_with_repeats,
        check_1M_unique_elements,
        check_5M_unique_elements_str_number_only,
        check_100k_big_elements_any_str,
    ]
    skip = [
        check_5M_unique_elements_str_number_only,
        check_100k_big_elements_any_str,
    ]

    err_count = 0
    if only is not None and only not in [t.__name__ for t in tests_with_timeout]:
        t = globals()[only]
        err_count += run_this_unit_test(only, n, timeout, max_mem_mb, hide_reason, 10, t)

    for i, t in enumerate(tests_with_timeout):
        if only != t.__name__ and t in skip and not ignore_skip:
            continue
        if only is not None and only != t.__name__:
            continue
        try:
            err_count += run_this_unit_test(only, n, timeout, max_mem_mb, hide_reason, i, t)
        except StopEarlier:
            break

    return err_count


class StopEarlier(Exception):
    pass


def run_this_unit_test(only, n, timeout, max_mem_mb, hide_reason, i, t) -> bool:
    reason = None
    if only is not None and t.__name__ != only:
        return True
    if only is None and i >= n:
        raise StopEarlier
    try:
        args = get_none
        tracemalloc.start()
        try:
            args = globals().get(f"setup_{t.__name__}", get_none)()
            _ = timeout_function(t, timeout, args=args)
        except Exception:
            raise
        finally:
            _, peak = tracemalloc.get_traced_memory()
            if peak > max_mem_mb * 10**6:
                raise AlgorithmError(
                    f"Max memory usage exceeded {max_mem_mb}MB ({peak / 10**6:.1f} MB)"
                )
            tracemalloc.stop()

    except KeyboardInterrupt:
        out = f"\033[91m✘\033[0m {t.__name__}"
        reason = f"(timeout)"
    except AlgorithmError as e:
        out = f"\033[91m✘\033[0m {t.__name__}"
        reason = f"FAILED: {e}"
    except Exception as e:
        out = f"\033[91m✘\033[0m {t.__name__}"
        reason = f"(exception {e.__class__}: {e})"
    else:
        out = f"\033[92m✔\033[0m {t.__name__}"

    if not hide_reason and reason is not None:
        out += f" {reason}"
    sys.stdout.write("" * 180 + "\r")
    sys.stdout.flush()
    print(f"{i+1:02d}. {out}")
    return bool(reason)

def main():
    return run_tests(7, hide_reason=True)
    # return run_tests(7)
    # return run_tests()
    # return run_tests(only="check_1M_unique_elements")
    # return run_tests(only="check_5M_unique_elements_str_number_only")
    # return run_tests(ignore_skip=True)


if __name__ == "__main__":
    raise SystemExit(main())
