# Görev 12.2: Oluşturma ile etkinleştirmeyi ayır

**Odak:** venv yorumlayıcı seçimi, activate/deactivate, sys.path ve PYTHONPATH sınırı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:12.1](../12.1-introduction/README.md).
- Ön bilgi: [t:6.2](../../06-modules/6.2-standard-modules/README.md).

## Tek görev

1. Yeni bir terminal oturumunda mevcut python --version sonucunu ve REPL içinde import sys sonrası sys.path listesini kaydet; quit() ile REPLden çık.

2. Kendi çalışma klasöründe henüz bulunmayan lesson-env dizinini python -m venv lesson-env ile oluştur. Bölümde işletim sistemin ve shellin için verilen activate yolunu kullan. Etkin ortamda python --version ve REPL içindeki sys.path gözlemini tekrarla; ortamın site-packages yolunu işaretle.

3. REPLden çıkıp deactivate çalıştır. Aynı gözlemi tekrar alarak terminalin önceki yorumlayıcı seçimine döndüğünü doğrula. Sürüm numarasının aynı kalmasının, ortamın değişmediği anlamına neden gelmediğini açıkla.

4. Python 3.12 yerine 3.11 ile ortam oluşturmanın sonucu, .venv/.env ayrımı ve PYTHONPATH sınırını not et. Paket indirme, global ayar değiştirme veya yeni yorumlayıcı kurma yok.

Kurulu yorumlayıcı venv oluşturmayı engelliyorsa gerçek hata kaydını sun; sistem kurulumu çözmek bu görevin kapsamı değildir. Uygulama kanıtı sağlanana kadar karar Kanıt bekleniyor olur; komut taslağı tek başına uygulama kanıtı sayılmaz.

## Geçiş ölçütleri

- [ ] venv kendisini çağıran Python sürümüyle oluşuyor; istenen başka sürümü kendiliğinden indirmiyor.
- [ ] Yerel lesson-env gerçekten oluşturulmuş; oluşturma ile shell içinde etkinleştirme ayrı olaylar olarak gösterilmiş.
- [ ] Önce/etkin/sonra gözlemleri var; etkin ortamın site-packages yolu sys.path içinde gösterilmiş. Yalnız istemdeki etikete veya sürüm numarasına bakılmamış.
- [ ] deactivate sonrasında önceki terminal seçimine dönüldüğü gerçek gözlemle doğrulanmış.
- [ ] Aktivasyon PYTHONPATH içeriğini temizleme garantisi vermiyor.
- [ ] Windows ve Unix yolları karıştırılmamış; .env değişken dosyası ile .venv dizini ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
