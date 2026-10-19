def resize(ba, size):
    if len(ba) > size:
        del ba[size:]
    else:
        ba += b'\0' * (size - len(ba))
