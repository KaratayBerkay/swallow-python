# Milestone: Satır tabanlı metni çözümle

## Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

## Tek görev

`"  Ada:7\nEce:9\nAda:8\n"` metnini splitlines ile satırlara ayır; kenar boşluklarını temizle; partition ile ad ve puanı çıkar. Boş ad, ayırıcısız satır ve boş metin girdilerini açıkça ele al. Yinelenen adların son değerini kullanıp adlara göre sıralı `ad=puan` metnini join ile üret; özgün metni koru.

## Geçiş ölçütleri

- [ ] Örnek çıktı Ada=8 ve Ece=9 satırlarıdır; hatalı satırların davranışı tutarlı seçilmiştir.
- [ ] Split/partition/strip/join seçimleri ve str değişmezliği açıklanmıştır; tüm yöntemleri gereksiz yere kullanma şartı yoktur.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
