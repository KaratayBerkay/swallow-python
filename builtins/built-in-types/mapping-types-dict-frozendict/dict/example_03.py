class Counter(dict):
    def __missing__(self, key):
        return 0
c = Counter()
print(repr(c['red']))
c['red'] += 1
print(repr(c['red']))
