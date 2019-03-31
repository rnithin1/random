import math

class Integers:
    def __init__(self):
        self.llimit = float("-inf")
        self.ulimit = float("inf")

    def __getitem__(self, x):
        assert type(x) == int \
                and x >= self.llimit \
                and x < self.ulimit
        return x

    def __contains__(self, x):
        return self.llimit <= x < self.ulimit \
                and type(x) == int

    def succ(self, x):
        assert type(x) == int \
                and x >= self.llimit \
                and x < self.ulimit
        return x + 1

    def prev(self, x):
        assert type(x) == int \
                and x >= self.llimit \
                and x < self.ulimit
        if x == self.llimit:
            raise ValueError("prev(" 
                    + self.llimit + ") is undefined")
        return x - 1
    
    def subset(self, x, y):
        assert type(x) == int \
                and x >= self.llimit \
                and x < self.ulimit

        assert type(y) == int \
                and y >= self.llimit \
                and y < self.ulimit

        n = Integers()
        n.llimit = max(float("-inf"), x)
        n.ulimit = min(float("inf"), max(float("-inf"), y))
        return n
Z = Integers()

class Naturals(Integers):
    def __init__(self):
        self.llimit = 0
        self.ulimit = float("inf")

    def subset(self, x, y=None):
        assert type(x) == int \
                and x >= self.llimit \
                and x < self.ulimit

        if y != None:
            assert type(y) == int \
                    and y >= self.llimit \
                    and y < self.ulimit
        if y == None:
            n = Naturals()
            n.llimit = max(0, x)

        else:
            n = Naturals()
            n.llimit = max(0, x)
            n.ulimit = min(float("inf"), max(0, y))
        return n
N = Naturals()

# Conway Pair
class Pair:
    def __init__(self, L=None, R=None):
        self._L = L
        self._R = R
        self._value = self.value()

    def __repr__(self):
        return "{ " + str(self._L) \
                + " | " + str(self._R) \
                + " }"

    def __cmp__(self, other):
        return min(1, max(self._value - other, -1))

    def __eq__(self, other):
        return isinstance(other, Pair) \
                and self._value == other._value

    def __add__(self, other):
        pass

    def __mul__(self, other):
        pass
    
    def __sub__(self, other):
        pass
    
    def __div__(self, other):
        pass

    def negate(self):
        self._L = -self._R
        self._R = -self._L
        self._value = -self._value

    def value(self):
        # Construct zero
        if self._L == None and self._R == None:
            return 0

        # Construct N
        if self._L in N and self._R == None:
            return N.succ(self._L)

        # Construct Z
        if self._R in Z and self._L == None:
            return Z.prev(self._R)

        # After everything is constructed
        return (self._R + self._L) / 2

class Rationals:
    def __init__(self):
        self.llimit = float("-inf")
        self.ulimit = float("inf")

    def __getitem__(self, x):
        assert x >= self.llimit \
            and x < self.ulimit
        return x

    def __contains__(self, x):
        return self.llimit <= x < self.ulimit

    def succ(self, x):
        raise NotImplementedError()

    def prev(self, x):
        raise NotImplementedError()

    def subset(self, x, y):
        assert x >= self.llimit \
                and x < self.ulimit

        assert y >= self.llimit \
                and y < self.ulimit

        n = Rationals()
        n.llimit = max(float("-inf"), x)
        n.ulimit = min(float("inf"), max(float("-inf"), y))
        return n

    def pair(self, L, R):
        return Pair(L, R)
Q = Rationals()

def Dyadic(Rationals):
    def __init__(self):
        self.llimit = float(1)
        self.ulimit = float("inf")

    def __getitem__(self, x):
        assert math.log(x) >= self.llimit \
            and math.log(x) < self.ulimit
        return 2**-x

    def __contains__(self, x):
        return -math.log(x) / math.log(2) in N

    def succ(self, x):
        return 2**-(-math.log(x)/math.log(2) + 1)

    def prev(self, x):
        assert x != 1
        return 2**-(-math.log(x)/math.log(2) - 1)

    def subset(self, x, y=None):
        assert x >= self.llimit \
            and x < self.ulimit

        if y != None:
            assert y >= self.llimit \
                and y < self.ulimit

        n = Dyadic()
        if y == None:
            n.llimit = max(float(1), x)
        else:
            n.llimit = max(float(1), x)
            n.ulimit = min(float("inf"), max(float("-inf"), y))
        return n
S = Dyadic()

class Reals:
    def __init__(self):
        self.llimit = float("-inf")
        self.ulimit = float("inf")

    def __contains__(self, x):
        return self.llimit <= x < self.ulimit
    
    def subset(self, x, y=None):
        assert x >= self.llimit \
                and x < self.ulimit

        assert y >= self.llimit \
                and y < self.ulimit

        n = Reals()
        n.llimit = max(float("-inf"), x)
        n.ulimit = min(float("inf"), max(float("-inf"), y))
        return n

    def pair(self, L, R):
        return Pair(L, R)

class SurrealPair(Pair):
    def __init__(self, L=None, R=None):
        if L == N and R == None:
            return "ω"

        if R == S and L == None:
            return "ε"

        self._L = L
        self._R = R
        self._value = self.value()

class Surreals(Reals):
    class ω:
        pass

    class ε:
        pass
