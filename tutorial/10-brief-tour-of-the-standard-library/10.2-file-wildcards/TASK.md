# Görev 10.2: Dosya adlarını kalıpla seç

**Odak:** glob.glob ile geçerli dizindeki dosya adı kalıbı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.1](../10.1-operating-system-interface/README.md).

## Tek görev

1. Ayrı çalışma klasörüne a.py, b.py ve note.txt adlı üç dosya koy.

2. Bu klasörde glob.glob("*.py") ile gelen adları al.

3. Sonuca sıralama garantisi yüklemeden hangi iki dosyanın dahil olduğunu, note.txt dosyasının neden dışarıda kaldığını açıklayıp "*.txt" ile tekrar dene.

## Geçiş ölçütleri

- [ ] *.py sonucu a.py ve b.py adlarını; *.txt sonucu note.txt adını içeriyor.
- [ ] Sonuç kaynak kodların içeriği değil dosya adları.
- [ ] Dizin ve dosya sırasından bağımsız üyelik üzerinden doğrulama yapılmış; regex bilgisi gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
