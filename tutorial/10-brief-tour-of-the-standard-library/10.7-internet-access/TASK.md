# Görev 10.7: Ağ örneğinin veri ve yan etki izini çıkar

**Odak:** urlopen yanıtı, bytes decode, satır filtresi, bağlam kapatma ve SMTP gönderim akışı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.2.1](../../07-input-and-output/7.2-reading-and-writing-files/7.2.1-methods-of-file-objects/README.md).
- Ön bilgi: [t:10.6](../10.6-mathematics/README.md).

## Tek görev

1. Ağ bağlantısı açmadan README örneğinin izini çıkar.

2. Yanıt satırlarını [b"Title\n", b"Last updated today\n"] kabul et; bölümdeki decode, "updated" filtresi ve rstrip işlemlerini bu liste üzerinde uygula.

3. SMTP örneğini yalnız kâğıt üzerinde SMTP bağlantısı, sendmail alıcı/gönderici/mesajı ve quit adımlarına ayır.

4. Taslakta gönderim yapan kodu çalıştırma; uzak işlem yapılmadan veri ve etki ayrımı değerlendiriliyor.

## Geçiş ölçütleri

- [ ] Yerel çıktı yalnız Last updated today; decode öncesi bytes, sonrası str.
- [ ] Satır sonunu kaldırma ile filtreleme ayrı işlemler olarak açıklanmış.
- [ ] with yanıt kaynağını kapatıyor; SMTP quit bağlantıyı bitiriyor.
- [ ] SMTP örneğinin sunucu gereksinimi ve sendmail çağrısının dış dünyaya mesaj gönderdiği doğru işaretlenmiş.
- [ ] Gerçek ağ servisi, e-posta hesabı veya gönderim gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
