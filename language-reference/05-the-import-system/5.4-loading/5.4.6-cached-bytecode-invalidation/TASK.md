# Görev 5.4.6: Bytecode geçerliliğini politika bazında ayır

**Odak:** Timestamp/size kontrolü ve checked/unchecked hash cache ayrımı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.5](../5.4.5-module-reprs/README.md).
- Ön bilgi: [t:6.1.3](../../../../tutorial/06-modules/6.1-more-on-modules/6.1.3-compiled-python-files/README.md).

## Tek görev

1. Üç sütunlu cache karar tablosu hazırla: timestamp+size, checked hash, unchecked hash.

2. Kaynağın zamanı/boyutu aynı kalırken içeriği değişmiş olsun; her politikada hangi verinin kontrol edildiğini, farkın fark edilip edilmeyebileceğini ve geçersiz checked hash durumunda ne olacağını yaz. --check-hash-based-pycs seçeneğinin hangi kararı etkileyebildiğini sözle belirt.

## Geçiş ölçütleri

- [ ] Metadata politikası yalnız zaman/boyut bilgisiyle karar veriyor; aynı metadata içerik değişimini kaçırabilir.
- [ ] Checked hash kaynak içeriğini hashleyip karşılaştırıyor ve geçersizse yeni checked cache üretiyor.
- [ ] Unchecked var olan cachei normalde geçerli kabul ediyor; bu davranış seçeneğe bağlı değişebilir.
- [ ] Cache politikası program sonucunun doğruluğuyla, .pyc yükleme hızıyla karıştırılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
