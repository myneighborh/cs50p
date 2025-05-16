class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 1:
            raise ValueError("Capacity must be larger than 0")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int):
            raise ValueError("Deposit must be an integer")

        if self.size + n > self.capacity:
            raise ValueError("Cannot add cookies: exceeds capacity")

        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int):
            raise ValueError("Withdraw must be an integer")

        if self.size - n < 0:
            raise ValueError("Cannot remove that many: not enough in jar.")

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
