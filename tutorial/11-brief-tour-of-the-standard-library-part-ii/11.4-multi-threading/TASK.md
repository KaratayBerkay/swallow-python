# Görev 11.4: Eşzamanlı akışta yalnız garanti edilen sırayı yaz

**Odak:** Thread.start, arka plan run, join ve paylaşılan kaynak koordinasyonu.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.3](../11.3-working-with-binary-data-record-layouts/README.md).
- Ön bilgi: [t:9.5](../../09-classes/9.5-inheritance/README.md).

## Tek görev

1. README içindeki AsyncZip sınıfını hazır örnek olarak incele.

2. Asıl örnekte üç mesaj için mümkün sıraları yaz: "Finished background zip", "The main program continues", "Main program waited".

3. Ayrı bir senkron sürümde aynı AsyncZip nesnesinin oluşturulmasından sonraki kodu aşağıdaki üç satırla değiştir. Bu sürümde start ve join çağrısı yok. Mesaj sırasını asıl örnekle karşılaştır:

```python
background.run()
print('The main program continues to run in foreground.')
print('Synchronous call finished.')
```

4. Paylaşılan tek dosyaya birden fazla thread yazması halinde bölümde önerilen tek kaynak sahibi thread + queue düzenini çiz. Thread veya zipfile iç APIlerini genişletmen gerekmiyor.

## Geçiş ölçütleri

- [ ] Asıl örnekte ilk iki mesajın sırası garanti edilmemiş; son mesaj her ikisinden sonra.
- [ ] Asıl örnekte start yeni akışı başlatıyor; join arka plan bitene kadar bekliyor.
- [ ] Senkron sürümde Finished background zip, The main program continues, Synchronous call finished sırası kesin; run normal metot çağrısı olarak bitmeden sonraki satıra geçilmiyor.
- [ ] Kuyruk ile tek kaynak sahibi yaklaşımının çakışan erişimi nasıl azalttığı açıklanmış; lock algoritması istenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
