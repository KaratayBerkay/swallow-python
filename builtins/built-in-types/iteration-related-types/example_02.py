class CardDeck:
    def __iter__(self):
        yield 'three of clubs'
        yield 'ace of hearts'
print(repr(list(CardDeck())))
