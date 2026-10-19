# Görev b:4.4.23: Parser konum bilgisini yorumla

## Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`compile("x =", "ornek.py", "exec")` çağrısını try/except SyntaxError ile yakala. msg, filename, lineno, offset, text, end_lineno ve end_offset alanlarını raporla. İlk satırın neden lineno=1 olduğunu ve str(e) ile alanların aynı veri olmadığını açıkla.

## Geçiş ölçütleri

- [ ] Hata derleme sırasında oluşur, dosya adı ornek.py ve satır 1 olur.
- [ ] Konum metadatası raporlanır; tam hata mesajının sürümler arasında aynı olması şart koşulmaz.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
