# Milestone: Sayıyı değeriyle birlikte taşı

## Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

## Tek görev

Signed iki baytlık ölçüm verisini int.from_bytes ile oku; hesaplanan sonucu int.to_bytes ile geri yaz. Negatif, sıfır ve sınır dışı sonuçları dene. Ayrı bir float örneğini as_integer_ratio ve hex/fromhex ile tam saklanan değerine geri döndür; complex sayıyı sıralamaya çalışmanın sınırını göster.

## Geçiş ölçütleri

- [ ] Bayt sırası ve signed seçimi bilinçli; yetersiz genişlik hatası açıklanır.
- [ ] Floatın saklanan değeri ile decimal görünümü ayrılır; int sınırsızlığı sabit bayt alanına taşınmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
