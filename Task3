def unique_in_order(values):
    seen = set()
    result = []
    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def word_frequencies(text):
    counts = {}
    for word in text.split():
        cleaned = word.strip('.,:;!?')
        if cleaned:
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts

def top_k(frequencies, k):
    return sorted(frequencies.items(), key=lambda pair: (-pair[1], pair[0]))[:k]

def transpose(matrix):
    if not matrix or not matrix[0]:
        return []
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

def invert(mapping):
    inverted = {}
    for key, value in mapping.items():
        inverted.setdefault(value, []).append(key)
    for val in inverted:
        inverted[val].sort()
    return inverted

def common_elements(first, second):
    return set(first) & set(second)

def group_by_length(words):
    grouped = {}
    for word in words:
        grouped.setdefault(len(word), []).append(word)
    return grouped

class Bag:
    def __init__(self, items=()):
        self._counts = {}
        self._total = 0
        for item in items:
            self.add(item)

    def add(self, item):
        self._counts[item] = self._counts.get(item, 0) + 1
        self._total += 1

    def remove(self, item):
        if item not in self._counts:
            raise KeyError(f"{item!r} not in Bag")
        self._counts[item] -= 1
        self._total -= 1
        if self._counts[item] == 0:
            del self._counts[item]

    def count(self, item):
        return self._counts.get(item, 0)

    def distinct(self):
        return set(self._counts.keys())

    def __len__(self):
        return self._total

    def __contains__(self, item):
        return item in self._counts

    def __iter__(self):
        for item, cnt in self._counts.items():
            for _ in range(cnt):
                yield item

    def __eq__(self, other):
        if not isinstance(other, Bag):
            return NotImplemented
        return self._counts == other._counts

    def __repr__(self):
        return f"Bag({sorted(self)!r})"

def countdown(n):
    while n > 0:
        yield n
        n -= 1

def chunks(values, size):
    if size <= 0:
        raise ValueError("Chunk size must be greater than 0")
    def _generator():
        for i in range(0, len(values), size):
            yield values[i : i + size]
    return _generator()
