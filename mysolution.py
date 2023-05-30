################################################################################
# Start Solutions one at a Time
################################################################################
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


class Algorithm0_1(BootstrapAlgorithm):
    def __init__(self):
        self.db = []

    def append(self, s: str) -> None:
        self.db.append(s)


class Algorithm0_2(BootstrapAlgorithm):
    def __init__(self):
        self.db = []

    def append(self, s: str) -> None:
        self.db.append(s)

    def pop(self, s: str) -> str:
        if s not in self.db:
            return ""
        return self.db.pop(self.db.index(s))


class Algorithm0_3(BootstrapAlgorithm):
    def __init__(self):
        self.db = []

    def append(self, s: str) -> None:
        self.db.append(s)

    def pop(self, s: str) -> str:
        if s not in self.db:
            return ""
        return self.db.pop(self.db.index(s))

    def __len__(self) -> int:
        return len(self.db)


class Algorithm0_4(BootstrapAlgorithm):
    def __init__(self):
        self.db = []

    def append(self, s: str) -> None:
        self.db.append(s)

    def pop(self, s: str) -> str:
        if s not in self.db:
            return ""
        return self.db.pop(self.db.index(s))

    def __len__(self) -> int:
        return len(self.db)

    def check(self, s: str) -> bool:
        return s in self.db


################################################################################
# End of some Solutions
################################################################################
