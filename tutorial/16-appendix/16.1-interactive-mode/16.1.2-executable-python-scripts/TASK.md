# Görev 16.1.2: Çalıştırılabilir betiğin başlığını doğrula

**Odak:** Shebang konumu, PATH, yürütme izni ve Unix/Windows farkı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:16.1.1](../16.1.1-error-handling/README.md).
- Ön bilgi: [t:2.2.1](../../../02-using-the-python-interpreter/2.2-the-interpreter-and-its-environment/2.2.1-source-code-encoding/README.md).

## Tek görev

1. Kendi klasöründe print("ready") yazan betiğin başına bölümdeki shebang satırını koy.

2. Unix için chmod +x ve betik yolu üzerinden çalıştırma planını yaz; mümkünse yalnız bu dosyada dene.

3. Shebang önüne boş satır eklemenin, python3 komutunun PATH içinde olmamasının ve CRLF satır sonunun neden ayrı sorunlar olduğunu açıkla.

4. Windows .py/.pyw farkını kaynakla eşleştir.

## Geçiş ölçütleri

- [ ] #! dosyanın ilk iki karakteri ve shebang ilk satır.
- [ ] Yürütme izniyle yorumlayıcı bulunması ayrı koşullar.
- [ ] Encoding bildirimi gerekirse ikinci satıra yerleştirilmiş.
- [ ] Windows ilişkilendirmesi Unix izniyle karıştırılmamış; .pyw konsol davranışı belirtilmiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
